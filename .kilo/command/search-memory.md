---
description: Search memory bank for similar attacks
---
Search the memory bank for attacks similar to the query:

Use the MemoryBank class to search:
```python
from src.memory.bank import MemoryBank
bank = MemoryBank(db_path="./memory_db")
results = bank.search("$ARGUMENTS", limit=10)
for r in results:
    print(f"[{r['severity_score']}] {r['prompt'][:60]}...")
    print(f"    Predicates: {r['predicates_triggered']}")
    print(f"    Tools: {[t['tool'] for t in r['tool_calls']]}")
```

Run this with: `source .venv/bin/activate && python -c "..."` 
