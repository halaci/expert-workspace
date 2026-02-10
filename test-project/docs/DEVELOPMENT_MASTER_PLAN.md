# Development Master Plan - Calculator Project

## Projekt: Python Calculator Modul

**Verzió:** 1.0  
**Státusz:** In Progress

---

## 1. Projekt Vízió

Egy egyszerű, de robusztus Python calculator modul fejlesztése, amely:
- Alapvető matematikai műveleteket támogat
- Megfelelő hibakezelést tartalmaz
- Jól tesztelt és dokumentált

---

## 2. Fázisok

### Phase 1: Alapműveletek ✅
**Státusz:** DONE

**Scope:**
- add(a, b) - összeadás
- subtract(a, b) - kivonás

### Phase 2: Bővített Műveletek 🔄
**Státusz:** IN PROGRESS

**Scope:**
- multiply(a, b) - szorzás
- divide(a, b) - osztás (hibakezelés!)

### Phase 3: Haladó Funkciók
**Státusz:** PLANNED

**Scope:**
- power(base, exp) - hatványozás
- sqrt(n) - négyzetgyök
- modulo(a, b) - maradékos osztás

---

## 3. Architektúra

```
test-project/
├── src/
│   └── calculator.py    # Fő modul
├── tests/
│   └── test_calculator.py
└── docs/
    ├── DEVELOPMENT_MASTER_PLAN.md
    ├── SPRINT_BACKLOG.md
    ├── USER_STORIES.md
    └── DEFINITION_OF_DONE.md
```

---

## 4. Minőségi Követelmények

- Teszt coverage: >= 80%
- Minden publikus függvény dokumentált
- Type hints használata
- Megfelelő error handling

---

*Calculator Development Master Plan v1.0*
