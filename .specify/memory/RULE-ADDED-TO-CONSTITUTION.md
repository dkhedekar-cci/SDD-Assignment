# ✅ File Synchronization Rule Added to Constitution

## Correct Hierarchy

### Level 1: PROJECT-WIDE CONSTITUTION (Authority)
**File**: `.specify/memory/constitution.md`
**New Section**: VI. Test Case File Synchronization (MANDATORY)
**Scope**: Applies to ALL features (011, 012, 013, etc.)

**What's in Constitution Section VI**:
- Rule Summary (3 file formats must sync)
- Count Verification Procedure
- Data Verification Requirements
- Failure Handling Protocol
- Sync Workflow (7 mandatory steps)
- Anti-Patterns (DO NOT DO)
- Documentation Requirements
- Example: Feature 011 (217 TCs verified)
- Tools & Scripts Reference

---

### Level 2: FEATURE-SPECIFIC IMPLEMENTATION (Details)
**File**: `specifications/011-central-repo/implementation.md`
**References**: Constitution.md Section VI
**Scope**: Central Repository Feature Only

**What's in implementation.md**:
- Specific commands for Feature 011
- Example: `grep -c "^#### TC_CENTRAL_"`
- Production scripts available
- Feature 011 current status (217 TCs verified)
- Quick reference checklist

---

## Why This Structure is Correct

| Aspect | Constitution.md | Implementation.md |
|--------|-----------------|-------------------|
| **Scope** | ALL features | Feature 011 only |
| **Authority** | Global standard | Feature-specific detail |
| **When** | Every test case export | Before testing 011 |
| **Who** | All QA teams | QA team for 011 |
| **Purpose** | Define the RULE | Implement the rule |

---

## What Was Added to Constitution

**Section VI. Test Case File Synchronization (MANDATORY)**

**Key Rule**: Markdown, Excel, and RTM files MUST have EXACTLY the same test case counts and data.

### Rule Details

1. **Count Verification** (MANDATORY at every export)
   - Get markdown count
   - Get Excel count (rows minus header)
   - **MUST BE IDENTICAL**
   - If not equal → DO NOT PROCEED

2. **Data Verification** (MANDATORY)
   - Every TC ID in markdown must exist in Excel
   - Every TC in Excel must have corresponding markdown
   - All details must match across formats
   - RTM must have ≥80% coverage

3. **Failure Handling** (MANDATORY)
   - IF count mismatch → STOP
   - Delete incomplete file
   - Regenerate from primary source (Excel)
   - Use programmatic scripts (NOT manual)
   - Re-run verification

4. **Sync Workflow** (MANDATORY for all regenerations)
   - Step 1: Generate/update Excel
   - Step 2: Verify Excel count
   - Step 3: Run sync script → regenerate markdown
   - Step 4: Verify markdown count matches Excel
   - Step 5: Regenerate RTM
   - Step 6: Run comprehensive verification
   - Step 7: Update version log

5. **Anti-Patterns** (VIOLATIONS - DO NOT DO)
   - ❌ Never accept markdown count ≠ Excel count
   - ❌ Never manually edit instead of sync scripts
   - ❌ Never deploy partial/incomplete TCs
   - ❌ Never skip verification step
   - ❌ Never use regex extraction for production
   - ❌ Never leave files out-of-sync

6. **Documentation** (MANDATORY)
   - Update version log every time files sync
   - Record: Timestamp, counts, verification status
   - Example: `2026-07-10 | 217 TCs | Excel: 217 | MD: 217 | RTM: 85 | Status: ✅`
   - DO NOT proceed with test execution until verified

---

## Current Status for Feature 011

| Metric | Value | Status |
|--------|-------|--------|
| Markdown Test Cases | 217 | ✅ |
| Excel Test Cases | 217 | ✅ |
| RTM Mappings | 85 | ✅ |
| Sync Status | PERFECTLY SYNCHRONIZED | ✅ |
| Constitution Status | Rule VI ACTIVE | ✅ |

---

## Next Steps

✅ **For Future Features** (012, 013, etc.):
- Follow Constitution Rule VI for test case file sync
- Reference `specifications/[feature]/implementation.md` for feature-specific commands
- Run verification scripts before test execution
- Document all sync activities in version log

✅ **For Current Feature (011)**:
- All files synced and verified
- Ready for test execution
- Continue documenting sync status in TEST_CASES_VERSION_LOG.md

---

**Result**: Single source of truth. Rule is in the right place (Constitution). All future features will follow the same synchronization procedure.
