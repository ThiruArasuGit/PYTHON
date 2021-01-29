'''
Author: Thirunavukkarasu A
Purpose: This file contains the general reusable functions.
'''

import requests

default_chunk_size = 2048


# GOALKICKER.com
def download_ebooks(dwnld_url, dest=None):
    req = requests.get(dwnld_url, stream=True)
    book_name = dwnld_url[str(dwnld_url).rfind("/") + 1:]
    # print(book_name)
    if dest is not None:
        with open(dest + book_name, 'wb') as df:
            for chunk in req.iter_content(chunk_size=default_chunk_size):
                if chunk:
                    df.write(chunk)
        return df.name + ' downloaded successfully!'
    else:
        with open(book_name, 'wb') as df:
            for chunk in req.iter_content(chunk_size=default_chunk_size):
                if chunk:
                    df.write(chunk)
        return df.name + ' downloaded successfully!'


# DATAWORLD.com
def download_csv_data(url, file_name, dest=None):
    req = requests.get(url, stream=True)
    if dest is not None:
        with open(dest + file_name, 'wb') as csvFile:
            for chunk in req.iter_content(chunk_size=default_chunk_size):
                if chunk:
                    csvFile.write(chunk)
        return file_name + ' downloaded successfully at ' + dest
    else:
        with open(file_name, 'wb') as csvFile:
            for chunk in req.iter_content(chunk_size=default_chunk_size):
                if chunk:
                    csvFile.write(chunk)
        return file_name + ' downloaded successfully!'


# Get details from email-id
def generate_email_id(firstname, lastname, domain=None):
    if domain is not None:
        return firstname.lower() + '.' + lastname.lower() + '@' + domain
    else:
        return firstname.lower() + '.' + lastname.lower() + '@blueyonder.com'


# get details from email_id
def collect_details(email=None):
    if email is not None:
        dtls = []
        splval1 = email.split('.')[0].capitalize()
        firstname = splval1
        dtls.append(firstname)
        splval2 = (email.split('.')[1]).split('@')[0].capitalize()
        lastname = splval2
        dtls.append(lastname)
        domain = email.split('@')[1]
        dtls.append(domain)
        company = domain.split('.')[0].capitalize()
        dtls.append(company)

        return dtls

    else:
        return 'Please pass valid email id.'
