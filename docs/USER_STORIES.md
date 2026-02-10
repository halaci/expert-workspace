# User Stories

---

## US-001: Developer Agent Instrukciók

**Mint** projekt menedzser  
**Szeretném** ha a fejlesztő agent részletes instrukciókat kapna  
**Hogy** konzisztensen tudjon dolgozni és validálható deliverable-eket tudjon előállítani

### Acceptance Criteria

- **AC-1:** Workspace struktúra egyértelműen definiálva
- **AC-2:** Fejlesztési workflow lépésről lépésre dokumentálva
- **AC-3:** Commit message formátum specifikálva (type, scope, body)
- **AC-4:** Validátorral való kommunikáció sablonjai elérhetők

### Prioritás
HIGH

### Story Points
5

---

## US-002: Validator Agent Instrukciók

**Mint** projekt menedzser  
**Szeretném** ha a validátor agent részletes instrukciókat kapna  
**Hogy** objektíven és konzisztensen tudja ellenőrizni a fejlesztéseket

### Acceptance Criteria

- **AC-1:** Cold-start protokoll (üres kontextusból indulás) definiálva
- **AC-2:** Validációs checklist minden kategóriára megvan
- **AC-3:** Hiba súlyossági szintek (CRITICAL/MAJOR/MINOR/INFO) definiálva
- **AC-4:** Validation report sablon elkészült

### Prioritás
HIGH

### Story Points
5

---

## US-003: GIT Diff Előkészítő Script

**Mint** fejlesztő agent  
**Szeretném** ha automatikusan generálódna a validáláshoz szükséges diff  
**Hogy** ne kelljen manuálisan összeszednem az információkat

### Acceptance Criteria

- **AC-1:** PowerShell script futtatható (prepare_validation.ps1)
- **AC-2:** Diff markdown formátumban generálódik
- **AC-3:** Commit információk (hash, szerző, üzenet) megjelennek
- **AC-4:** Módosított fájlok listázva státusszal (added/modified/deleted)
- **AC-5:** Korábbi diff automatikusan archiválódik

### Prioritás
HIGH

### Story Points
3

---

## US-004: Use Cases és Tesztelési Dokumentáció

**Mint** projekt menedzser  
**Szeretném** ha dokumentálva lennének a használati esetek és tesztek  
**Hogy** ellenőrizni tudjam a protokoll megfelelő működését

### Acceptance Criteria

- **AC-1:** Minimum 5 use case dokumentálva (sikeres, rework, rejected, stb.)
- **AC-2:** Script tesztelési szcenáriók definiálva
- **AC-3:** End-to-end tesztek leírva

### Prioritás
MEDIUM

### Story Points
3

---

## US-005: Minta Workspace

**Mint** tesztelő  
**Szeretném** ha lenne egy működő minta workspace  
**Hogy** kipróbálhassam a protokollt valós körülmények között

### Acceptance Criteria

- **AC-1:** docs/ mappa a szükséges dokumentumokkal
- **AC-2:** .validation/ mappa struktúra létrehozva
- **AC-3:** Minta diff generálva teszteléshez

### Prioritás
MEDIUM

### Story Points
2

---

*User Stories v1.0*
