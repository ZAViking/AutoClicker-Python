import wikipedia
import datetime

WikiSearch = input("What would you like to search: ")
print("\nSearching...")

print(wikipedia.page(WikiSearch).title)
print(wikipedia.summary(WikiSearch))
print("\nBelow are some categories you may be interested in:")
print(wikipedia.page(WikiSearch).categories)
print("\nBelow are some references")
print(wikipedia.page(WikiSearch).references)
print("\nHere is the URL")
print(wikipedia.page(WikiSearch).url)

x = datetime.datetime.now()

print(x.strftime("\nToday is the %dth of %B %Y"))
