---
agent: speckit.specify
---
# QA Specification Generation Instructions

## Objective

Generate a comprehensive `spec.md` document from the provided
requirements, user stories, business documents, screenshots, UI mockups,
or any other available artifacts.

The generated specification should be complete enough that a QA engineer
can derive manual and automated test cases without requiring additional
clarification.

------------------------------------------------------------------------

# General Guidelines

## 1. Understand Before Writing

-   Read all provided inputs completely.
-   Do not assume missing information.
-   Identify ambiguities.
-   If requirements are incomplete, explicitly list assumptions.
-   Capture business intent instead of simply restating requirements.

## 2. Write from a QA Perspective

The specification should help QA answer: - What is being built? - Why
does it exist? - How should it behave? - What should never happen? -
What validations exist? - What edge cases must be tested?

## 3. Keep the Specification Implementation Independent

Avoid mentioning: - Database tables - Internal APIs - Source code -
Programming languages - Frameworks

Describe expected system behaviour only.

# Required Sections

1.  Feature Overview
2.  Scope (In Scope / Out of Scope)
3.  Actors
4.  Preconditions
5.  Functional Behaviour
6.  Field Definitions
7.  Business Rules
8.  Validation Rules
9.  Error Handling
10. Success Behaviour
11. Permissions
12. UI Behaviour
13. Edge Cases
14. Non-functional Requirements
15. Acceptance Criteria (prefer Gherkin)
16. Assumptions
17. Open Questions

# Writing Style

The specification should be: - Clear - Concise - Testable -
Unambiguous - Consistent - Professional

Avoid ambiguous wording or inventing missing business logic.

# QA Focus

The specification should enable creation of: - Functional tests -
Negative tests - Boundary tests - Validation tests - UI tests -
Permission tests - Regression tests - Smoke tests - Exploratory tests

# Output Requirements

-   Markdown format
-   Proper headings
-   Tables where appropriate
-   Bullet lists for readability
-   Self-contained
-   Separate confirmed requirements from assumptions
-   Suitable for manual and automation test design

---

## FOR EVERY FUNCTIONAL REQUIREMENT (MANDATORY TEST ANALYSIS)

This section defines the 8-step analytical process for decomposing functional requirements into comprehensive test coverage.

### Step 1: Understand the Business Objective (MANDATORY)

Before analyzing any requirement, understand:
- What business problem does this requirement solve?
- Who are the end users and stakeholders?
- What is the desired outcome?
- Why is this requirement important?

**Example**: "Enable users to reset password" → Business Objective: "Allow locked-out users to regain account access securely"

### Step 2: Identify the 10 Key Aspects (MANDATORY)

For EVERY functional requirement, identify and document:

**2.1 Validations** - What inputs must be validated?
- Email format validation
- Password strength rules
- Field length constraints
- Required vs optional fields
- Data type validation

**2.2 Business Rules** - What business logic applies?
- Password expiry rules
- Account lockout policies
- Reset token expiry
- Historical password restrictions
- Multi-attempt thresholds

**2.3 User Roles** - Who can perform this action?
- Admin reset capability
- User self-service reset
- Support agent reset capability
- Role-based access restrictions

**2.4 UI Behavior** - How does the interface behave?
- Form layout and field visibility
- Button states (enabled/disabled)
- Error message display
- Loading indicators
- Success confirmations
- Field tooltips and help text

**2.5 Workflow** - What is the sequence of operations?
- Step 1: User clicks "Forgot Password"
- Step 2: Enter email address
- Step 3: Verify email ownership
- Step 4: Set new password
- Step 5: Confirmation message
- Step 6: Redirect to login

**2.6 Error Conditions** - What can go wrong?
- Account not found
- Email not verified
- Token expired
- Token already used
- Invalid password format
- Weak password
- Network timeout
- Database unavailable

**2.7 Alternate Flows** - What are the alternative paths?
- Reset via security questions
- Reset via mobile number
- Admin-initiated reset
- Reset with email verification code vs token link
- Reset with temporary vs permanent password

