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

## Clone This Repository
###  Using SSH:
git clone git@github.com:ammarhasan6679/pubmed-project.git
cd pubmed-project

### Using HTTPS:
git clone https://github.com/ammarhasan6679/pubmed-project.git
cd pubmed-project

## 3️⃣ Install Dependencies
 poetry install

###✅ Usage
Run the tool through Poetry so it uses the correct environment.


### Basic Command
poetry run get-papers-list "covid vaccine" -f output.csv --debug

🧪 Examples
Search: AI in Medicine (print to console)
poetry run get-papers-list "AI in medicine"
Search: COVID Vaccine Papers (2024 onward; save to file)
poetry run get-papers-list "covid vaccine AND 2024:3000[dp]" -f covid_2024.csv --debug
Search: Cancer Immunotherapy
poetry run get-papers-list "cancer immunotherapy" -f cancer.csv
📄 Output Format (CSV)
Columns in the generated CSV:

Column	Meaning
PubMedID	Unique PubMed identifier.
Title	Paper title.
Publication Date	As reported by PubMed (e.g., 2025 Jul 15).
Non-academic Authors	Authors linked to at least one non-academic affiliation (heuristic: current version lists all authors if any industry affiliation found).
Company Affiliations	Affiliation strings flagged as industry (pharma, biotech, Inc., Ltd., LLC, etc.).

Example Row:

mathematica

40663029,Responses of Kidney Transplant Recipients...,2025 Jul 15,Walter D Park; Sumi S Nair,Janssen Scientific Affairs LLC; Janssen Vaccines
🧠 How Non-Academic Affiliations Are Detected
We classify each affiliation string using simple keyword rules.

Company Keywords (if any match → industry):
pharma, biotech, inc, ltd, llc, corporation, company, scientific affairs, clinical research

Academic Keywords (if found and no company word → academic):
university, college, school, institute, center, hospital, department, medical school

⚠️ This is a basic heuristic suitable for a take‑home exercise. Real data can be messy; see Future Enhancements below.

🗂 Project Structure

pubmed-project/
│
├── paper_finder/
│   ├── __init__.py
│   └── core.py          # PubMed fetch, filtering, CSV export
│
├── scripts/
│   └── cli.py           # CLI entry point (main())
│
├── README.md
├── pyproject.toml       # Poetry config (deps + CLI script)
└── poetry.lock          # Locked dependency versions
👩‍💻 Developer Notes
Run Module Directly (quick test)

poetry run python paper_finder/core.py
Run CLI (recommended)

poetry run get-papers-list "covid vaccine" -f results.csv --debug
Change Query (just replace text)

poetry run get-papers-list "AI in medicine" -f ai.csv
🔍 Example Debug Output

Query: covid vaccine
Output file: output.csv
Found PubMed IDs: ['40667140', '40667012', '40666529', ...]
Results saved to output.csv
⚠️ Limitations
All authors are marked “Non-academic Authors” if the paper has any industry affiliation (improvement needed).

Email extraction not fully implemented; AID fields in MEDLINE are not guaranteed emails.

Keyword filter may mislabel hospitals or government agencies.

max_results currently hard-coded (default 10).

🚀 Future Enhancements
Map each author to the correct affiliation (author ↔ org).

Extract corresponding author email robustly (MEDLINE + regex).

Add --max-results CLI option.

Add paging for large queries.

Improve industry detection with regex & known-company list.

JSON + Parquet exports.

Publish paper_finder to Test PyPI (bonus per spec).

Add tests + CI (GitHub Actions).




