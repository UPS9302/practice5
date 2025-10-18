import wikipedia

# Set language
n=input("enter language code en/de/fr/hi:")
wikipedia.set_lang(n)
n2=int(input("Enter no. of sentences for summary:"))

# Search query
query = input("Enter a topic to search on Wikipedia: ")

# Get summary
try:
    summary = wikipedia.summary(query, sentences=n2)
    print("\nWikipedia Summary:")
    print(summary)
except wikipedia.exceptions.PageError:
    print("No page found for that topic.")
