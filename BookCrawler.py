from requests import get
from bs4 import BeautifulSoup
import pause

bookAmount = int(input("Enter amount of books you wish to see: "))

pageCap = bookAmount // 20
pageRem = bookAmount % 20

for page in range(0, int(pageCap) + 1):

    response = get('https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=20&page=' + str(page + 1))

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

    if page < pageCap:
        for index, book in enumerate(book_container):
            print("Rank: " + ranks[index])
            print("Title: " + titles[index])
            print("\t" + authors[index])
            print("Published: " + dates[index])
            print("Price: " + prices[index] + "\n")
    else:
        for index in range(0, pageRem):
            print("Rank: " + ranks[index])
            print("Title: " + titles[index])
            print("\t" + authors[index])
            print("Published: " + dates[index])
            print("Price: " + prices[index] + "\n")

    # Pause retrieving info from website so servers don't get strained
    pause.sleep(2)
