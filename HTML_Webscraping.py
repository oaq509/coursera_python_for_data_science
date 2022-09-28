# Webscraping is a process that can be used to automatically extract information from a website,
# and can easily be accomplished within a matter of minutes and not hours. 

# In short term, Getting data from html web pages

# Beautiful Soup Objects 
# Beautiful Soup is a Python library for pulling data out of HTML and XML files, 
# we will focus on HTML files. This is accomplished by representing the HTML as a set of objects with methods used to parse the HTML. 
# We can navigate the HTML as a tree and/or filter out what we are looking for.

from bs4 import BeautifulSoup
import requests

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())

tag_object = soup.title # <title>Page Title</title>
# print("tag object:",tag_object)

type(tag_object) # <class 'bs4.element.Tag'>

tag_object = soup.h3 # <h3><b id="boldest">Lebron James</b></h3>

# ------------------------------------------------------------

# The find_all() method looks through a tag’s descendants and retrieves all descendants that match your filters.
# The Method signature for find_all(name, attrs, recursive, string, limit, **kwargs)
# We can store it as a string in the variable table:
table_bs = BeautifulSoup(table, "html.parser")

# ---------------------------------------------------
table_bs.find_all(id="flight")

# find all the elements without href value
table_bs.find_all(href=False)

# With string you can search for strings instead of tags,
# where we find all the elments with Florida.
table_bs.find_all(string="Florida")


# Scrape data from HTML tables into a DataFrame using BeautifulSoup and read_html
# ....
# ....