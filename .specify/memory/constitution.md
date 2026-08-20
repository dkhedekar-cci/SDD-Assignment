# MHA (Mould & Handling Application) Constitution
<!-- Specification & Quality Assurance Constitution -->

## Core Principles

### I. Single Source of Truth
Every specification and requirement must have one authoritative source; All changes tracked through version control; No conflicting requirements across documents; Stakeholder consensus required before finalization

### II. Test-First Validation (NON-NEGOTIABLE)
Every requirement must have corresponding test cases; Acceptance criteria defined in Given/When/Then format; Tests written before implementation begins; Red-Green-Refactor cycle strictly enforced; No code ships without passing tests

### III. Specification Completeness
Every feature requires comprehensive specification covering functional and non-functional requirements; Edge cases identified and documented; Acceptance scenarios defined (minimum 2-3 per user story); Dependencies clearly mapped; Success criteria measurable and testable

### IV. Cross-Functional Alignment
Product, Technical, QA, and Security teams review and approve every specification before development; Stakeholder sign-off documented with dates; Design decisions recorded in Clarifications section; No ambiguity allowed at approval time

### V. Traceability & Coverage
Every requirement (FR-XXX, NFR-XXX) linked to test cases; Test coverage targets: P1=100%, P2=80%+, P3=50%+; Requirement IDs remain stable throughout lifecycle; Coverage metrics tracked and reported; Impact analysis conducted for changes

## Quality Assurance Standards

### Test Case Format & Mandatory Fields

**Every test case MUST include these 12 fields in this exact format:**

| Field | Format | Example | Requirement |
|-------|--------|---------|-------------|
| **Test Case ID** | TC_[MODULE]_[SEQUENCE] | TC_PACKSZ_001 | Unique, sequential, immutable |
| **Test Case Summary** | Concise one-liner | "Verify client can add pack size commitment" | Clear and actionable |
| **Prerequisites** | List of required setup | User logged in, Client role assigned, Mould active | Specific and complete |
| **Test Steps** | Numbered step-by-step actions | 1. Navigate to Pack Size; 2. Click Add; 3. Enter volume... | Sequential and clear |
| **Expected Output** | What should happen | "Commitment saved with green success message, DB updated" | Precise and testable |
| **Actual Output** | What actually happened | To be filled during execution | Exact result observed |
| **Test Status** | Pass / Fail / Blocked | Pass, Fail, or Blocked | Clear outcome |
| **Priority** | P1 / P2 / P3 | P1 | P1=Critical, P2=High, P3=Low |
| **Assignee** | Team member name | John Doe (QA) | Clear responsibility |
| **Severity** | Critical / High / Medium / Low | Critical | Impact if broken |
| **JIRA Issue ID** | JIRA ticket reference | MHA-1234 | Traceability link |
| **Comments** | Additional notes or findings | "Test data reused from MHA-1100" | Context for future reference |

### Test Scenario Coverage - Mandatory Categories (NO MISSING SCENARIOS)

**For EVERY requirement, test cases MUST cover ALL 10 categories below. No test scenarios can be missing.**

#### 1. **Happy Path / Positive Scenarios** (Baseline)
- Standard use case with valid inputs
- Expected successful outcome
- **Minimum 1 test case per requirement**
- **Priority: P1**
- **Severity: Critical**

#### 2. **Alternative Path / Business Logic Scenarios**
- Valid but less common workflows
- Different user roles performing same action
- Different business unit combinations
- **Minimum 1-2 test cases per requirement**
- **Priority: P2**
- **Severity: High**

#### 3. **Edge Cases / Boundary Scenarios**
- Minimum valid values (0, 1, empty string, null)
- Maximum valid values (999,999, max date, etc.)
- Boundary transitions (e.g., 85% → 86% utilisation threshold)
- Date boundaries (month-end, year-end, leap year)
- **Minimum 1-2 test cases per requirement**
- **Priority: P2**
- **Severity: High**

#### 4. **Error Handling / Negative Scenarios**
- Invalid inputs (negative numbers, special characters, exceeding limits)
- Missing mandatory fields
- Unauthorized access attempts
- System constraint violations (e.g., over-capacity)
- **Minimum 1-2 test cases per requirement**
- **Priority: P2**
- **Severity: High**

#### 5. **Validation Scenarios**
- Field-level validation (format, length, data type)
- Cross-field validation (dependency checks)
- Business rule validation (e.g., committed capacity > available capacity)
- Duplicate prevention
- **Minimum 1-2 test cases per requirement**
- **Priority: P2**
- **Severity: Medium**

