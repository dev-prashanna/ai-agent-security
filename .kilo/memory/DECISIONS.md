# Architecture Decisions

## 2026-06-25: Memory Bank Implementation

**Decision:** Use LanceDB + sentence-transformers for attack trace storage

**Rationale:**
- LanceDB is embedded (no Docker/server needed for Kaggle)
- sentence-transformers provides local embeddings (no API calls)
- Supports semantic search over past attacks
- Enables deduplication via trace signatures

**Alternatives Considered:**
- Qdrant: Requires server, overkill for single-user competition
- SQLite: No semantic search capability
- FAISS: Less Pythonic, harder to integrate

**Status:** Implemented in `src/memory/`

---

## 2026-06-25: Attack Algorithm Structure

**Decision:** Single `AttackAlgorithm` class with memory bank integration

**Rationale:**
- Competition requires `AttackAlgorithmBase` inheritance
- Memory bank provides deduplication and success tracking
- Snapshot/restore enables state-space exploration

**Status:** Stub implemented in `src/attack.py`

---

## 2026-06-25: Configuration Strategy

**Decision:** JSON config files in `configs/` directory

**Rationale:**
- Easy to iterate on parameters without code changes
- Can version different strategies separately
- Competition SDK may support config injection

**Status:** `configs/default.json` created

---

## Pending Decisions

- [ ] Which attack strategy to prioritize (fuzzing vs evolutionary vs hybrid)
- [ ] Whether to use LLM-assisted prompt generation
- [ ] How to handle the 9,000 second time budget efficiently
- [ ] Memory bank schema — currently stores raw tool calls, may need refinement
