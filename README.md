# 📚 PubMed Paper Finder

A **command-line tool** to search **PubMed** for research papers and identify **non-academic (industry-affiliated) authors**.  
The tool fetches PubMed data using the **NCBI Entrez API**, filters out academic affiliations, and exports the results to a **CSV file**.

---

## ✅ Features
- Fetches PubMed articles using **NCBI API**  
- Identifies **company/industry affiliations** (pharma, biotech, etc.)  
- Exports results to **CSV** (PubMed ID, Title, Authors, Company info)  
- Simple **CLI** with query, output file, and debug options  

---

## ✅ External Tools & Dependencies
This project uses the following external tools and libraries:

- **[Poetry](https://python-poetry.org/)** → Dependency and environment manager  
- **[Biopython](https://biopython.org/)** → For interacting with the NCBI Entrez API  
- **[Requests](https://docs.python-requests.org/)** → For handling HTTP requests (future scope)  
- **NCBI Entrez API** → Data source for PubMed  
- **Python 3.10+** → Required for running the project  

---

## ✅ Installation Guide

### 1️⃣ Install Poetry
```bash
pip install poetry

