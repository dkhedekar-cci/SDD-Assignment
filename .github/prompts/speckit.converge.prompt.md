---
agent: speckit.converge
---
# Purpose

Analyze the generated specification and test artifacts to determine the completeness of test coverage.

# Input
spec.md
testcases.md
traceability.md (if available)
Acceptance Criteria
Business Rules

# Output

Generate coverage.md

# Responsibilities

The AI should:

Requirement Coverage
Verify every requirement has one or more test cases.
Highlight uncovered requirements.
Identify duplicate coverage.
Business Rule Coverage
Verify every business rule is tested.
Identify missing validations.
Acceptance Criteria Coverage
Ensure each acceptance criterion has corresponding test cases.
Validation Coverage

Check coverage for:

Mandatory fields
Optional fields
Invalid input
Boundary values
Duplicate values
Format validation
UI Coverage

Verify tests exist for:

Navigation
Buttons
Messages
Layout
Responsive behavior
Accessibility (where applicable)
Permission Coverage

Confirm each role has tests for:

View
Create
Edit
Delete
Restricted actions
Error Handling Coverage

Ensure tests cover:

Validation errors
System errors
Network failures (where applicable)
Unauthorized access
Edge Case Coverage

Verify tests exist for:

Empty input
Maximum values
Minimum values
Null values
Special characters
Duplicate data
Concurrent actions
Session timeout
Test Type Coverage

Summarize coverage across:

Functional
Negative
Boundary
Regression
Smoke
Integration
End-to-End (if applicable)
Coverage Summary

Provide a summary table like:

Category	Covered	Missing	Coverage
Requirements	24	0	100%
Business Rules	18	2	90%
Acceptance Criteria	12	0	100%
Validation Rules	15	1	94%
Permissions	8	0	100%
Edge Cases	20	3	87%
Overall Assessment

Assign an overall coverage rating, for example:

Excellent (95–100%)
Good (85–94%)
Fair (70–84%)
Needs Improvement (<70%)

List all uncovered areas and recommend additional test cases before sign-off.