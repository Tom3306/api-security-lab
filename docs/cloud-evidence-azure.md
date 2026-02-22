# Cloud Evidence Notes - Azure Hardening & IAM

## Goal
Document cloud security controls that would support this API project in Azure and provide evidence points suitable for interviews/audits.

## Reference Architecture (Azure)
- **Compute**: Azure App Service or AKS (private ingress preferred)
- **Data**: Azure Database for PostgreSQL (private endpoint)
- **Secrets**: Azure Key Vault
- **Identity**: Microsoft Entra ID + Managed Identity
- **Monitoring**: Azure Monitor + Log Analytics + Defender for Cloud

## Hardening Checklist (Azure-focused)

### Identity & Access Management
- Use **Managed Identity** for API service to access Key Vault/DB secrets (no hardcoded credentials).
- Enforce **least privilege RBAC**:
  - App identity: read only required Key Vault secrets
  - CI identity: scoped rights for deploy only
- Enable Conditional Access + MFA for admin roles.
- Review privileged role assignments monthly.

### Network Security
- Restrict public exposure:
  - Prefer private endpoints for DB and Key Vault
  - NSG rules deny-by-default, open only required ports
- Enable WAF in front of API (Application Gateway or Front Door).
- Disable broad egress where feasible; allowlist destination services.

### Data Protection
- Encryption at rest (Azure-managed keys minimum; CMK where required).
- TLS 1.2+ enforced for in-transit encryption.
- PostgreSQL configuration baseline:
  - disable overly permissive roles
  - restrict admin account usage

### Monitoring & Detection
- Send App, WAF, and DB audit logs to Log Analytics.
- Alerts for:
  - auth failure spikes
  - unusual admin role changes
  - unexpected secret access events
- Defender for Cloud recommendations reviewed and tracked.

### DevSecOps Controls
- Secret scanning in CI (Gitleaks) and repository protections.
- SAST (Bandit/Semgrep) + vulnerability scanning (Trivy).
- Branch protection requiring passing security gates.

## Evidence Artifacts to Collect
- Screenshot/export of Azure RBAC assignments (sanitized)
- Key Vault access policy / RBAC view
- NSG and private endpoint configuration evidence
- Azure Monitor alert rule definitions
- Defender for Cloud recommendation status
- CI run showing passing security gates

## Example Azure CLI Validation Snippets
```bash
# List role assignments for app managed identity
az role assignment list --assignee <principal-id> --all -o table

# Show Key Vault network/default action
az keyvault show -n <kv-name> --query "properties.networkAcls.defaultAction"

# List PostgreSQL firewall rules
az postgres flexible-server firewall-rule list -g <rg> -n <pg-server>
```

## Interview Angle
Keep it practical: explain that even a lab project can show cloud security maturity by demonstrating IAM scoping, private connectivity, monitoring, and verifiable security evidence.