#### 6. **Integration Scenarios** (If applicable)
- Multi-step workflows across modules
- Data consistency across systems
- API contract validation
- Concurrent user operations
- **Minimum 1-2 test cases per requirement**
- **Priority: P2**
- **Severity: High**

#### 7. **Performance & Load Scenarios** (If applicable)
- Response time validation (must be < X seconds)
- Bulk operations (import 10,000 records)
- Concurrent user load (50+ users simultaneously)
- **Minimum 1 test case per NFR**
- **Priority: P3**
- **Severity: Medium**

#### 8. **Security & Permission Scenarios**
- Role-based access control (Admin vs Client vs Supplier)
- Data isolation (Can User A see User B's data? They shouldn't.)
- Injection attack prevention (SQL, XSS)
- **Minimum 1-2 test cases per requirement**
- **Priority: P1**
- **Severity: Critical**

#### 9. **UI/UX Scenarios**
- Form validation messages appear correctly
- Error messages are user-friendly
- Navigation flows work as expected
- Mobile responsiveness (if applicable)
- **Minimum 1 test case per requirement**
- **Priority: P3**
- **Severity: Low**

#### 10. **Data Consistency Scenarios**
- Create → Read → Update → Delete (CRUD) operations
- Database rollback on error
- Data audit trail captures all changes
- Undo/redo functionality (if applicable)
- **Minimum 1-2 test cases per requirement**
- **Priority: P2**
- **Severity: Medium**

### Test Coverage Calculation

### VI. Test Case File Synchronization (MANDATORY)

**CRITICAL RULE**: Markdown, Excel, and RTM files MUST have EXACTLY the same test case counts and data.

#### Rule Summary
- Every feature implementation requires test cases in MULTIPLE synchronized formats
- Markdown (.md) = Reference/Documentation version
- Excel (.xlsx) = ALM import/Test execution version
- RTM (.xlsx) = Requirements Traceability Matrix version
- **ALL THREE MUST ALWAYS BE IN SYNC** (same counts, same data)

#### Synchronization Requirements

**1. Count Verification (MANDATORY at every export)**
```bash
# Get markdown count
grep -c "^#### TC_" testcases.md

# Get Excel count (rows minus header)
python -c "import openpyxl; wb = openpyxl.load_workbook('test-cases.xlsx'); ws = wb.active; print(f'{ws.max_row - 1}')"

# These MUST BE IDENTICAL
# If not equal → DO NOT PROCEED (regenerate immediately)
```

**2. Data Verification (MANDATORY)**
- Every test case ID in markdown must exist in Excel
- Every test case in Excel must have corresponding markdown entry
- Test case details (Summary, Prerequisites, Steps, Expected Output, etc.) must match across all formats
- RTM must have ≥80% coverage of test cases (80+ mappings for 100+ TCs expected)
- If ANY mismatch detected → **REGENERATE SYNCED FILES IMMEDIATELY**

**3. Failure Handling Protocol (MANDATORY)**
- IF count mismatch detected → STOP
- Delete the incomplete/older file
- Regenerate from primary source (Excel is master)
- Use programmatic sync scripts (NOT manual editing, NOT regex extraction)
- Re-run verification to confirm all counts match
- Document the incident in project version log

**4. Sync Workflow (MANDATORY for all regenerations)**
- **Step 1**: Generate/update test-cases.xlsx (primary source)
- **Step 2**: Verify Excel count
- **Step 3**: Run sync script to regenerate testcases.md from Excel
- **Step 4**: Verify markdown count matches Excel count
- **Step 5**: Regenerate RTM with all requirement mappings
- **Step 6**: Run comprehensive verification
- **Step 7**: Update version log with counts and "✅ VERIFIED" status

**5. Anti-Patterns (DO NOT DO - VIOLATIONS)**
- ❌ Never accept markdown count ≠ Excel count
- ❌ Never manually edit files instead of running automated sync scripts
- ❌ Never deploy files with partial/incomplete test cases
- ❌ Never skip verification step before marking files as ready
- ❌ Never use regex extraction for production (unreliable and error-prone)
- ❌ Never leave files out-of-sync for "later fixing"

**6. Documentation (MANDATORY)**
- Every time test case files are generated/synced, update version log
- Record: Timestamp, Markdown count, Excel count, RTM count, Verification status (✅ or ❌)
- Example: `2026-07-10 | 217 TCs | Excel: 217 | Markdown: 217 | RTM: 85 | Status: ✅ VERIFIED SYNC`
- Do not proceed with test execution until all counts are verified and documented

