import os

# Files to DELETE (unwanted/redundant)
delete_files = [
    # Old Python scripts
    'analyze_excel.py', 'check_sheets.py', 'convert_to_excel.py',
    'extract_reference.py', 'final_export_all_tc.py', 'final_summary.py',
    'generate_complete_excel.py', 'generate_excel.py', 'generate_excel_full.py',
    'generate_test_cases_excel.py', 'read_reference.py', 'regenerate_testcases_v3.py',
    'sync_markdown_to_excel.py', 'sync_testcases.py', 'verify_excel.py',
    'verify_rtm_sync.py', 'sync-testcases.bat',
    
    # Old test case files
    'Testcases-reference.xlsx', 'testcases.md', 'testcases_template.md',
    'testcases_v1.0_original_archive.md',
    
    # Old v3.0 docs
    'FINAL_STATUS_REPORT_v3.0.md', 'QUICK_REFERENCE_v3.0.md',
    'IMPLEMENTATION_GUIDE_v3.0.md', 'INDEX_AND_NAVIGATION_v3.0.md',
    'TESTCASE_REGENERATION_SUMMARY_v3.0.md',
    
    # Old guides and checklists
    'clarifications.md', 'FUTURE-PROOF-SYNC.md', 'QA-CONSTITUTION-001-EXPORT-VERIFICATION.md',
    'QUICK-START-SYNC.md', 'SYNC-GUIDE.md', 'SYNC-PREVENTION-CHECKLIST.md', 'SYNC-CHECKLIST.md',
    'implementation.md', 'requirements.md', 'spec-review.md', 'tasks.md', 'testplan.md',
    'RTM-DOCUMENTATION.md', 'TEST-CASES-EXPORT-COMPLETE.md', 'TEST-CASES-EXPORT-SUMMARY.md',
    
    # Analysis and old summary docs
    'ANALYSIS_DOCUMENTS_INDEX.md', 'ANSWER_WHY_RULES_VIOLATED.md',
    'ROOT_CAUSE_ANALYSIS_WHY_RULES_VIOLATED.md', 'PREVENTIVE_ACTION_PLAN.md',
    'PROJECT_COMPLETION_BANNER.md', 'QUALITY_REGENERATION_COMPLETION_SUMMARY_v4.0.md',
    'QUALITY_ASSURANCE_REPORT_v4.0.md', 'EXECUTIVE_SUMMARY_v4.0.md', 'FINAL_SUMMARY_v4.0.md',
    'TEST_CASE_QUALITY_REGENERATION_DOCUMENTATION_INDEX.md', 'ISSUE-RESOLUTION-FINAL-REPORT.md',
    'VISUAL_EXPLANATION.md', 'VISUAL_COMPARISON_42_vs_109.md', 'CLARIFICATION_WHY_42_TESTCASES.md',
    'SYNCHRONIZATION-REPORT.md', 'SYNC-VERIFICATION-v4.0.md', '00_START_HERE_EXECUTIVE_SUMMARY.md'
]

deleted = 0
for file in delete_files:
    if os.path.exists(file):
        try:
            os.remove(file)
            print(f"✅ Deleted: {file}")
            deleted += 1
        except Exception as e:
            print(f"❌ Error deleting {file}: {e}")

print(f"\n✅ Total files deleted: {deleted}")
