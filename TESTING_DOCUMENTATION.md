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