#### Example: Central Repository Feature (011)
- **Markdown**: testcases.md = 217 atomic test cases
- **Excel**: test-cases.xlsx = 217 rows (excluding header)
- **RTM**: rtm.xlsx = 85 unique requirement mappings
- **Status**: ✅ ALL SYNCHRONIZED (217 = 217, coverage: 85 mappings)
- **Next Regeneration**: Use SAME procedure to maintain sync

#### Tools & Scripts
- **Primary Generation**: final_export_all_tc.py (generates Excel with all TCs)
- **RTM Generation**: generate_rtm_complete.py (maps requirements to TCs)
- **Markdown Sync**: sync_markdown_to_excel.py (regenerates markdown from Excel)
- **Verification**: verify_complete_sync.py (verifies all 3 files match)

---

**Reference Implementation**: See `specifications/011-central-repo/implementation.md` Section 0 for detailed procedures specific to each feature.

---

### VII. Atomic Test Case Format & Mandatory Structure (MANDATORY)

**CRITICAL**: Every test case MUST follow this exact structure. No deviations allowed.

#### Rule: ATOMIC TEST CASES ONLY
- ✅ Each test case tests **EXACTLY ONE requirement or scenario** (atomic)
- ✅ Each test case has **ONE clear assertion** (single expected outcome)
- ✅ Separate test cases created for each distinct verification (not bundled)
- **Violation**: Combining multiple requirements into one TC = automatic rejection

#### Rule: 12-COLUMN MANDATORY FORMAT (IMMUTABLE)

**Every test case MUST include ALL 12 columns in this exact order:**

| # | Column Name | Format | Example | Requirement |
|---|---|---|---|---|
| 1 | **Test Case ID** | TC_[MODULE]_[SEQUENCE] | TC_PACKSZ_001 | Unique, sequential, immutable |
| 2 | **Test Case Summary** | One-line objective (concise) | "Verify client can add pack size" | Clear and actionable (NOT multi-line) |
| 3 | **Prerequisites** | List of required setup (1-3 items) | "User logged in; Client role; Mould active" | Specific, complete, minimal |
| 4 | **Test Steps** | Numbered step-by-step actions (3-5 steps) | "1. Navigate to Pack Size\n2. Click Add\n3. Enter volume" | Sequential, clear, NOT narrative |
| 5 | **Expected Output** | ONE clear expected result | "Commitment saved with success message" | Precise, testable, ONE outcome (NOT a checklist) |
| 6 | **Actual Output** | What actually happened | "Commitment saved successfully" | Filled during test execution |
| 7 | **Test Status** | Pass / Fail / Blocked | Pass | Clear outcome only |
| 8 | **Priority** | P1 / P2 / P3 | P1 | P1=Critical, P2=High, P3=Low |
| 9 | **Assignee** | Team member name | John Doe (QA) | Clear responsibility |
| 10 | **Severity** | Critical / High / Medium / Low | Critical | Impact if broken |
| 11 | **JIRA Issue ID** | JIRA ticket reference | MHA-1234 | Traceability link |
| 12 | **Comments** | Additional notes and findings | "Test data reused from MHA-1100" | Context for future reference |

#### Rule: QUALITY CHARACTERISTICS (MANDATORY)

Every test case MUST demonstrate ALL of these characteristics:

1. **Requirement Traceability** (MANDATORY)
   - Every TC linked to at least one requirement (in Comments field)
   - Example: "Validates FR-PERM-001" or "Tests NFR-PERF-003"
   - NO orphan test cases without requirement link

2. **Atomic Granularity** (MANDATORY)
   - Each TC tests ONE specific requirement (not multiple)
   - If testing multiple requirements → SPLIT into separate TCs
   - Example: WRONG = "Upload file AND verify in list AND download AND delete"
   - Example: RIGHT = Separate TCs: Upload (TC_1), Verify (TC_2), Download (TC_3), Delete (TC_4)

3. **Minimal Prerequisites** (MANDATORY)
   - Only setup required for THIS specific test
   - NOT over-documented
   - 1-3 numbered setup items (typical range)
   - Example: "User logged in; Client role assigned" (sufficient)
   - Example WRONG: Long narrative about system setup (too verbose)

4. **Concise Steps** (MANDATORY)
   - 3-5 numbered actions (typical range)
   - Clear, sequential, no narrative
   - Example: "1. Click Upload\n2. Select file\n3. Click Submit"
   - Example WRONG: "The user should navigate to the upload dialog and carefully select..."