**2.8 Edge Cases** - What boundary conditions exist?
- Very long email addresses
- Accounts with no email
- Recently deleted accounts
- Disabled accounts
- Accounts with pending reset
- Multiple simultaneous reset requests
- Token reuse attempts
- Reset during account migration

**2.9 Dependencies** - What external systems are involved?
- Email service (SMTP, SendGrid, AWS SES)
- User database
- Token management service
- Logging service
- Notification service
- Authentication service

**2.10 Acceptance Criteria** - What defines success?
- User receives reset email within 30 seconds
- Reset link valid for 24 hours
- Token is one-time use only
- New password must be at least 12 characters
- Password reset triggers security log entry
- User receives confirmation email after reset
- Previous sessions are invalidated

### Step 3: Generate Exhaustive Manual Test Cases (MANDATORY)

Based on the 10 aspects identified above, generate minimum 15-20 manual test cases.

**DO NOT** limit yourself to:
- One positive test case
- Happy path scenarios only
- Basic validation tests

**MUST INCLUDE**:
- Multiple positive test cases (different scenarios, different user roles, different data variations)
- Comprehensive negative test cases (each error condition)
- Boundary test cases (min/max values, edge inputs)
- Validation test cases (each validation rule)
- Workflow test cases (each workflow step)
- UI behavior test cases (each UI interaction)
- Alternate flow test cases (each alternate path)
- Permission test cases (each user role)
- Error recovery test cases (retry after error, timeout recovery)
- Integration test cases (cross-system validations)

Each test case must:
- Have a unique, descriptive title
- Document the prerequisite state
- List clear, step-by-step actions
- Define expected results (specific, measurable, observable)
- Include assertion points
- Reference the relevant requirement
- Categorize as: Positive | Negative | Boundary | Validation | Workflow | UI | Alternate | Permission | Error | Integration | Edge | Data | Audit | Regression

### Step 4: Ensure Complete Coverage (MANDATORY)

Verify that your test cases cover:
- ✓ ALL 10 aspects identified in Step 2
- ✓ ALL business rules
- ✓ ALL error conditions
- ✓ ALL user roles
- ✓ ALL workflow steps
- ✓ ALL alternate flows
- ✓ ALL edge cases
- ✓ ALL validations
- ✓ ALL UI behaviors
- ✓ ALL dependencies

**Test Coverage Checklist**:
- Positive scenarios: 3-5 test cases
- Negative scenarios (each error): 1 test case per error
- Boundary scenarios: 2-3 test cases
- Validation scenarios: 1 test case per validation rule
- Workflow scenarios: 1 test case per step
- UI behavior scenarios: 1 test case per behavior
- Permission scenarios: 1 test case per role
- Alternate flow scenarios: 1 test case per alternate
- Edge case scenarios: 1 test case per edge case
- Dependency scenarios: 1 test case per integration point

**Minimum Test Case Count by Aspect**:
- Validations: 6+ test cases
- Business Rules: 5+ test cases
- User Roles: 3+ test cases
- UI Behavior: 4+ test cases
- Workflows: 5+ test cases
- Error Conditions: 8+ test cases
- Alternate Flows: 3+ test cases
- Edge Cases: 4+ test cases
- Dependencies: 3+ test cases
- Acceptance Criteria: 4+ test cases

**Total**: Minimum 45+ test cases per functional requirement

### Step 5: Do NOT Stop After One Positive Test Case (MANDATORY)

**ANTI-PATTERN** ❌ - DO NOT DO THIS:
```
TC-1: User resets password successfully
- Action: Enter email, click reset, set new password
- Expected: Password changed
```

**CORRECT PATTERN** ✅ - DO THIS:

