# SOC Triage Notes - API Abuse Scenarios

## Purpose
Quick triage playbook for common API abuse patterns observed in this lab.

## Scenario A: Brute Force on `/auth/login`
**Indicators**
- High count of `401/403` from one IP/user-agent
- Spike in auth failures without matching success volume

**Triage Steps (first 15 minutes)**
1. Validate alert fidelity: pull logs for last 15 minutes (source IP, user-agent, username).
2. Check spread: single target account vs many accounts.
3. Identify success-after-fail pattern (possible account compromise).
4. Cross-check with threat intel / known scanner IP ranges.
5. Apply temporary controls if active (WAF/IP block/rate-limit tighten).

**Evidence to collect**
- Raw auth logs with timestamps and correlation IDs
- Affected accounts list
- GeoIP and ASN context

**Escalate when**
- Any suspicious successful login follows brute-force burst
- Attempts target privileged/admin accounts

---

## Scenario B: BOLA/Object Enumeration
**Indicators**
- Authenticated user requests many sequential object IDs
- High ratio of denied access (`403/404`) on object endpoints

**Triage Steps**
1. Identify requesting account/API key and role.
2. Compare requested object ownership vs user scope.
3. Confirm if behavior matches QA or automation allowlist.
4. Review endpoint auth logic and recent code changes.

**Containment options**
- Disable/revoke affected API key or token
- Temporary policy rule to block high-rate object ID probing

**Escalate when**
- Data from unauthorized tenant/object returned (`200` where deny expected)
- Pattern repeats across multiple accounts from same origin

---

## Scenario C: Error/Debug Information Leakage
**Indicators**
- Increased `500` responses with stack trace text
- Logs/responses contain secrets, SQL fragments, or internal paths

**Triage Steps**
1. Capture sample response bodies and error logs.
2. Determine exposure scope (which endpoint, how long, how many requests).
3. Verify if sensitive values were returned externally.
4. Open incident and force secret rotation if exposure confirmed.

## Severity Guide
- **High**: Confirmed unauthorized access, credential compromise, or sensitive data exposure
- **Medium**: Active abuse attempts without evidence of successful compromise
- **Low**: Noise/scanner activity with effective controls

## Recommended Queries (pseudo)
```text
# Brute force indicator
where http.path = "/auth/login" and status in (401,403)
| stats count() by src.ip, user_agent, username, bin(5m)

# Enumeration indicator
where http.path like "/api/v1/objects/%" and status in (403,404)
| stats count_distinct(http.path) by user.id, src.ip, bin(10m)
```
