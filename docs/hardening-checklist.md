# Hardening Checklist (Initial)

- [ ] Implement JWT auth with secure expiry and refresh strategy
- [ ] Enforce RBAC + object-level authorization checks
- [ ] Add request validation with strict schemas
- [ ] Use parameterized DB access only
- [ ] Add rate limits to auth and search routes
- [ ] Standardize error responses (avoid sensitive leakage)
- [ ] Add audit logs for auth/admin actions
- [ ] Integrate SAST/dependency checks in CI
- [ ] Add ZAP baseline scan in CI
- [ ] Define remediation SLA for high/critical findings
