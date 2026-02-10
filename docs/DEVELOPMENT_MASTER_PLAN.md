# Development Master Plan

## Projekt: Diff Validator AI PoC

**Verzió:** 1.0  
**Kezdés:** 2026-02-01  
**Státusz:** In Progress

---

## 1. Projekt Vízió

Egy GIT diff alapú validációs rendszer, ahol két AI agent együttműködik:
- **Developer Agent:** Implementál, commitol, dokumentál
- **Validator Agent:** Ellenőrzi a változtatásokat a projekt célok alapján

**Végcél:** Objektív, automatizált fejlesztési előrehaladás ellenőrzés.

---

## 2. Fázisok

### Phase 1: Protokoll Kialakítás ✅
**Időtartam:** 1 hét  
**Státusz:** DONE

**Deliverables:**
- [x] A2A Protocol Specification
- [x] Agent Instructions (Developer)
- [x] Agent Instructions (Validator)
- [x] System Prompt Addendum
- [x] Diff készítő script
- [x] Use Cases dokumentáció

### Phase 2: Proof of Concept 🔄
**Időtartam:** 2 hét  
**Státusz:** IN PROGRESS

**Deliverables:**
- [ ] Minta workspace felállítása
- [ ] Developer-Validator ciklus tesztelése
- [ ] Iteráció a protokollon
- [ ] Dokumentáció finomítás

### Phase 3: A2A Integráció
**Időtartam:** 2 hét  
**Státusz:** PLANNED

**Deliverables:**
- [ ] A2A protokoll integráció
- [ ] Agent orchestration
- [ ] Automatizált workflow

---

## 3. Architektúra

```
┌─────────────────────────────────────────────────────────────┐
│                     GIT REPOSITORY                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │   docs/     │  │    src/     │  │   .validation/      │ │
│  │  - PLAN.md  │  │  - code     │  │  - current_diff.md  │ │
│  │  - SPRINT   │  │  - tests    │  │  - reports          │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
         │                                      ▲
         │ commit                               │ read
         ▼                                      │
┌─────────────────┐    A2A messages    ┌─────────────────┐
│ Developer Agent │◄──────────────────►│ Validator Agent │
│                 │                    │                 │
│ - Implements    │                    │ - Validates     │
│ - Documents     │                    │ - Reports       │
│ - Commits       │                    │ - Approves      │
└─────────────────┘                    └─────────────────┘
```

---

## 4. Sikerkritériumok

| Kritérium | Mérték | Célérték |
|-----------|--------|----------|
| Protokoll teljessége | Dokumentumok száma | 6 db |
| Cold-start képesség | Validátor sikeres indulás üres kontextusból | 100% |
| Validáció minőség | False positive rate | < 10% |
| Ciklus idő | Validáció idő | < 5 perc |

---

## 5. Kockázatok

| Kockázat | Valószínűség | Hatás | Mitigáció |
|----------|--------------|-------|-----------|
| LLM context limit | Közepes | Magas | Tömör dokumentumok |
| Félreértés a protokollban | Alacsony | Közepes | Részletes spec |
| Performance | Közepes | Közepes | Optimalizálás |

---

*Development Master Plan v1.0*
