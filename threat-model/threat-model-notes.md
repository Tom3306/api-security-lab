# Threat Model Notes - API Security Lab

## Scope
- FastAPI service exposing authentication and resource endpoints
- PostgreSQL backend
- Test and CI pipeline for security validation

## Assets
- User credentials / tokens
- Customer PII in API responses
- Administrative endpoints
- Audit logs and security test reports

## Entry Points
- `/auth/login`
- `/users/{id}`
- `/search`
- `/admin/*`

## Trust Boundaries
1. Internet client → API
2. API application → database
3. CI runner → security tooling and artifacts

## Initial Threats (STRIDE-style)
- **Spoofing:** weak authentication controls, token misuse
- **Tampering:** unsanitized input causing SQL/command injection
- **Repudiation:** insufficient auth/audit trails
- **Information Disclosure:** verbose errors, overexposed fields
- **Denial of Service:** missing rate limits on auth/search endpoints
- **Elevation of Privilege:** role-check bypass / BOLA

## Mitigations Planned
- Strong password policy + secure token expiration/rotation
- Parameterized DB queries + strict input validation
- RBAC checks at route and object level
- Response filtering + centralized error handling
- Rate limiting on sensitive endpoints
- Audit event logging for auth/admin actions

## Verification Plan
- Unit/integration tests for authz/authn boundaries
- Negative tests for injection and privilege escalation
- OWASP ZAP baseline in CI for regression detection
