# Binary and Bipolar Matrix Generator using BCH Codes

This repository provides Python code to generate **binary and bipolar matrices** for compressed sensing applications using **BCH (Bose–Chaudhuri–Hocquenghem) codes**.

---

## 📌 Features

- Construct binary matrix \( A \in \{0,1\}^{m \times n} \)
- Construct bipolar matrix \( B = 2A - 1 \in \{-1,+1\}^{m \times n} \)
- Based on BCH code structure and minimum distance
- Designed for compressed sensing and sparse recovery

---

## 📦 Files Overview

| File Name       | Description                                      |
|----------------|--------------------------------------------------|
| `bipolar.py`    | Main generator function for binary/bipolar matrices |
| `custom.py`     | Custom BCH code setup                            |
| `custom2.py`    | Alternate custom matrix construction             |
| `cyclo.py`      | Cyclotomic polynomial-related routines           |
| `dmin.py`       | Minimum distance computation                     |
| `nsymgen.py`    | BCH parameter generator (non-symmetric version) |
| `nsymmetric.py` | Symmetric variant of BCH parameter setup        |

---

## 🛠 Installation

You’ll need Python 3 and the following libraries:

```bash
pip install numpy galois
