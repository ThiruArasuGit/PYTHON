"""
Purpose: Download the the given list of e-books from goalclicker.com website.
        The files are in pdf format.
        example:
         'https://goalkicker.com/GitBook/GitNotesForProfessionals.pdf'

"""
from utilFile import download_ebooks

book_list = ['Git', 'MySQL', 'PostgreSQL', 'Python', 'Algorithms', 'Java', 'SpringFramework', 'MongoDB']
book_ext = 'NotesForProfessionals.pdf'
web_site = 'https://goalkicker.com/'
dest_dir = r'C:/GWS/pdf_files/Technical-e-Books/'

for book in book_list:
    book_url = web_site + book + "Book/" + book + book_ext
    # print(book_url)
    # download_ebooks(book_url)
    download_ebooks(book_url, dest_dir)
