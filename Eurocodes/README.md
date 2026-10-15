# 🏛️ pamd_eurocodes

[![PyPI version](https://img.shields.io/pypi/v/pamd_eurocodes.svg)](https://pypi.org/project/pamd_eurocodes/)
[![Python versions](https://img.shields.io/pypi/pyversions/pamd_eurocodes.svg)](https://pypi.org/project/pamd_eurocodes/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **European Structural Design Standards (Eurocodes EN 1990 – EN 1999) ported into a structured, programmatic Python library.**

`pamd_eurocodes` is part of **The Catalogue** engineering ecosystem. It brings official Eurocode design parameters, characteristic load tables, safety factors, material classes, symbols, and standard definitions directly into your Python scripts and structural calculation pipelines.

No more manual lookups across thousands of pages of standard documents — access standard values programmatically, perform calculations with recommended defaults, and even export design tables directly to AutoCAD DXF drawings.

---

## 🚀 Key Features

- **Comprehensive Eurocode Suite (EN 1990 – EN 1999):** Complete breakdown from Eurocode 0 (Basis of design) to Eurocode 9 (Aluminium).
- **Structured Standard Tables (`Table`):** Access design tables with headers, values, captions, and notes. Built-in Markdown representation and querying support.
- **AutoCAD DXF Export (`toDXF`):** Export standard tables directly into AutoCAD drawing format (.dxf) for direct embedding into engineering drawings.
- **Bounded Range Support (`BRange`):** Eurocode parameters often specify a range with a recommended standard value (allowing National Annex adjustments). `BRange` captures min, max, and default values while allowing direct arithmetic operations using the default value.
- **LaTeX Math Symbols (`Symbol`):** Formatted LaTeX symbols and official definitions for programmatic reporting and Jupyter notebook rendering.
- **Terms & Definitions (`TAD`):** Official definitions referenced throughout each Eurocode standard.

---

## 📦 Installation

Install `pamd_eurocodes` via pip:

```bash
pip install pamd_eurocodes
```

Or install locally from source:

```bash
git clone https://github.com/Abstergo2003/PyAct.git
cd PyAct/Eurocodes
pip install .
```

*Optional dependency for DXF generation:*
```bash
pip install ezdxf
```

---

## 📚 Eurocodes Covered

| Code | Standard | Scope / Description | Sub-parts |
|:-----|:---------|:--------------------|:----------|
| **Eurocode 0** | EN 1990 | Basis of structural design | Symbols, Design working life, $\psi$ factors, Combination values |
| **Eurocode 1** | EN 1991 | Actions on structures | Densities, self-weight, imposed loads (1-1), Fire (1-2), Snow (1-3), Wind (1-4), Thermal (1-5), Execution (1-6), Accidental (1-7), Traffic (2), Cranes/machinery (3), Silos/tanks (4) |
| **Eurocode 2** | EN 1992 | Design of concrete structures | General rules & buildings (1-1), Fire (1-2), Lightweight aggregate (1-4), Unreinforced concrete (1-6), Bridges (2), Retaining & containment (3) |
| **Eurocode 3** | EN 1993 | Design of steel structures | General rules (1-1), Fire (1-2), Cold-formed (1-3), Plated elements (1-5), Joints (1-8), Fatigue (1-9), Toughness (1-10), Towers/masts/chimneys (3) |
| **Eurocode 4** | EN 1994 | Composite steel & concrete structures | General rules & buildings (1-1), Fire (1-2), Bridges (2) |
| **Eurocode 5** | EN 1995 | Design of timber structures | Common rules & buildings (1-1), Fire (1-2), Bridges (2) |
| **Eurocode 6** | EN 1996 | Design of masonry structures | Common rules for reinforced & unreinforced (1-1), Fire (1-2), Lateral load (1-3), Simplified calculation (2), Simplified methods (3) |
| **Eurocode 7** | EN 1997 | Geotechnical design | General rules (1), Ground investigation and testing (2), Additional design rules (3) |
| **Eurocode 8** | EN 1998 | Earthquake resistance | Seismic actions & building rules (1), Bridges (2), Assessment/retrofitting (3), Silos/tanks (4), Foundations/retaining (5), Towers/masts/chimneys (6) |
| **Eurocode 9** | EN 1999 | Design of aluminium structures | General rules (1-1), Fire (1-2), Structures susceptible to fatigue (1-3), Cold-formed sheeting (1-4), Shell structures (1-5), Structures with tension elements (2) |

---

## 💡 Quick Examples

### 1. Imposed Loads from Eurocode 1 (EN 1991-1-1)

```python
from pamd_eurocodes.eurocode_1.part_1_1.Tables import (
    categories_of_use,
    imposed_loads_on_floors_balconies_and_stairs_in_buildings
)

# Print markdown formatted table
print(categories_of_use)

# Inspect imposed floor load table
print(imposed_loads_on_floors_balconies_and_stairs_in_buildings)
```

### 2. Using `BRange` for Parametric Calculations

Eurocodes often provide recommended values within allowable ranges. `BRange` seamlessly evaluates using the recommended default value in mathematical expressions:

```python
from pamd_eurocodes.range import BRange

# BRange(min=1.5, max=2.0, default=2.0)
q_k = BRange(1.5, 2.0, 2.0)

print(q_k)  # Output: <1.5, 2.0> (default value formatted)

# Perform arithmetic directly - uses the default recommended value (2.0):
gamma_q = 1.5
design_load = q_k * gamma_q
print(f"Design load: {design_load} kN/m2")  # 3.0 kN/m2

# Access range bounds
print(f"Min: {q_k.min}, Max: {q_k.max}, Default: {q_k.default}")
```

### 3. Querying Tables & Exporting to AutoCAD DXF

```python
from pamd_eurocodes.eurocode_1.part_1_1.Tables import imposed_loads_on_floors_balconies_and_stairs_in_buildings

# Search for a specific category row
balcony_load = imposed_loads_on_floors_balconies_and_stairs_in_buildings.get(query="Category A - Balconies")
print(balcony_load)

# Export the standard table to AutoCAD DXF format
imposed_loads_on_floors_balconies_and_stairs_in_buildings.toDXF("Category_A_Loads.dxf")
```

### 4. Working with Symbols and Terms & Definitions

```python
# Access LaTeX symbols
from pamd_eurocodes.eurocode_1.part_1_1 import Symbols

print(Symbols.alpha_A)  # LaTeX string and description

# Access official Eurocode terms & definitions
from pamd_eurocodes.eurocode_1.part_1_1 import TermsAndDefinitions

for term in TermsAndDefinitions.__all__:
    item = getattr(TermsAndDefinitions, term)
    print(f"{item.name}: {item.definition}")
```

---

## 🛠 Project Structure

```text
Eurocodes/
├── pamd_eurocodes/
│   ├── range.py                 # BRange class (bounded range with recommended default)
│   ├── table.py                 # Table class (markdown display & DXF export)
│   ├── symbol.py                # Symbol class (LaTeX representation)
│   ├── tad.py                   # TAD class (Terms And Definitions)
│   ├── eurocode_0/              # EN 1990: Basis of structural design
│   ├── eurocode_1/              # EN 1991: Actions on structures (Parts 1-1 to 4)
│   ├── eurocode_2/              # EN 1992: Design of concrete structures
│   ├── eurocode_3/              # EN 1993: Design of steel structures
│   ├── eurocode_4/              # EN 1994: Composite steel & concrete structures
│   ├── eurocode_5/              # EN 1995: Timber structures
│   ├── eurocode_6/              # EN 1996: Masonry structures
│   ├── eurocode_7/              # EN 1997: Geotechnical design
│   ├── eurocode_8/              # EN 1998: Earthquake resistance
│   └── eurocode_9/              # EN 1999: Aluminium structures
├── setup.py                     # Package distribution setup
└── workflow.bat                 # Build and PyPI deployment script
```

---

## 🤝 Contributing

Contributions are welcome! If you find missing tables, additional National Annex values, or want to contribute new parts:

1. Fork the repository: [https://github.com/Abstergo2003/PyAct](https://github.com/Abstergo2003/PyAct)
2. Create your feature branch (`git checkout -b feature/eurocode-update`)
3. Commit your changes (`git commit -m 'Add Eurocode tables'`)
4. Push to the branch (`git push origin feature/eurocode-update`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
