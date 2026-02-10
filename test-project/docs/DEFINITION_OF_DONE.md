# Definition of Done (DoD) - Calculator

## Általános DoD Kritériumok

### 1. Kód Minőség
- [ ] A kód szintaktikailag helyes (python -m py_compile sikeres)
- [ ] Nincs TODO/FIXME a commit-olt kódban
- [ ] Nincsenek placeholder/stub implementációk
- [ ] Nincsenek hardcoded teszt válaszok
- [ ] Edge case-ek kezelve vannak

### 2. Teszt Követelmények
- [ ] Unit tesztek írva és futnak
- [ ] Minden Acceptance Criteria le van tesztelve
- [ ] Teszt coverage > 80%
- [ ] Nincsenek skip-pelt tesztek indoklás nélkül
- [ ] Nincsenek `assert True` vagy üres tesztek

### 3. Dokumentáció
- [ ] Docstring minden publikus metódushoz
- [ ] CHANGELOG frissítve
- [ ] README frissítve (ha szükséges)

### 4. Error Handling
- [ ] Hibák megfelelően kezelve (nem üres except blokk)
- [ ] Értelmes hibaüzenetek
- [ ] Input validáció működik

---

## Sprint 2 Specifikus DoD

### TASK-001: Szorzás implementálása
- [ ] multiply() függvény működik
- [ ] Negatív számok kezelése
- [ ] Float számok kezelése
- [ ] Nullával szorzás működik
- [ ] Unit tesztek készek

### TASK-002: Osztás implementálása
- [ ] divide() függvény működik
- [ ] Negatív számok kezelése
- [ ] Float eredmény kezelése
- [ ] Nullával osztás → ValueError
- [ ] Unit tesztek készek

---

*Definition of Done v1.0*
