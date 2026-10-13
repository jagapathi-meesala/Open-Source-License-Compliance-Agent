"""Offline helpers for reviewing supplied license inventory data."""
def analyze_inventory(rows: list[dict]) -> dict:
    if not isinstance(rows, list):
        raise ValueError("rows must be a list")
    findings, normalized = [], []
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            findings.append({"row": i, "issue": "invalid-row", "severity": "medium"})
            continue
        package = str(row.get("package", "")).strip()
        version = str(row.get("version", "")).strip()
        license_id = str(row.get("license_id", "")).strip()
        evidence = str(row.get("evidence", "")).strip()
        normalized.append({"package": package, "version": version, "license_id": license_id, "evidence": evidence})
        for key, value, severity in [("missing-package", package, "medium"), ("missing-version", version, "low"), ("missing-license-id", license_id, "high")]:
            if not value:
                findings.append({"row": i, "issue": key, "severity": severity})
        if license_id and not evidence:
            findings.append({"row": i, "issue": "license-evidence-missing", "severity": "high"})
    return {"inventory": normalized, "findings": findings,
            "status": "requires-human-review" if findings else "evidence-provided-not-certified"}

def obligation_questions(license_id: str, distribution_context: str = "") -> list[str]:
    questions = []
    if not license_id.strip():
        questions.append("Obtain the applicable license text and verify the license identifier.")
    if not distribution_context.strip():
        questions.append("Document the distribution context, including whether software is modified, linked, or combined.")
    questions.extend([
        "Check requirements to preserve copyright and license notices.",
        "Check attribution and third-party notice requirements.",
        "Check any source-disclosure or source-offer conditions that may apply.",
        "Review compatibility across combined components using the actual license texts.",
    ])
    return questions
