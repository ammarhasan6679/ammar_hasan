from typing import List, Dict
from Bio import Entrez, Medline
import csv


Entrez.email = "ammarhasan66679@gmail.com" 


def fetch_pubmed_ids(query: str, max_results: int = 10) -> List[str]:
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    return record.get("IdList", [])


def fetch_paper_details(pubmed_ids: List[str]) -> List[Dict[str, str]]:
    if not pubmed_ids:
        return []

    handle = Entrez.efetch(db="pubmed", id=",".join(pubmed_ids), rettype="medline", retmode="text")
    records = Medline.parse(handle)

    papers = []
    for record in records:
        authors = record.get("FAU", [])
        affiliations = record.get("AD", [])

        non_academic_authors = []
        company_affiliations = []

        for aff in affiliations:
            if is_non_academic(aff):
                company_affiliations.append(aff)

        if company_affiliations:
            non_academic_authors = authors

        papers.append({
            "pubmed_id": record.get("PMID", ""),
            "title": record.get("TI", ""),
            "date": record.get("DP", ""),
            "non_academic_authors": non_academic_authors,
            "company_affiliations": company_affiliations,
        })

    return papers


def is_non_academic(affiliation: str) -> bool:
    """Return True if affiliation looks like a company."""
    academic_keywords = ["university", "college", "school", "institute", "center", "hospital", "department"]
    company_keywords = ["pharma", "biotech", "inc", "ltd", "llc", "corporation", "company"]

    affil_lower = affiliation.lower()
    if any(word in affil_lower for word in company_keywords):
        return True
    if any(word in affil_lower for word in academic_keywords):
        return False
    return False

def save_to_csv(papers: List[Dict[str, str]], filename: str) -> None:
    """Save filtered papers to CSV file."""
    fieldnames = [
        "PubmedID",
        "Title",
        "Publication Date",
        "Non-academic Authors",
        "Company Affiliations"
    ]
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for paper in papers:
            if paper["company_affiliations"]:  
                writer.writerow({
                    "PubmedID": paper["pubmed_id"],
                    "Title": paper["title"],
                    "Publication Date": paper["date"],
                    "Non-academic Authors": "; ".join(paper["non_academic_authors"]),
                    "Company Affiliations": "; ".join(paper["company_affiliations"])
                })


if __name__ == "__main__":
    ids = fetch_pubmed_ids("covid vaccine 2023")
    details = fetch_paper_details(ids)
    
    save_to_csv(details, "output.csv")
    print("Results saved to output.csv")
