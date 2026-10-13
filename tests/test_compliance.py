import pytest
from core.compliance import analyze_inventory, obligation_questions

def test_non_list_rejected():
    with pytest.raises(ValueError): analyze_inventory("bad")
def test_missing_license_flagged():
    assert any(f["issue"] == "missing-license-id" for f in analyze_inventory([{"package":"x","version":"1"}])["findings"])
def test_declared_license_without_evidence_flagged():
    assert any(f["issue"] == "license-evidence-missing" for f in analyze_inventory([{"package":"x","version":"1","license_id":"MIT"}])["findings"])
def test_evidence_kept():
    r = analyze_inventory([{"package":"x","version":"1","license_id":"MIT","evidence":"LICENSE file"}])
    assert r["inventory"][0]["evidence"] == "LICENSE file"
def test_missing_package_flagged():
    assert any(f["issue"] == "missing-package" for f in analyze_inventory([{"version":"1"}])["findings"])
def test_complete_metadata_not_certified():
    r = analyze_inventory([{"package":"x","version":"1","license_id":"MIT","evidence":"text attached"}])
    assert r["status"] == "evidence-provided-not-certified"
def test_notice_question():
    assert any("notices" in x.lower() for x in obligation_questions("MIT","redistribution"))
def test_missing_distribution_context():
    assert any("distribution" in x.lower() for x in obligation_questions("MIT",""))