5. **Single Expected Output** (MANDATORY)
   - ONE assertion per test case (not multiple)
   - Example: "File uploaded successfully with green confirmation message"
   - Example WRONG: "File uploaded, appears in list, shows correct size, correct date"
   - If multiple items → SPLIT into separate TCs

6. **Complete Coverage** (MANDATORY)
   - All 10 test scenario categories must be covered for EVERY requirement
   - See Constitution Section IV (Test Scenario Coverage - 10 Categories)
   - Coverage targets: P1=100%, P2=80%+, P3=50%+

#### Rule: NO TEST CASE VIOLATIONS (MANDATORY)

**These patterns are VIOLATIONS and MUST be rejected:**

- ❌ **Multi-Requirement TCs**: "Test upload AND download AND delete" → SPLIT
- ❌ **Multiple Assertions**: "File saved AND shows in list AND size correct" → SPLIT
- ❌ **Narrative Steps**: Long descriptions instead of numbered actions → REWRITE
- ❌ **Vague Expected Output**: "System works correctly" → SPECIFY
- ❌ **Missing Traceability**: No requirement link in Comments → ADD
- ❌ **Incomplete Format**: Missing any of 12 columns → COMPLETE
- ❌ **Invalid ID Format**: "TEST_001" or "TC001" instead of "TC_PACKSZ_001" → CORRECT
- ❌ **Multi-line Summary**: Summary has 2+ lines → MAKE CONCISE
- ❌ **Over-documented Prerequisites**: 5+ items → MINIMIZE to 1-3 essentials
- ❌ **Missing Status/Priority**: These fields are mandatory → FILL

#### Rule: FORMAT REFERENCE & EXAMPLES

**Where to find format specifications and examples:**
- Location: `specifications/[feature]/Testcases-reference.xlsx`
- Contains: 100+ verified example test cases with correct format
- Feature Example: PackSize feature (143 verified TCs)
- What to do: Copy format, adapt for your feature, ensure atomicity

**Current Feature 011 Status:**
- Format: ✅ All 217 TCs follow 12-column format
- Atomicity: ✅ All 217 TCs test exactly one requirement
- Traceability: ✅ All 217 TCs have requirement links
- Quality: ✅ All 217 TCs meet quality characteristics

---

### VIII. Test Scenario Coverage: 10 Mandatory Categories (MANDATORY)

**For EVERY requirement, test cases MUST cover ALL 10 categories below. No missing scenarios.**

See Constitution Section IV (earlier in this document) for detailed requirements for each category:

1. **Happy Path / Positive Scenarios** (P1, Critical)
2. **Alternative Path / Business Logic** (P2, High)
3. **Edge Cases / Boundary Scenarios** (P2, High)
4. **Error Handling / Negative Scenarios** (P2, High)
5. **Validation Scenarios** (P2, Medium)
6. **Integration Scenarios** (P2, High)
7. **Performance & Load Scenarios** (P3, Medium)
8. **Security & Permission Scenarios** (P1, Critical)
9. **UI/UX Scenarios** (P3, Low)
10. **Data Consistency Scenarios** (P2, Medium)

**Coverage Calculation**:
- Count: Number of test cases covering requirement X
- Minimum coverage: At least 1 TC per category (10 TCs per requirement minimum)
- Target: 2-3 TCs per category (20-30 TCs per high-priority requirement ideal)

**Example: Requirement FR-UPLOAD-001**
- Category 1 (Happy Path): TC_CENTRAL_001 (admin upload)
- Category 2 (Alternative): TC_CENTRAL_008 (client upload)
- Category 3 (Edge Cases): TC_CENTRAL_021 (exactly 10MB limit)
- Category 4 (Error Handling): TC_CENTRAL_031 (.exe file rejection)
- Category 5 (Validation): TC_CENTRAL_041 (file type validation)
- Category 6 (Integration): TC_CENTRAL_051 (auth integration)
- Category 7 (Performance): TC_CENTRAL_061 (upload speed SLA)
- Category 8 (Security): TC_CENTRAL_071 (RBAC permission check)
- Category 9 (UI/UX): TC_CENTRAL_081 (form responsiveness)
- Category 10 (Data Consistency): TC_CENTRAL_091 (database consistency)
- **Total**: 10 TCs covering all 10 categories for requirement FR-UPLOAD-001

**Rule Violation**: If ANY category is missing → Test coverage is incomplete → DO NOT PROCEED

---

### IX. Test Design Rules & Quality Standards (MANDATORY)

**CRITICAL**: These rules govern HOW test cases are designed, generated, and validated.

#### Rule: EXHAUSTIVE MANUAL TEST CASE GENERATION (MANDATORY)

