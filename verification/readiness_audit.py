from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = ["agent.yaml","SOUL.md","README.md","RULES.md","DUTIES.md","AGENTS.md","EXPLAINABILITY.md","requirements.txt","pytest.ini","core/compliance.py","tools/analyze-license-inventory.yaml","tools/review-license-obligations.yaml","tools/generate-compliance-report.yaml","skills/license-inventory/SKILL.md","skills/obligation-review/SKILL.md","skills/compliance-reporting/SKILL.md","tests/test_compliance.py","verification/readiness_audit.py"]
missing = [p for p in required if not (root/p).is_file()]
if missing:
    print("FAIL: missing required files:", ", ".join(missing)); sys.exit(1)
print(f"PASS: all {len(required)}/{len(required)} required files present")
