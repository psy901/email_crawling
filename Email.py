import requests
from bs4 import BeautifulSoup
import re
from time import sleep


def extract_email_from_url(url):
    '''
    From the provided url, it extracts all valid email addresses
    :param url: URL to enter
    :return: Set of email addresses in string
    '''

    emails = set()
    try:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        text = soup.text

        # from the text, it collects all valid email addresses
        regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                            "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                            "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))
        emails_tuples = re.findall(regex, text)
    except:
        return emails

    for email in emails_tuples:
        emails.add(email[0])
    return emails

def get_links(url):
    '''
    From the URL, it returns all the links embedded
    :param url: URL to enter
    :return: Set of links in string
    '''

    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    set_links = set()

    # finds all the links and return them as a list
    for link in soup.findAll('a', limit=20):
        href = link.get('href')
        if href == None:
            continue

        if href.startswith("http"):
            set_links.add(href)
            # print("href = " + href)
        else:
            set_links.add(url + href)
            # print("href = " + url+href)

    return set_links

def get_emails(url):
    '''
    From the URL, it tries to extract emails from the landing page
    and its 2nd level pages. And it prints all the email addresses it retrieved
    :param url: provided URL from the user
    '''
    emails = set()

    # 1st level
    emails.update(extract_email_from_url(url))

    # TODO: skip level 2 if an email is found?
    # 2nd level -- iterate over the set of links
    set_links = get_links(url)

    for link_url in set_links:
        try:
            # print("working on: " + link_url)
            emails.update(extract_email_from_url(link_url))
        # except requests.exceptions.MissingSchema:
        #     # some links relative paths, so change them into absolute path
        #     new_url = url + link_url
        #     # print("working on changed one..." + new_url)
        #     emails.update(extract_email_from_url(new_url))
        except:
            pass

    return emails

# get_emails("http://www.tonnomaruzzella.it/contatti/")