**Requirement**: Every functional requirement MUST have comprehensive test case coverage.

**What This Means**:
- Generate test cases for EVERY aspect of requirement behavior
- Test all user interactions and system responses
- Test all data flows and transformations
- Test all error conditions and edge cases
- Test all permission/role combinations
- Test all business rule validations
- Leave NOTHING untested

**How to Ensure Exhaustive Coverage**:
1. Read requirement completely
2. Identify all user actions (happy path + alternatives)
3. Identify all system validations
4. Identify all business rules
5. Identify all error conditions
6. Identify all permission checks
7. Create test case for EACH distinct behavior
8. Map each TC to specific requirement clause

**Example: Upload File Requirement**

Requirement: "Admin can upload file to repository; File must be ≤10MB; Only specific file types allowed"

**Exhaustive test cases for this requirement**:
- TC_001: Admin uploads valid file (happy path)
- TC_002: Admin uploads file exactly 10MB (boundary)
- TC_003: Admin uploads file >10MB (rejection)
- TC_004: Admin uploads unsupported file type (rejection)
- TC_005: Admin uploads supported file type (acceptance)
- TC_006: Admin uploads file with special characters in name
- TC_007: Admin uploads duplicate filename (should overwrite or reject?)
- TC_008: Admin uploads file with corrupted content
- TC_009: Non-admin user attempts upload (permission denial)
- TC_010: Concurrent uploads from multiple admins
- TC_011: Upload with network interruption
- TC_012: Upload with disk space full
- TC_013: Verify file appears in list after upload
- TC_014: Verify file metadata stored correctly
- TC_015: Verify audit log records upload event

**Minimum Result**: 15+ test cases for single requirement (not 2-3)

---

#### Rule: UNIQUE TEST CASES ONLY (MANDATORY)

**Requirement**: NEVER create duplicate or redundant test cases.

**What This Means**:
- Each test case has UNIQUE preconditions
- Each test case has UNIQUE steps
- Each test case has UNIQUE expected result
- No two TCs testing identical behavior
- No copy-paste TCs with minor variable changes

