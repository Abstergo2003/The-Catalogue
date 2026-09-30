# 🌍 The Catalogue

> **The Ultimate Data Companion for Engineers & Scientists**

Welcome to **The Catalogue**, a comprehensive, modular collection of reference data, physical constants, and material properties designed for professionals, researchers, and students across all engineering and scientific disciplines. 

Stop wasting time searching through handbooks, datasheets, or obscure webpages for standard values. **The Catalogue** brings the data directly to your codebase with easy-to-use Python packages!

---

## 🚀 Why Use The Catalogue?

- 🛠 **All-in-One Engineering Data:** From Civil Engineering to Chemistry and Biology, we provide the foundational data you need to build robust models, simulations, and applications.
- 📦 **Modular Design:** Import only what you need. Each discipline is separated into its own lightweight Python package.
- ⚡ **Ready for Automation:** Perfect for scripts, data analysis, structural calculations, and scientific modeling.
- 📖 **Reliable & Structured:** Cleanly organized modules and constants mean fewer typos and more time doing actual engineering.

---

## 📚 Supported Disciplines

### 🏗 Civil Engineering (`pamd_civil_engineering`)
Build the world with confidence. Access a vast library of structural materials and geometric properties for load-bearing calculations.
- **Materials:** Steel, Concrete, Softwood, Aluminium, Soil, Mortar, and Masonry Units.
- **Structural Components:** Rebars, Bolt Grades & Sizes.
- **Beam Cross-Sections:** 
  - **Steel:** L-shapes, C-channels, T-beams, Z-sections, Circular, Square, Rails, Sheets, and more.
  - **Wood:** Rectangular and Composite beams.
- **Physical Constants & Conversions:** Standardized units and engineering conversions.

### 🧪 Chemistry (`pamd_chemistry`)
The building blocks of matter at your fingertips. Essential thermodynamic and chemical data for reactions and material science.
- **The Elements:** Complete Periodic Table data.
- **Thermodynamics:** Latent Heats, Vapor Pressures, Bond Energies.
- **Reactions & Solutions:** Acid Dissociation constants, Solubility Products, Reduction Potentials.
- **Compounds & Constants:** Extensive database of chemical compounds and universal physical constants.

### 🧬 Biology (`pamd_biology`)
Model life itself. Core biological parameters and biochemical data for biomedical engineers, bioinformatics, and computational biologists.
- **Biochemistry:** Amino Acids, Nucleic Acids, Enzyme Kinetics, Bioenergetics.
- **Cellular & Organism Data:** Cell Biology metrics, Organism Genomes, Macromolecule Density.
- **Physiology:** Standard Blood Parameters.

---

## 🛠 Installation & Usage

Each module is built as an independent Python package. You can install them locally from this repository. For instance:

```bash
# Clone the repository
git clone https://github.com/yourusername/The_Catalogue.git
cd The_Catalogue

# Install the Civil Engineering catalogue
cd Civil_Engineering
pip install .
```

```python
# Example Usage in Python
from pamd_civil_engineering.Beams.Steel.C import C_Beam # (Example import path)
from pamd_chemistry.PeriodicTable import Element

# Start engineering!
```

---

## 🤝 Contribute

Are you an Electrical, Mechanical, Aerospace, or Software Engineer? We are constantly expanding! **The Catalogue** is built for engineers, by engineers. Feel free to open a Pull Request and add standard datasets for your specific domain!

**Join us in building the largest open-source programmatic handbook for engineers!**
