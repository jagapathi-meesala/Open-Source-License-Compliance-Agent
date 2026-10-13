# Explainability

This document explains the agent's inputs, decision process, outputs, and limitations.

## Inputs
The agent accepts user-supplied dependency inventories, package names and versions, SPDX identifiers, license text excerpts, package metadata, notice files, and distribution context. Missing evidence is explicitly identified.

## Decision
The agent separates declared license metadata from verified evidence. It flags missing or conflicting information and raises questions about attribution, notice preservation, source-related conditions, and license compatibility. It does not decide legal compatibility solely from an SPDX label.

## Limits
The agent does not fetch or scan packages, independently verify repositories, or provide legal advice. Obligations depend on actual license text, modifications, linking, distribution, jurisdiction, and contracts. Findings are review prompts, not legal conclusions.

## Tool: analyze-license-inventory

### Inputs and Data Sources
Receives a dependency inventory and supplied license identifiers, versions, and evidence references.

### Decision and Reasoning
Checks whether key fields are present and distinguishes declared identifiers from supporting evidence.

### Outputs and Evidence
Returns an organized inventory with missing or conflicting evidence flagged.

### Limits and Constraints
Package names alone do not establish a license. The tool cannot independently verify repository content.

### Failure Handling
If rows are malformed or fields are absent, report missing fields rather than guessing.

### Human Review
A maintainer verifies each dependency against authoritative package and repository license materials.

## Tool: review-license-obligations

### Inputs and Data Sources
Receives license identifiers or text, notice files, dependency context, and distribution details supplied by the user.

### Decision and Reasoning
Highlights obligation questions including attribution, notice preservation, source-related conditions, and compatibility concerns.

### Outputs and Evidence
Returns conditional review questions linked to supplied evidence; it does not render a legal verdict.

### Limits and Constraints
SPDX identifiers do not replace reading applicable license text or assessing the use case.

### Failure Handling
When license text or distribution context is missing, mark the assessment incomplete.

### Human Review
A qualified reviewer resolves material ambiguity before release.

## Tool: generate-compliance-report

### Inputs and Data Sources
Receives the inventory, identified gaps, evidence references, and intended distribution context.

### Decision and Reasoning
Prioritizes follow-up based on missing evidence, conflicting metadata, and potentially significant obligations.

### Outputs and Evidence
Produces a draft report, evidence checklist, and unresolved questions.

### Limits and Constraints
The report is not a compliance certification, legal opinion, or substitute for organizational policy.

### Failure Handling
If evidence is incomplete, retain an incomplete status and list required follow-up.

### Human Review
Maintainers and, where appropriate, qualified counsel approve final interpretations and release decisions.

## Evidence and Uncertainty
Findings should reference supplied metadata or license text. Conflicting declarations must be surfaced, not silently reconciled.

## Security and Responsible Use
Do not include private registry tokens, credentials, or confidential source details in reports.

## Audit and Reproducibility
Record package versions, evidence sources, license text versions, distribution model, review decisions, and unresolved issues.
