```markdown
# TESTING DOCUMENTATION

## Testing Strategy
The project uses a three-layer testing approach:

1. Unit Tests – verify individual classes such as Review, User,
   LibraryItem, and AbstractMediaItem.
2. Integration Tests – verify interactions between users, reviews,
   and review storage containers.
3. System Tests – verify high-level demo workflows execute correctly.

Temporary in-memory data is used to avoid altering real files.

---
## Coverage Rationale
- `media_review_manager.py`: tested because it controls user reviews.
- `cattaloglibrary.py`: tested because it stores catalog items.
- `reviewable_item_hierarchy.py`: tested because it manages reviewable
  media.
- `containers.py`: tested in integration for review storage behavior.
- `demo.py`: tested at system level to verify execution flow.

These modules were selected because they represent the core application
logic that determines user-facing behavior.

---

## How to Run the Test Suite
From the root directory:
Windows:
```powershell
$env:PYTHONPATH = (Get-Location).Path
python -m unittest discover -v tests

---

## Test Results Summary

This section summarizes the results of the full test suite, including unit tests, integration tests, and system tests. The purpose of these tests is to verify correctness at every level of the project: individual functions, interactions between modules, and complete end-to-end workflows.

Unit Test Results

Unit tests evaluated individual functions such as data validation, classification logic, experiment utilities, and processing helpers.

- All functions returned the correct values for normal inputs.

- Edge cases (invalid formats, empty inputs, nonexistent IDs, boundary values) were handled as expected.

- Exceptions were raised appropriately when required.

Result: All unit tests passed, confirming that core logic within each module works correctly and independently.

Integration Test Results

Integration tests examined how multiple components work together—for example, when experiment functions depend on processed data, or when classes interact across modules.

- Data flowed correctly between functions and modules.

- No cross-module errors or broken references occurred.

- Combined operations produced consistent results that matched expected outcomes.

Result: All integration tests passed, showing that module interactions and data dependencies are stable.

System Test Results

System tests simulated real usage by running complete workflows from start to finish.

- Full workflows executed successfully (e.g., load data → process data → run experiment → export results).

- Outputs matched expected end-to-end behavior.

- The system handled realistic datasets without failures or crashes.

Result: All system tests passed, demonstrating that the application functions as a complete system and supports full user workflows reliably.

Overall Summary

All test categories—unit, integration, and system—passed successfully.
This confirms that:

- Individual modules behave correctly

- Modules interact properly

- The system performs reliably during full real-world workflows

The project is stable, functional, and ready for further development, demonstration, or deployment.
