from requests import get
from bs4 import BeautifulSoup
import pause

bookAmount = int(input("Enter amount of books you wish to see: "))

for page in range(1, int(bookAmount / 21) + 2):

    response = get('https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=20&page=' + str(page))

    # Start Parsing
    soup = BeautifulSoup(response.text, 'html.parser')

    book_container = soup.find_all('div', class_='pb-m mt-m bd-bottom-disabled-gray record')

    ranks = []
    titles = []
    authors = []
    dates = []
    prices = []

    for book in book_container:
        ranks.append(book.div.div.text)
        titles.append(book.div.h3.a.text)
        authors.append(book.find('div', class_='product-shelf-author contributors').text)
        dates.append(book.div.h3.span.text)
        prices.append(book.find('div', class_='product-shelf-pricing mt-s mb-s').tbody.tr.span.a.text)

    print("B&N Top 100 Book Bestsellers:")

    for index, book in enumerate(book_container):
        print("Rank: " + ranks[index])
        print("Title: " + titles[index])
        print("\t" + authors[index])
        print("Published: " + dates[index])
        print("Price: " + prices[index] + "\n")

    # Pause retrieving info from website so servers don't get strained
    pause.sleep(5)