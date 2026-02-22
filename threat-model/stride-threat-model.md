# STRIDE Threat Model - API Security Lab

## Scope
- FastAPI service endpoints
- Authentication and authorization checks
- Request validation and data handling
- PostgreSQL data store
- CI/CD and supporting secrets

## Assumptions
- Lab environment mirrors production patterns at small scale
- Logs are forwarded to a SIEM-compatible sink
- Secrets are intended to be provided via environment variables or a secrets manager

## STRIDE Table

| STRIDE Category | Threat Scenario | Impact | Existing/Planned Controls | Validation |
|---|---|---|---|---|
| **S - Spoofing** | Attacker uses forged/stolen JWT to impersonate user | Unauthorized access | JWT signature validation, short token TTL, issuer/audience checks, key rotation | Negative auth tests + expired token tests |
| **T - Tampering** | API payload modified to inject commands or alter critical fields | Data corruption / compromise | Input validation (Pydantic), parameterized queries/ORM usage, WAF rules | Injection test cases + SAST |
| **R - Repudiation** | User denies performing sensitive action | Investigation gaps | Structured audit logs with request ID, user ID, action, timestamp | Log review checklist + SIEM correlation |
| **I - Information Disclosure** | Excessive response data or verbose error leaks internals | Privacy leak / recon value | Response schema minimization, secure error handling, secret scanning | API response tests + DAST checks |
| **D - Denial of Service** | Credential stuffing or endpoint flooding | Service degradation / outage | Rate limiting, burst controls, alerting on 4xx/5xx spikes | Load/abuse simulation + alert tuning |
| **E - Elevation of Privilege** | Broken object-level authorization (BOLA) for resource access | Cross-tenant/user data access | RBAC/ABAC checks per object, deny-by-default authorization | Authorization unit/integration tests |

## Priority Risks (current phase)
1. BOLA / broken authorization on object access
2. Authentication weaknesses (token handling / session abuse)
3. Injection and unsafe input handling
4. Sensitive data exposure through errors/logs
5. API abuse (brute force/rate-limit bypass)

## Near-Term Mitigations
- Add per-route authorization tests for positive/negative cases
- Implement stricter response models for sensitive endpoints
- Enforce rate limiting and lockout thresholds on auth paths
- Introduce log schema with mandatory correlation ID
