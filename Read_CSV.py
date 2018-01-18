import pandas as pd


def read_csv(filename, num_rows):
    # print("")
    df = pd.read_csv(filename, encoding='latin-1', nrows=num_rows)
    table = df[['Name', 'Country']]

    search_terms = []
    # getting columns of name and country
    for index, row in table.iterrows():
        name = row['Name']
        # country = row['Country']
        search_term = name
        search_terms.append(search_term)
    return search_terms
