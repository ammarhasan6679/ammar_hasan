Project Title & Description

A short summary of what the project does (e.g., "A CLI tool to fetch PubMed papers and identify non-academic authors").

Features

What the tool can do (fetch papers, filter industry authors, export to CSV, etc.).

External Tools & Dependencies
(This is important as per your requirement)

Poetry (for dependency management)

Biopython (for PubMed API)

Requests (HTTP requests)

NCBI Entrez API (data source)

Python 3.10+

Installation Instructions

How to install Poetry

How to clone the repo

How to install dependencies (poetry install)

Usage Guide

How to run the CLI with examples:

bash
Copy
Edit
poetry run get-papers-list "covid vaccine" -f output.csv --debug
Explain all arguments:

query → PubMed search query

-f → output file name

--debug → enable logs

Output Format

Explain what the CSV contains:

PubMed ID

Title

Date

Non-academic authors

Company affiliations

Project Structure

Show folder layout (paper_finder/, scripts/, etc.).

License

Add MIT License (or whichever you prefer).

