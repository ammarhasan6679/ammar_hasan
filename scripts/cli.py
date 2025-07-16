import argparse
from paper_finder.core import fetch_pubmed_ids, fetch_paper_details, save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-f", "--file", help="Output CSV file name", default=None)
    parser.add_argument("-d", "--debug", help="Enable debug mode", action="store_true")

    args = parser.parse_args()

    if args.debug:
        print(f"Query: {args.query}")
        if args.file:
            print(f"Output file: {args.file}")

    ids = fetch_pubmed_ids(args.query)
    if args.debug:
        print(f"Found PubMed IDs: {ids}")

    details = fetch_paper_details(ids)

    if args.file:
        save_to_csv(details, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in details:
            if paper["company_affiliations"]:
                print(f"{paper['pubmed_id']} - {paper['title']}")

if __name__ == "__main__":
    main()
