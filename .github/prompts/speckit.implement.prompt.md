---
agent: speckit.implement
---

# Purpose

Implement the approved QA artifacts from the generated specification.

This prompt is responsible for transforming an approved specification into executable QA deliverables.

Do not generate application source code.

# Input

Use the following artifacts where available:

spec.md
review.md
judgespec.md
traceability.md
testplan.md
tasks.md

# Responsibilities

Perform the following activities.

1. Verify Specification Approval

Ensure:

Specification has been reviewed.
Critical review comments are resolved.
JudgeSpec status is PASS or PASS WITH COMMENTS.
Business assumptions are documented.

If the specification is not approved, stop and explain why implementation cannot continue.

2. Generate Test Assets

Create:

Manual Test Cases
Regression Suite
Smoke Suite
Validation Test Cases
Negative Test Cases
Boundary Value Tests
Permission Tests
UI Test Scenarios

Do not create duplicate test cases.

3. Validate Coverage

Verify that:

Every requirement has test coverage.
Every business rule has test coverage.
Every acceptance criterion has test coverage.
Every validation rule has test coverage.

Highlight uncovered requirements.

4. Prepare Test Data

Identify:

Required master data
Positive test data
Negative test data
Boundary data
Invalid data
Duplicate data
5. Generate Execution Order

Recommend the order of execution.

Example:

Smoke Testing
Functional Testing
Validation Testing
Permission Testing
Negative Testing
Boundary Testing
Regression Testing
6. Risk Assessment

Identify:

High-risk features
Critical workflows
Business-critical scenarios
Areas requiring exploratory testing
7. Implementation Summary

Produce a summary including:

Artifacts generated
Coverage achieved
Remaining risks
Missing information
Recommended next actions
Restrictions

Do not:

Generate application code.
Modify business requirements.
Invent missing functionality.
Ignore review findings.

Always base outputs on the approved specification.

Output

Generate the QA implementation package in Markdown, ready for execution by the QA team.

### Test Case Generation Standards & Mandatory Format

**⚠️ CRITICAL: All test cases MUST follow the Reference Format from Testcases-reference.xlsx**

Reference file: `specifications/011-central-repo/Testcases-reference.xlsx`
This file defines the MANDATORY structure and quality standards for ALL generated test cases.

### Test Case Format & Mandatory Fields (12 Columns)

**Every test case MUST include these 12 fields in this exact format:**

| Field | Format | Example | Requirement |
|-------|--------|---------|-------------|
| **Test Case ID** | TC_[MODULE]_[SEQUENCE] | TC_CENTRAL_001 | Unique, sequential, immutable |
| **Test Case Summary** | **SINGLE LINE**: One clear objective ONLY | "Admin can upload PDF file to Central Repository" | ATOMIC - ONE assertion per test case |
| **Prerequisites** | **MINIMAL numbered list** | 1. Admin user logged in; 2. PDF file available (2MB) | Only what's needed to setup |
| **Test Steps** | **Numbered concise actions** (3-5 steps) | 1. Click Upload; 2. Select PDF; 3. Submit | Sequential, clear, NOT verbose |
| **Expected Output** | **ONE clear expected result** | "File uploaded successfully, visible in document list" | Single assertion - NOT multiple checks |
| **Actual Output** | What actually happened | To be filled during execution | Exact result observed |
| **Test Status** | Pass / Fail / Blocked | Pass, Fail, or Blocked | Clear outcome |
| **Priority** | P1 / P2 / P3 | P1 | P1=Critical, P2=High, P3=Low |
| **Assignee** | Team member name | QA Engineer 1 | Clear responsibility |
| **Severity** | Critical / High / Medium / Low | Critical | Impact if broken |
| **JIRA Issue ID** | JIRA ticket reference | MHA-001 | Traceability link |
| **Comments** | Additional notes or findings | "Validates FR-PERM-001, FR-LIST-001" | Context + requirement mapping |

### Test Case Generation - KEY CHARACTERISTICS (MANDATORY)

**These are NON-NEGOTIABLE rules enforced from the Reference Format:**

✅ **ATOMIC TEST CASES** - Each test case tests EXACTLY ONE requirement or scenario
- ❌ DO NOT combine multiple assertions in one test case
- ✅ DO create separate test cases for each assertion

✅ **SINGLE EXPECTED OUTPUT** - Expected Output section contains ONE clear expectation
- ❌ DO NOT list 5-8 expected results per test case
- ✅ DO create new test cases if multiple outcomes need verification

✅ **MINIMAL PREREQUISITES** - Only setup steps required to execute this specific test
- ❌ DO NOT over-document setup
- ✅ DO make prerequisites numbered and concise (1-3 items typically)

✅ **CONCISE TEST STEPS** - 3-5 numbered actions, not lengthy narratives
- ❌ DO NOT write lengthy explanations
- ✅ DO use numbered steps: "1. Click X; 2. Enter Y; 3. Verify Z"

✅ **CLEAR TEST SUMMARY** - One-line description of what test verifies
- ❌ DO NOT write multi-line summaries
- ✅ DO write: "User can upload PDF file successfully"

✅ **COMPREHENSIVE COVERAGE** - Generate 200+ test cases for 80%+ requirement coverage
- Current target: Cover ALL 235+ requirements from requirements.md
- Target test case count: 200-250 test cases minimum
- Each requirement should map to at least one test case

✅ **REQUIREMENT TRACEABILITY** - Comments field MUST reference requirement IDs
- Example: "Validates FR-PERM-001, FR-LIST-002"
- Enables RTM generation and coverage tracking