**How to Ensure Uniqueness**:
1. Before creating new TC, search existing TCs for similar coverage
2. If similar TC exists → REUSE or SPLIT (don't duplicate)
3. If creating multiple TCs for same requirement → Ensure each tests DIFFERENT aspect

**Examples of DUPLICATES (DO NOT CREATE)**:
- ❌ TC_001: "Admin uploads file.txt" + TC_002: "Admin uploads document.docx" (both same behavior, just different filenames)
- ❌ TC_010: "User enters password" + TC_011: "User enters username" (same validation pattern)
- ❌ TC_050: "Save form succeeds" + TC_051: "Form saves successfully" (identical expected result)

**Examples of UNIQUE (CREATE THESE)**:
- ✅ TC_001: "Upload file succeeds" (happy path)
- ✅ TC_002: "Upload file >10MB rejected" (boundary violation)
- ✅ TC_003: "Upload unsupported file type rejected" (validation failure)
- ✅ TC_004: "Non-admin cannot upload" (permission denial)

---

#### Rule: ATOMIC TEST CASES ONLY (REITERATED & REINFORCED)

**Requirement**: Every test case tests EXACTLY ONE objective/behavior.

**What This Means**:
- One assertion per TC
- One requirement per TC
- One user action per TC
- One expected outcome per TC
- Split if testing multiple behaviors

**How to Ensure Atomicity**:
1. Define the SINGLE objective before writing TC
2. Stop after testing that objective
3. If additional behaviors → Create separate TCs
4. If unsure → Err on side of MORE TCs (atomic) vs FEWER TCs (bundled)

**Examples of NON-ATOMIC (SPLIT THESE)**:
- ❌ "User uploads file AND system saves to DB AND file appears in list AND audit log records event" → 4 TCs
- ❌ "Field validates required AND validates format AND validates length" → 3 TCs
- ❌ "Permission check passes AND role is assigned AND user sees menu AND data loads" → 4 TCs

**Examples of ATOMIC (GOOD)**:
- ✅ "User uploads valid file successfully" (one action, one outcome)
- ✅ "System saves file to database" (one action, one outcome)
- ✅ "File appears in user list after upload" (one action, one outcome)
- ✅ "Audit log records file upload event" (one action, one outcome)

---

#### Rule: REQUIREMENT ↔ TEST CASE TRACEABILITY (MANDATORY)

**Requirement**: Every test case MUST link back to requirement it tests.

**How to Ensure Traceability**:
1. Put requirement ID in TC Comments field
2. Format: "Validates FR-MODULE-001" or "Tests NFR-PERF-002"
3. Use exact requirement ID from specification
4. One or more requirements per TC allowed
5. NO orphan test cases without requirement link

**Example Traceability Links**:
- TC_001: Comments = "Validates FR-UPLOAD-001 (Admin can upload file)"
- TC_002: Comments = "Validates FR-UPLOAD-002, FR-VALIDATION-003 (File size limit)"
- TC_003: Comments = "Tests NFR-PERF-001 (Upload completes within 30 seconds)"

**Reverse Traceability Check**:
For each requirement in specification:
1. Search test case list for requirement ID in Comments
2. If NOT FOUND → Requirement has no test coverage → MISSING TC
3. If FOUND → Review TC to ensure it actually tests requirement

---

#### Rule: CLEAR & MEASURABLE EXPECTED RESULTS (MANDATORY)

**Requirement**: Every TC must have PRECISE, TESTABLE expected result.

**What This Means**:
- Expected result is NOT vague ("system works correctly")
- Expected result is SPECIFIC ("success message appears, file in list, DB updated")
- Expected result is MEASURABLE ("count increases by 1")
- Expected result is OBSERVABLE ("green success message with filename")
- Expected result is NOT assumed ("assume file is saved")

**Examples of VAGUE (REJECT THESE)**:
- ❌ "File uploads successfully"
- ❌ "System works correctly"
- ❌ "Data is validated"
- ❌ "User can access file"
- ❌ "Permission is checked"

**Examples of CLEAR & MEASURABLE (ACCEPT THESE)**:
- ✅ "Success message 'File uploaded: filename.txt' appears in green; File count increases from 5 to 6; DB record created with timestamp"
- ✅ "Error message 'File size exceeds 10MB limit' appears in red; Upload cancelled; File not added to list"
- ✅ "Upload time: 4.2 seconds (within 30-second SLA); File MD5 matches source"
- ✅ "Permission denied dialog appears; Upload button remains disabled; Audit log records 'Access denied for User_X'"

---

## Coverage Rules (COMPREHENSIVE CHECKLIST)

**For EVERY applicable requirement, generate test cases covering ALL of these scenarios:**

### Positive Scenarios (MANDATORY)
- ✅ Happy path with valid inputs
- ✅ Alternative happy paths (different but valid workflows)
- ✅ Minimum valid inputs (e.g., username = "a")
- ✅ Maximum valid inputs (e.g., username = 50 chars)
- ✅ Special character handling (é, ñ, emoji, etc.)
- ✅ Boundary values (1, 0, -1, null, empty, max_int)

### Negative Scenarios (MANDATORY)
- ✅ Invalid input (type mismatch, format error)
- ✅ Out-of-range values (negative, exceeds limit)
- ✅ Missing required fields
- ✅ SQL injection attempts
- ✅ XSS attack attempts
- ✅ Special characters that break parsing

### Boundary Value Analysis (MANDATORY)
- ✅ Minimum valid value (e.g., 1)
- ✅ Just below minimum (e.g., 0)
- ✅ Just above minimum (e.g., 2)
- ✅ Maximum valid value (e.g., 999)
- ✅ Just below maximum (e.g., 998)
- ✅ Just above maximum (e.g., 1000)

### Input Validation (MANDATORY)
- ✅ Field format validation (phone, email, date)
- ✅ Field length validation (min/max)
- ✅ Field type validation (string vs number)
- ✅ Required field validation
- ✅ Pattern matching validation (regex)
- ✅ Duplicate prevention validation

### Business Rule Validation (MANDATORY)
- ✅ Business logic constraints (e.g., committed ≤ available)
- ✅ Cross-field dependencies (e.g., if A then B required)
- ✅ State-based rules (e.g., can't delete if approved)
- ✅ Workflow rules (e.g., sequence must be followed)
- ✅ Time-based rules (e.g., past dates not allowed)

### Permission/Role-Based Scenarios (MANDATORY)
- ✅ Admin action (should succeed)
- ✅ User action (varies by role)
- ✅ Client action (limited permissions)
- ✅ Unauthorized user action (should fail)
- ✅ Guest/Anonymous action (should fail)
- ✅ Multiple role combinations
- ✅ Permission escalation attempts (should fail)

### Workflow Scenarios (MANDATORY)
- ✅ Normal workflow completion
- ✅ Workflow with delays
- ✅ Workflow interruption recovery
- ✅ Workflow branching (alternate paths)
- ✅ Workflow loops (if applicable)
- ✅ Concurrent workflow execution

### Alternate Flows (MANDATORY)
- ✅ Valid alternatives to happy path
- ✅ Different user roles with different outcomes
- ✅ Different business unit combinations
- ✅ Optional steps (if applicable)
- ✅ Skip steps (if allowed)

### Error Handling (MANDATORY)
- ✅ Database connection failure
- ✅ File system full
- ✅ Timeout/slow response
- ✅ Invalid state transition
- ✅ Resource not found (404)
- ✅ Unauthorized access (403)
- ✅ Server error (500)
- ✅ Network failure
- ✅ Retry logic (if applicable)

### Exception Scenarios (MANDATORY)
- ✅ Null pointer exceptions
- ✅ Array index out of bounds
- ✅ Type casting errors
- ✅ Division by zero
- ✅ Circular dependencies
- ✅ Deadlock conditions
- ✅ Memory exhaustion
- ✅ Stack overflow

### UI Verification (MANDATORY if UI feature)
- ✅ Element visibility (shown/hidden correctly)
- ✅ Element enablement (enabled/disabled correctly)
- ✅ Element values (displays correct data)
- ✅ Button functionality (click works)
- ✅ Form submission (submits correctly)
- ✅ Error messages (display correctly)
- ✅ Success messages (display correctly)
- ✅ Responsive design (mobile/tablet/desktop)

### Data Integrity Validation (MANDATORY)
- ✅ Create operation (data stored correctly)
- ✅ Read operation (data retrieved correctly)
- ✅ Update operation (data modified correctly)
- ✅ Delete operation (data removed correctly)
- ✅ Rollback operation (changes reverted)
- ✅ Data consistency (no orphans or duplicates)
- ✅ Data isolation (multi-user scenarios)

### Audit/Logging Validation (MANDATORY if applicable)
- ✅ Action logged (operation recorded)
- ✅ Timestamp correct (within acceptable range)
- ✅ User logged (who performed action)
- ✅ Action details logged (what was changed)
- ✅ Old value captured (if update)
- ✅ New value captured (if update)
- ✅ Log is immutable (cannot be tampered)

### Integration Scenarios (MANDATORY if applicable)
- ✅ Multi-step workflow across modules
- ✅ Data passed correctly between modules
- ✅ Dependencies resolved in correct order
- ✅ Rollback cascades correctly
- ✅ External API calls (if applicable)
- ✅ Event handling/callbacks
- ✅ Concurrent operations across modules

### State Transition Scenarios (MANDATORY if stateful)
- ✅ Valid state transition (allowed)
- ✅ Invalid state transition (rejected)
- ✅ Skip state transition (if allowed)
- ✅ Circular transitions (if applicable)
- ✅ Concurrent state changes (if multi-user)
- ✅ State persistence (after reload)

### Regression Scenarios (MANDATORY if feature impacts existing)
- ✅ New feature doesn't break existing feature A
- ✅ New feature doesn't break existing feature B
- ✅ New feature doesn't break existing feature C
- ✅ Existing workflows still work
- ✅ Existing permissions still enforced
- ✅ Existing data migration works

---

## QA Heuristics (THOUGHT PROCESS BEFORE GENERATING TCs)

**Ask these questions BEFORE creating test cases:**

### Risk Analysis Heuristics
- **What can go wrong?**
  - Data corruption
  - Unauthorized access
  - Performance degradation
  - Loss of data
  - System crash
  - User confusion

- **Who can perform this action?**
  - Admin (should succeed)
  - User (depends on role)
  - Client (limited access)
  - Guest (should fail)
  - Unauthorized (should fail)

- **Who should be prevented?**
  - Users without permission
  - Users with expired credentials
  - Deleted users
  - Suspended users
  - Cross-tenant users

- **What validations exist?**
  - Input validation (format, length, type)
  - Business rule validation
  - Permission validation
  - State validation
  - Dependency validation

- **What business rules exist?**
  - Workflow rules (sequence)
  - State rules (valid transitions)
  - Constraint rules (limits)
  - Relationship rules (dependencies)
  - Time rules (deadlines)

### Outcome Heuristics
- **What happens after success?**
  - Data stored
  - User notified
  - Workflow advances
  - Next step enabled
  - Audit log updated
  - Email sent (if applicable)

- **What happens after failure?**
  - Error message shown
  - Data NOT stored
  - Workflow NOT advanced
  - User retries
  - Support notified (critical errors)
  - Failure logged

- **What happens with invalid input?**
  - Validation fails
  - Error message shown
  - Field highlighted
  - Suggestion provided
  - Form not submitted
  - Previous data retained

- **What happens with duplicate data?**
  - Duplicate rejected (most common)
  - Duplicate merged
  - Duplicate warned (allow override)
  - Duplicate version created
  - Duplicates listed for user selection

### Notification & Logging Heuristics
- **Are there notifications?**
  - Success message
  - Error message
  - Warning message
  - Confirmation dialog
  - Email notification
  - In-app notification
  - SMS notification (if applicable)

- **Is logging required?**
  - Action logged (what)
  - User logged (who)
  - Timestamp logged (when)
  - Changes logged (old → new)
  - Reason logged (why, if applicable)
  - Result logged (success/failure)

- **Are permissions enforced?**
  - Role checked
  - Action checked
  - Resource checked
  - Time-based check (if applicable)
  - Multi-factor check (if applicable)

- **Are there UI changes?**
  - Menu item shown/hidden
  - Button enabled/disabled
  - Field shown/hidden
  - Data refreshed
  - Status updated
  - Color changed (success/error)

---

## Quality Rules (MINIMUM STANDARDS)

**Every test case MUST meet these quality standards:**

### Rule 1: NO GENERIC PLACEHOLDER TEST CASES (MANDATORY)
- ❌ REJECT: "Test the feature"
- ❌ REJECT: "Verify it works"
- ❌ REJECT: "Check functionality"
- ❌ REJECT: "Test happy path"
- ❌ REJECT: "Test error handling"

- ✅ ACCEPT: "Verify admin can upload file ≤10MB with valid extension"
- ✅ ACCEPT: "Verify system rejects upload >10MB with error message 'File exceeds limit'"
- ✅ ACCEPT: "Verify non-admin user receives 'Permission Denied' message"
- ✅ ACCEPT: "Verify file appears in user list within 5 seconds of upload completion"

### Rule 2: NO UNNECESSARY DUPLICATION (MANDATORY)
- ❌ REJECT: Identical preconditions across multiple TCs (reuse or split)
- ❌ REJECT: Identical expected results across multiple TCs (combine or differentiate)
- ❌ REJECT: Copy-paste TCs with only variable names changed

- ✅ ACCEPT: Each TC has unique precondition OR unique step OR unique expected result
- ✅ ACCEPT: Variation serves testing purpose (boundary, alternate role, error condition)

### Rule 3: MEANINGFUL TEST CASE TITLES (MANDATORY)
- ❌ REJECT: "Test 1", "Test 2", "Verify functionality"
- ❌ REJECT: "Upload", "Delete", "Search"
- ❌ REJECT: "Happy path", "Negative test"

- ✅ ACCEPT: "Admin uploads 9.9MB file with .pdf extension successfully"
- ✅ ACCEPT: "System rejects 10.1MB file with error message 'File too large'"
- ✅ ACCEPT: "Non-admin user receives 403 Permission Denied when attempting upload"
- ✅ ACCEPT: "Verify file metadata (name, size, type, timestamp) correct after upload"

**Format for meaningful titles:**
`[Role] [Action] [Condition] [Expected Result]`
- Example: "Admin uploads file with special characters in filename successfully"
- Example: "Client attempts download of file uploaded by different client; access denied"

### Rule 4: HIGHLIGHT AMBIGUOUS REQUIREMENTS (MANDATORY)
- ❌ DO NOT: Assume behavior for ambiguous requirements
- ❌ DO NOT: Fill gaps with made-up logic
- ❌ DO NOT: Guess at business rules

- ✅ DO: Document ambiguity in test case Comments
- ✅ DO: Create test case based on reasonable interpretation
- ✅ DO: Flag ambiguity for clarification

**Example Ambiguous Requirement**: "System must be responsive"
- Unclear: What breakpoints? 320px? 1920px?
- Unclear: What is "responsive"? Layout change? Content scale?
- Unclear: Which browsers? Chrome only? All major?

**How to Handle**:
```
TC_ABC_001: Verify page layout adapts to 320px mobile screen
Comments: "Interprets 'responsive' as layout change for mobile. 
Clarification needed: What are minimum/maximum breakpoints?"

TC_ABC_002: Verify all images scale proportionally on tablet (768px)
Comments: "Assumes 'responsive' includes image scaling. 
Clarification needed: Is image cropping acceptable?"
```

**This prevents**:
- Misaligned test cases and implementation
- Repeated failures due to unclear requirements
- Wasted test effort on wrong assumptions

---

**Result**: Comprehensive, meaningful, quality test case generation with clear traceability and measurable results.