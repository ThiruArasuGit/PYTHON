'''
Author: Thirunavukkarasu A
Purpose: This file contains the general reusable functions.
'''

import requests

default_chunk_size = 2048


def download_ebooks(dwnld_url, dest=None):
    req = requests.get(dwnld_url, stream=True)
    book_name = dwnld_url[str(dwnld_url).rfind("/") + 1:]
    # print(book_name)
    if dest is not None:
        with open(dest + book_name, 'wb') as df:
            for chunk in req.iter_content(chunk_size=default_chunk_size):
                if chunk:
                    df.write(chunk)
        print(df.name + ' downloaded successfully!')
    else:
        with open(book_name, 'wb') as df:
            for chunk in req.iter_content(chunk_size=default_chunk_size):
                if chunk:
                    df.write(chunk)
        print(df.name + ' downloaded successfully!')


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

