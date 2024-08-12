import wikipedia

cities = [
    "Sydney",       
    "Melbourne",    
    "Brisbane",     
    "Perth",        
    "Adelaide",     
    "Hobart",       
    "Darwin",       
]

def city_content(city):
    page = wikipedia.page(city)
    return page.content


def count_words(text):
    words = text.split()
    return len(words)

word_counts = {}


for city in cities:
    content = city_content(city)
    word_count = count_words(content)
    word_counts[city] = word_count
    print(f"{city}: {word_count} words")


longest_city = max(word_counts, key=word_counts.get)
print(f"\nThe city with the longest Wikipedia page is {longest_city} with {word_counts[longest_city]} words.")
