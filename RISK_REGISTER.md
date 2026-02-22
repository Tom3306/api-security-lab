# Risk Register - API Security Lab

| ID | Risk | Likelihood | Impact | Rating | Owner | Mitigation | Status |
|---|---|---|---|---|---|---|---|
| R-01 | Broken object-level authorization (BOLA) | Medium | High | High | Project Owner | Enforce object-level checks + negative tests | Open |
| R-02 | Brute-force auth abuse | High | Medium | High | Project Owner | Rate limiting, lockouts, detection alerts | Open |
| R-03 | Injection via unsafe input handling | Medium | High | High | Project Owner | Validation + ORM parameterization + SAST | Open |
| R-04 | Sensitive data leakage in errors/logs | Medium | High | High | Project Owner | Sanitize responses/logs, secure error handling | Open |
| R-05 | Secrets accidentally committed | Low | High | Medium | Project Owner | Gitleaks in CI + secret hygiene checklist | Mitigating |
| R-06 | Vulnerable dependency introduced | Medium | Medium | Medium | Project Owner | Trivy scanning + pinned versions + updates | Open |

## Review Cadence
- Review risks at least once per sprint or after major feature changes.
- Update likelihood/impact based on test and incident outcomes.
