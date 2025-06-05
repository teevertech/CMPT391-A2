# 📊 Premier League Data Analytics — CMPT 391, Spring 2025

This project is a data analytics case study for **CMPT 391: Database Management Systems** at MacEwan University. The goal is to clean, process, and analyze **English Premier League match data** using Python, applying the following data mining techniques:

- Association Rule Mining  
- Clustering  
- Classification  

---

## 🔍 Objectives

- Acquire and explore Premier League football data from Kaggle  
- Perform data cleaning, preparation, and integration  
- Apply a data mining technique (classification, clustering, or association rules)  
- Generate visualizations and insights into patterns and trends  
- Submit a report with clear, well-organized, and professional presentation

---

## 📁 Project Structure

```
league_analysis/
├── input/                # Raw CSV files from Kaggle dataset
├── output/               # Analysis output (tables, graphs, cluster labels, etc.)
├── league_analysis.py    # Main script that performs all analysis steps
├── setup.sh              # Creates virtual environment and installs dependencies
├── run.sh                # Runs the main analysis script
├── requirements.txt      # Required Python packages
├── LICENSE               # Open source license
└── README.md             # This file
```

## ▶️ Getting Started

### 1. Initial Setup of Environment

```bash
./setup.sh
```

This will create a Python virtual environment and install required libraries.

### 2. Run Analysis

```bash
./run.sh
```

This will check if the virtual environment is activate and if not activate it and then run our analysis script.

---

## 📦 Dependencies

- Python 3.10+
- pandas

Install manually:

```bash
pip install -r requirements.txt
```

---

## 🔗 Dataset

> [Premier League Dataset on Kaggle](https://www.kaggle.com/datasets/zaeemnalla/premier-league)

---

## 📜 License

This project is open source and licensed under the terms of the MIT License.
