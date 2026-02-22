# Incident Runbook - API Security Lab

## 1) Trigger Conditions
Start this runbook when one of the following occurs:
- Confirmed unauthorized API access
- Suspicious auth abuse spike (credential stuffing/brute force)
- Sensitive data exposure in response/logs
- Secret leak detected in repo/CI

## 2) Initial Actions (0-15 min)
1. Declare incident severity (Low/Medium/High).
2. Preserve evidence: logs, timestamps, request IDs, affected endpoints.
3. Contain active abuse:
   - tighten rate limits
   - block malicious IP/user-agent patterns
   - revoke suspicious tokens/keys
4. Assign roles: incident lead, comms owner, investigator.

## 3) Investigation (15-60 min)
- Build timeline of attacker/request activity.
- Identify blast radius:
  - affected users/data
  - impacted systems
  - potential persistence
- Validate root cause:
  - auth logic
  - authorization checks
  - input validation
  - configuration drift

## 4) Eradication & Recovery
- Patch vulnerable code/config.
- Rotate affected credentials/secrets.
- Re-run security tests and CI gates.
- Monitor for recurrence for at least 24 hours.

## 5) Communication
- Internal update includes: impact, current status, next checkpoint.
- For external/customer context (if applicable): concise impact statement and remediation status.

## 6) Post-Incident Review
Within 3 business days:
- Document root cause and timeline
- Record what worked/failed in response
- Add or improve:
  - tests
  - detection rules
  - runbook steps
  - risk register entries

## Useful Commands (examples)
```bash
# Run tests quickly
pytest -q

# Local static scans
bandit -r app -q
semgrep --config p/owasp-top-ten app --error
```
