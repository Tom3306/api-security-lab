# Interview Talking Points - API Security Lab

## 30-Second Summary
"I built a small API security lab in Python/FastAPI where I modeled API threats, added practical hardening controls, and enforced security checks in CI with Bandit, Semgrep, Trivy, and Gitleaks. I also added detection and incident-response documentation to show end-to-end security engineering." 

## What I Designed
- STRIDE threat model focused on real API risks (BOLA, auth abuse, injection, info disclosure).
- Security controls mapped to threats (validation, RBAC, logging, rate limiting).

## What I Built
- Security-focused tests and ZAP baseline automation.
- CI security gates with fail conditions on meaningful findings.
- Sigma-style detection examples + SOC triage workflow.

## What I Learned
- Security value increases when design, code checks, and operations are connected.
- Good logging/correlation IDs are critical for triage and incident response.
- "Shift-left" only works when findings are actionable and tuned.

## Challenges & Tradeoffs
- Balancing strict fail gates vs developer productivity.
- Reducing scanner noise while still catching high-risk issues.
- Keeping a lab realistic without overengineering.

## Likely Questions + Short Answers
- **Q: Why multiple scanners?**  
  A: Each covers different risk classes: SAST patterns, secret leaks, and known vulnerabilities.
- **Q: How do you avoid false positives?**  
  A: Start strict on high/critical, tune rules, and document suppressions with justification.
- **Q: What would you do next?**  
  A: Add auth abuse simulation tests, SIEM dashboards, and IaC policy checks.
