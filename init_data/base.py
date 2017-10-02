import os
from urllib2 import urlopen
from zipfile import ZipFile


import pandas as pd


def download_dataset():
    if os.path.isdir("./init_data/BX-CSV-Dump"):
        return None

    print('Start downloading the dataset...')
    zipurl = 'http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip'
    # Download the file from the URL
    zipresp = urlopen(zipurl)
    # Create a new file on the hard drive
    tempzip = open("./init_data/BX-CSV-Dump.zip", "wb")
    # Write the contents of the downloaded file into the new file
    tempzip.write(zipresp.read())
    # Close the newly-created file
    tempzip.close()
    # Re-open the newly-created file with ZipFile()
    zf = ZipFile("./init_data/BX-CSV-Dump.zip")
    # Extract its contents into /tmp/mystuff
    # note that extractall will automatically create the path
    zf.extractall(path = './init_data/BX-CSV-Dump')
    # close the ZipFile instance
    zf.close()
    print('Finish downloading the dataset')


def get_books():
    
    download_dataset()
    
    book_cols = ['ISBN', 'Book-Title', 'Book-Author',
                 'Year-Of-Publication', 'Publisher', 'Image-URL-S', 'Image-URL-M', 'Image-URL-L']

    dtype = {
        'ISBN': 'object',
        'Book-Title': 'object',
        'Book-Author': 'object',
        'Year-Of-Publication': 'object',
        'Publisher': 'object',
        'Image-URL-S': 'object',
        'Image-URL-M': 'object',
        'Image-URL-L': 'object',
    }

    books = pd.read_csv('init_data/BX-CSV-Dump/BX-Books.csv', sep=';',
                        names=book_cols, usecols=range(8), encoding='latin-1', dtype=dtype, low_memory=False)

    return books