Multiple positive scenarios for password reset:
```
TC-1: User resets password with valid email
TC-2: User resets password with previously used password (must fail)
TC-3: User resets password, new password meets minimum requirements
TC-4: User resets password on first attempt
TC-5: User resets password after multiple failed login attempts
TC-6: User resets password using alternative email on file
TC-7: Admin resets user password without user action
```

Each positive scenario tests DIFFERENT conditions, DIFFERENT data, DIFFERENT user roles, DIFFERENT states.

### Step 6: Multiple Validations = Separate Test Cases (MANDATORY)

**ANTI-PATTERN** ❌ - DO NOT DO THIS:
```
TC-1: Reset password validates input
- Action: Try empty email, invalid format, weak password
- Expected: All validations fail
```

**CORRECT PATTERN** ✅ - DO THIS (Each validation = Separate TC):
```
TC-1: Email validation - empty email rejected
TC-2: Email validation - invalid format rejected
TC-3: Email validation - SQL injection attempt rejected
TC-4: Password validation - empty password rejected
TC-5: Password validation - password too short rejected
TC-6: Password validation - password without uppercase rejected
TC-7: Password validation - password without number rejected
TC-8: Password validation - password without special character rejected
TC-9: Password validation - same as previous password rejected
```

**Rule**: If a requirement specifies "X must be validated", create AT LEAST ONE test case per validation rule. If 8 validations exist, create 8+ validation test cases.

### Step 7: Report Uncovered or Ambiguous Requirements (MANDATORY)

If during this analysis you discover:

**Uncovered Requirements** - Aspects of the requirement that lack test coverage or seem incomplete:
- Document in section: "Test Coverage Gaps"
- Example: "Password reset via security questions is mentioned but no workflow defined"
- Action: Flag as uncovered until specification is clarified

**Ambiguous Requirements** - Aspects that are unclear or conflict with other requirements:
- Document in section: "Ambiguities Requiring Clarification"
- Example: "Is reset token valid for 24 hours or until next login?"
- Action: Request clarification before finalizing test cases

**Missing Information** - Details needed to complete test design:
- Document in section: "Information Needed"
- Example: "What is the minimum password length requirement?"
- Action: Obtain information before test case finalization

### Step 8: Produce Requirement Traceability Matrix (MANDATORY)

Create or update the Requirement Traceability Matrix (RTM) with:

**Columns**:
- Requirement ID (e.g., REQ-011-001)
- Requirement Description
- Test Case ID (e.g., TC-011-001)
- Test Case Title
- Coverage Status (✓ Covered | ⚠ Partial | ✗ Not Covered)
- Coverage Type (Positive | Negative | Boundary | Validation | Workflow | UI | Alternate | Permission | Error | Integration | Edge | Data | Audit | Regression)
- Verification Date
- Verification Status (Pass | Fail | Blocked)

**Mandatory Sections in RTM**:
1. **Summary Statistics**:
   - Total Requirements: X
   - Total Test Cases: Y
   - Coverage Percentage: (Y/X × Expected Coverage Factor) = Z%
   - Expected Coverage Factor: 5-10 (5 test cases per requirement minimum, up to 10 for complex requirements)

2. **Coverage by Aspect**:
   - Validations: X test cases
   - Business Rules: X test cases
   - User Roles: X test cases
   - UI Behaviors: X test cases
   - Workflows: X test cases
   - Error Conditions: X test cases
   - Alternate Flows: X test cases
   - Edge Cases: X test cases
   - Dependencies: X test cases
   - Acceptance Criteria: X test cases

3. **Verification Status**:
   - Passed: X test cases
   - Failed: X test cases (with reasons)
   - Blocked: X test cases (with blockers)
   - Not Yet Executed: X test cases

**RTM Requirements**:
- ✓ Every requirement mapped to minimum 5 test cases
- ✓ Every test case traced back to source requirement
- ✓ Every test case categorized by type
- ✓ Coverage percentage calculated and reported
- ✓ Uncovered requirements highlighted
- ✓ Updated whenever requirements change
- ✓ Reviewed for completeness before test execution

