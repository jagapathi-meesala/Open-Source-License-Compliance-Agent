# Open-Source License Compliance Agent

An offline advisory agent for reviewing user-supplied dependency inventories and license evidence.

## Features
- Organizes package, version, declared license, and evidence fields.
- Flags missing or ambiguous license information.
- Highlights notice, attribution, source-related, and compatibility questions for review.
- Drafts an evidence-linked checklist.

## Quick start
Python 3.10+:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python3 verification/readiness_audit.py
```

## Limitations
License obligations depend on actual license text, how software is modified, linked, combined or distributed, jurisdiction, and contracts. This agent is not legal advice and cannot certify compliance. It does not fetch packages or scan repositories automatically.
