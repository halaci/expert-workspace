# User Stories - Calculator

---

## US-001: Összeadás ✅

**Mint** felhasználó  
**Szeretném** két számot összeadni  
**Hogy** megkapjam az összegüket

### Acceptance Criteria
- **AC-1:** add(2, 3) == 5
- **AC-2:** add(-1, 1) == 0
- **AC-3:** add(1.5, 2.5) == 4.0

---

## US-002: Kivonás ✅

**Mint** felhasználó  
**Szeretném** két számot kivonni  
**Hogy** megkapjam a különbségüket

### Acceptance Criteria
- **AC-1:** subtract(5, 3) == 2
- **AC-2:** subtract(1, 5) == -4
- **AC-3:** subtract(2.5, 1.5) == 1.0

---

## US-003: Szorzás 🔄

**Mint** felhasználó  
**Szeretném** két számot összeszorozni  
**Hogy** megkapjam a szorzatukat

### Acceptance Criteria
- **AC-1:** multiply(2, 3) == 6
- **AC-2:** multiply(-2, 3) == -6
- **AC-3:** multiply(2.5, 4) == 10.0
- **AC-4:** multiply(0, 100) == 0

---

## US-004: Osztás 🔄

**Mint** felhasználó  
**Szeretném** két számot elosztani  
**Hogy** megkapjam a hányadosukat

### Acceptance Criteria
- **AC-1:** divide(6, 2) == 3
- **AC-2:** divide(7, 2) == 3.5
- **AC-3:** divide(-6, 2) == -3
- **AC-4:** divide(5, 0) → ValueError("Division by zero")

---

*User Stories v1.0*
