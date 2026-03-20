<div align="center">

# 🩸 Blood Bank Management System

### SPARK 2026 — Nigeria South South Capstone Project
**Group: Neural Sight** · Project #08

---

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557c?style=flat-square)
![Kaggle](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?style=flat-square&logo=kaggle&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

</div>

---

## 📌 Project Overview

A class-based blood bank management system built in Python that tracks blood donations, monitors inventory levels, flags critical shortages, and generates visualisations of supply, donor demographics, and donation trends over time.

Built as part of the **SPARK 2026 Data Science Capstone** for the Nigeria South South cohort.

---

## 🎯 Objectives

- Load and process blood donation records from CSV
- Track accepted blood volume per blood type as usable inventory
- Compare supply against demand and flag critical shortages
- Visualise inventory, donor demographics, and donation trends

---

## 🏗️ System Design

### Classes

| Class | Responsibility |
|---|---|
| `Donor` | Models an individual donor — stores ID, name, gender, age, and blood type |
| `BloodBank` | Manages the full system — loads data, tracks inventory, checks supply, flags shortages |

### Key Methods

| Method | Description |
|---|---|
| `load_donations(filepath)` | Reads the CSV, filters accepted donations, builds inventory by blood type |
| `check_supply(demand_dict)` | Compares current inventory against a demand dictionary, returns status table |
| `flag_shortage(threshold)` | Flags any blood type with volume below the critical threshold (default: 1,000ml) |

---

## 📊 Visualisations

Three charts are generated from the dataset:

**1. Bar Chart — Blood Type Inventory**  
Total accepted volume (ml) per blood type, sorted descending. Highlights which types are well-stocked and which are critically low.

**2. Pie Chart — Donor Demographics**  
Gender distribution across all donors in the dataset. Split is approximately 52% Female / 48% Male.

**3. Line Chart — Donations Over Time**  
Donation frequency plotted by date across the full 2023–2024 period. Shows irregular, campaign-driven donation patterns.

---

## 📁 Dataset

| Field | Description |
|---|---|
| `donor_id` | Unique donor identifier |
| `donor_name` | Full name |
| `gender` | Male / Female |
| `age` | Donor age |
| `blood_type` | One of 8 types: A+, A-, B+, B-, O+, O-, AB+, AB- |
| `volume_ml` | Volume donated in millilitres |
| `donation_date` | Date of donation (YYYY-MM-DD) |
| `status` | Accepted / Pending / Deferred |
| `source` | Walk-in / Referred / Campaign |


---

## 🔍 Key Findings

From the 100 donation records in the dataset:

- Only **39% of donations** were accepted into inventory — the rest were deferred or pending
- Total accepted volume: **14,473 ml** across 8 blood types
- **A+ (350ml)** and **B+ (618ml)** are critically low — both fall below the 1,000ml safety threshold
- **AB+** and **AB-** have the strongest supply relative to demand
- Donor source is well-distributed: Campaign (36%), Walk-in (34%), Referred (30%)

---


```python
bb = BloodBank()
df = bb.load_donations('/kaggle/input/.../08_blood_donations.csv')

supply_status = bb.check_supply(demand)
critical_shortages = bb.flag_shortage(threshold=1000)
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Pandas** — data loading and manipulation
- **Matplotlib** — all visualisations
- **Kaggle Notebooks** — execution environment

---

## 👥 Group

**Neural Sight**  
SPARK 2026 · Nigeria South South Cohort

---

<div align="center">
<sub>SPARK 2026 Data Science Capstone · Nigeria South South</sub>
</div>