### Test Case Generation & Mandatory Fields (12 Columns)

### Reference Examples - From Testcases-reference.xlsx (PackSize Feature - 143 Verified Test Cases)

These examples demonstrate the EXACT FORMAT all new test cases must follow:

#### Example 1: Atomic Test Case (✅ CORRECT)
```
Test Case ID:        TC_PCS_01
Summary:             Verify Admin can see client sub category option when adding a user
Prerequisites:       1. Admin user logged in; 2. Access to User Management
Test Steps:          1. Navigate to User Management; 2. Click Create New User; 3. Observe dropdown options
Expected Output:     Client sub category option is visible in user creation form
Priority:            P1
Severity:            High
Comments:            Validates FR-USR-001 (User type selection functionality)
```

#### Example 2: Atomic Test Case (✅ CORRECT)
```
Test Case ID:        TC_PCS_02
Summary:             Verify all proper options are shown under client sub category
Prerequisites:       1. Admin user logged in; 2. In User Creation form; 3. Client sub category field visible
Test Steps:          1. Click on Client sub category dropdown; 2. Observe all options; 3. Count distinct options
Expected Output:     All client sub category options (Bronze, Silver, Gold, Platinum) are displayed
Priority:            P1
Severity:            High
Comments:            Validates FR-USR-002 (Sub category options enumeration)"
```

#### Example 3: Atomic Test Case (✅ CORRECT)
```
Test Case ID:        TC_PCS_03
Summary:             Verify Admin can select one client sub category option at a time
Prerequisites:       1. Admin logged in; 2. User Creation form open; 3. Client sub category dropdown visible
Test Steps:          1. Click Client sub category dropdown; 2. Select "Silver" option; 3. Verify selection persists
Expected Output:     "Silver" option selected, highlighted, and retained in form
Priority:            P1
Severity:            Medium
Comments:            Validates FR-USR-003 (Sub category selection persistence)"
```

**Why These Examples are CORRECT** ✅:
- Each test case tests exactly ONE scenario
- Test Summary is ONE line, ONE clear objective
- Prerequisites are minimal (1-3 items)
- Test Steps are 3-5 concise numbered actions
- Expected Output contains ONE clear assertion
- NO combining of multiple verifications in one test case
- NO multiple expected outcomes listed
- Direct traceability to requirements (FR-USR-XXX)

**How NOT to Write Test Cases** ❌:
```
❌ BAD EXAMPLE - DO NOT FOLLOW THIS PATTERN:
Test Case ID:        TC_WRONG_001
Summary:             Verify user creation works and all fields save correctly and email is sent and audit log updated
Prerequisites:       User must be logged in with admin role and have mould selected and have rights and...
Test Steps:          1. Go to user management and click create and fill all fields and...
Expected Output:     1. User created; 2. Email sent; 3. Audit log entry; 4. DB synced; 5. Cache updated; 6. API called
Comments:            Multiple things being tested together - NOT ATOMIC
```

### Compliance & Validation Rules

**Before exporting to Excel, ALL test cases MUST pass this checklist:**

- [ ] **One Assertion Rule**: Each TC tests exactly one requirement/scenario
- [ ] **Expected Output Rule**: ONE clear expected result (not a list of 5-8 items)
- [ ] **Prerequisites Rule**: Minimal setup (1-3 items, numbered)
- [ ] **Steps Rule**: 3-5 concise actions (numbered, not narratives)
- [ ] **Summary Rule**: ONE line, clear objective
- [ ] **Traceability Rule**: Comments reference requirement ID (FR-XXX-XXX format)
- [ ] **Requirement Mapping**: Every TC linked to at least one requirement
- [ ] **Coverage Target**: Total TCs ≥ 200 for 80%+ coverage of 235 requirements

**Non-Atomic Test Cases MUST be split:**
- If a TC tests multiple scenarios → Split into separate TCs
- If Expected Output has multiple items (>1) → Split into separate TCs
- If Prerequisites are complex narrative → Simplify or split TCs
- Example: "Verify login AND redirect AND profile load" → Create 3 separate TCs

### Test Case Export Requirements

When exporting to Excel (via sync_testcases.py):
1. All 12 mandatory columns MUST be present in exact order
2. Each row = ONE atomic test case
3. Test Case IDs MUST be unique and sequential (TC_CENTRAL_001, TC_CENTRAL_002, etc.)
4. Headers preserved in Row 1
5. Column order preserved
6. No empty mandatory fields except "Actual Output" (filled during execution)
7. Excel file MUST be named: `test-cases.xlsx`

### Test Case Generation & Mandatory Fields 

**Every Requirement Tracebility MUST include:**
Requirements ID
Business Requirement 
Functional Requirement 
Test Scenario ID 
Test Case ID 
Coverage Status 
Regression Coverage 
Automation Candidate Mapping 

**Excel ready structure**
Output must be formatted and exported directly into:
Test case excel in .xlsx format 
RTM Excel in .xlsx format 

## RTM Structure
**Mandatory Columns:**
Requirement ID | Business Requirement | Functional Requirement | Module Name | Test Scenario ID | Test Case ID | Coverage Status | Regression Coverage | Automation Candidate | UAT Mapping | Defect Reference 

**Non-negotiable Deliverables:**
Test casea and RTM must be generated in Excel format, with clear mapping between requirements and test cases, ready for Client delivery and audit review. 
Also, the versioning of the deliverables must be maintained to ensure tracebility and governance compliance. 
Export the '.md' files generated for testcases and RTM into '.xlsx' format, ensuring all formatting and structure is preserved for immedidate use by the client and QA team. 
