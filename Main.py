import Email, Google, Read_CSV


def main():

    # SETTING
    num_rows = 10
    max_links_from_google = 2

    # import csv
    search_terms = Read_CSV.read_csv('suppliers.csv', num_rows)

    # iterate each tuple
    results = []

    results = Google.get_results(search_terms, max_links_from_google)
    emails = set()
    print("")
    for url in results:
        print("Working on: " + url)
        new_emails = Email.get_emails(url)

        if len(new_emails) != 0:
            print("Emails found from: " + url)
            for email in new_emails:
                print(email)
        else:
            print("No emails found from: " + url)
    print("\n=============================================\n")
if __name__ == "__main__":
    main()