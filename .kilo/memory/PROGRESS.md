# Progress Tracker

## Current Sprint: Foundation

### Completed
- [x] Project setup and structure
- [x] Competition SDK downloaded and extracted
- [x] Basic attack algorithm stub (`src/attack.py`)
- [x] Utility functions (`src/utils.py`)
- [x] Memory bank implementation (`src/memory/`)
- [x] LanceDB + sentence-transformers integration
- [x] Test suite for memory bank (`tests/test_memory.py`)
- [x] Configuration system (`configs/default.json`)
- [x] Kilo persistent memory system (AGENTS.md + .kilo/)

### In Progress
- [ ] SDK integration (replace placeholder classes)
- [ ] First working attack strategy

### Blocked
- Competition data download (needs Kaggle credentials)

## Next Steps

1. **Install competition SDK** and replace placeholder classes
2. **Implement basic prompt fuzzing** strategy
3. **Test against local sandbox** if available
4. **Iterate on prompt templates** based on results
5. **Add evolutionary algorithm** for prompt optimization

## Lessons Learned

- LanceDB needs `pylance` package for `to_pandas()` operations
- sentence-transformers downloads models on first use (~100MB)
- Memory bank dedup works via tool call signatures, not prompt text
- Competition uses `AttackRunConfig` with `time_budget_s` and `max_steps`

## Metrics

| Metric | Value |
|--------|-------|
| Memory entries stored | 0 (fresh) |
| Successful attacks found | 0 |
| Unique signatures | 0 |
| Test coverage | Memory bank only |
