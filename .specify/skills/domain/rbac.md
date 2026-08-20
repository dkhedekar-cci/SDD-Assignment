# Skill: RBAC and Access-Control Test Derivation (Project-Aware, Reusable)

## Purpose
Generate complete role-based test coverage from any feature spec while staying reusable for future modules.

## Scope
Use this skill when requirements involve:
- Protected routes/pages
- Permissioned actions (create/update/delete/approve/export/etc.)
- API authorization
- Role-based UI visibility
- Tenant/org/location boundaries

## Canonical Roles (current project baseline)
- **Admin**: Full system access
- **AHM**: Management access for mapped scope (client/account mappings apply)
- **Client**: Read-oriented access to own organization scope
- **Supplier**: Submission/data access limited to own supplier/location scope

> If a new spec introduces additional roles, append them to the role map before test generation.

## Core RBAC Principles
1. Authentication check happens before authorization check.
2. Authorization failure must not clear a valid authenticated session.
3. UI visibility checks are supportive; backend/API authorization is authoritative.
4. Scope boundaries (own org / mapped clients / own locations / tenant) are mandatory.
5. Denied access must not mutate data.
6. Error handling should avoid sensitive data leakage.

## Authorization Outcome Rules
For every protected action/route:
- **Allowed role** → success response/view.
- **Unauthorized role** → deny (`403` or unauthorized view), no sensitive data exposure.
- **Unauthenticated user** → deny/redirect (`401` or `/login`).
- **Denied attempt** → no data mutation, and audit/trace where required by spec/contracts.

## Mandatory RBAC Test Patterns
For each role-sensitive requirement, generate all applicable patterns:

1. **Allowed Access (Positive)**
   - Authorized role performs action successfully in valid scope.

2. **Denied Access (Negative)**
   - Unauthorized role is blocked with correct response/behavior.

3. **Scope Boundary**
   - Authorized role in wrong scope is blocked (cross-org/client/location/tenant).

4. **Privilege Escalation Attempt**
   - Lower-privilege role attempts higher-privilege action (direct URL/API tampering).

5. **Auth vs AuthZ Distinction**
   - Unauthenticated behavior differs correctly from authenticated-but-unauthorized behavior.

6. **UI Enforcement**
   - Restricted menu/actions hidden or disabled for unauthorized roles.

7. **No Side Effects on Denial**
   - Denied requests do not create/update/delete/approve data.

8. **Auditability**
   - Sensitive allow/deny events logged where required.

## Extraction Heuristics for New Specs
When applied to a new feature spec:
1. Identify all protected routes/actions/endpoints.
2. Identify role references and permission statements.
3. Identify scope qualifiers (`own`, `mapped`, `tenant`, `location`, `clientId`, etc.).
4. Build action-role-scope matrix first.
5. Generate tests from matrix; do not skip empty/ambiguous cells without explicit `N/A (reason)`.

## Coverage Minimum Rule (Hard Requirement)
For every role-sensitive requirement, generate at least:
- 1 test per allowed role group
- 1 test per denied role group
- 1 out-of-scope boundary test
- 1 privilege-escalation/tampering test

If a pattern is not applicable, include: `N/A (reason)`.

## Test Case Output Format (MANDATORY - project template)
All generated test cases MUST use exactly these columns and order:

1. Test case ID  
2. Test case summary  
3. Prerequisites  
4. Test Steps  
5. Expected Output  
6. Actual Output  
7. Test Status (Pass/Fail)  
8. Priority  
9. Assignee  
10. Severity  
11. JIRA Issue ID  
12. Comments

## Field Rules for Generation
- **Actual Output**: set to `TBD during execution`.
- **Test Status (Pass/Fail)**: set to `Not Executed`.
- **Assignee**: set to `Unassigned` unless explicitly provided.
- **JIRA Issue ID**: set to `TBD`.
- **Comments**: include classification tags such as:
  - `RBAC-positive`
  - `RBAC-negative`
  - `RBAC-scope-boundary`
  - `RBAC-privilege-escalation`
- **Test case ID**: keep consistent format, e.g. `TC-RBAC-001`, `TC-RBAC-002`.
- **Priority / Severity guidance**:
  - Privilege escalation / authorization bypass risk → `High / High`
  - Standard deny/allow verification → `Medium / Medium`
  - UI visibility-only checks → `Low / Low`

## Quality Gates (Fail Conditions)
Generation fails if any condition is true:
- Role-sensitive requirement has no RBAC test.
- Denied-path validation missing.
- Scope-boundary validation missing where scope exists.
- Duplicate semantic tests exist (same objective + same outcome intent).
- Test case does not map back to requirement reference.
- Output format deviates from mandated project template columns/order.