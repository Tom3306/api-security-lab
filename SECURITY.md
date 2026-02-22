# SECURITY.md

## Security Policy (Lab Project)

This repository is a portfolio/lab project. Security issues are still welcome and handled responsibly.

## Supported Scope
- FastAPI application code in `app/`
- Security tests in `tests/`
- CI security controls and scripts

## Reporting a Vulnerability
Please report privately with:
- Vulnerability type and impact
- Affected endpoint/file
- Reproduction steps (curl/request sample)
- Suggested fix (if available)

Avoid posting sensitive exploit details publicly in issues.

## Response Targets (Best Effort)
- Acknowledge report: within 3 business days
- Initial triage: within 7 business days
- Fix timeline: based on severity and complexity

## Severity (simple rubric)
- **High**: auth bypass, privilege escalation, data exposure
- **Medium**: exploitable weakness with compensating controls
- **Low**: hardening or best-practice gap

## Secure Development Practices Used
- Code scanning in CI (Bandit, Semgrep)
- Dependency/image/filesystem vulnerability scanning (Trivy)
- Secret scanning (Gitleaks)
- Threat modeling and runbook documentation
