import wikipedia

# Set language
n=input("enter language code en/de/fr/hi:")
wikipedia.set_lang(n)

# Search query
query = input("Enter a topic to search on Wikipedia: ")

# Get summary
try:
    summary = wikipedia.summary(query, sentences=3)
    print("\nWikipedia Summary:")
    print(summary)
except wikipedia.exceptions.PageError:
    print("No page found for that topic.")
