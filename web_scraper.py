
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

quotes = soup.find_all('div', class_='quote')  # Each quote is inside a div with class 'quote'
data = []
for quote in quotes:
    text = quote.find('span', class_='text').text.strip()
    author = quote.find('small', class_='author').text.strip()
    tags = [tag.text for tag in quote.find_all('a', class_='tag')]  # Tags are in <a> elements
    data.append({'Quote': text, 'Author': author, 'Tags': ', '.join(tags)})

df = pd.DataFrame(data)
print("First few rows of the DataFrame:")
print(df.head())  # Preview the first few rows

df.to_csv('quotes_data.csv', index=False)
print("Data saved to 'quotes_data.csv'.")

# Split tags into individual words and count their frequency
all_tags = [tag for tags in df['Tags'] for tag in tags.split(', ')]
tag_counts = Counter(all_tags)

top_tags = tag_counts.most_common(10)
tags, counts = zip(*top_tags)

plt.figure(figsize=(10, 6))
plt.bar(tags, counts, color='skyblue')
plt.title('Top 10 Most Frequent Tags in Quotes')
plt.xlabel('Tag')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("Visualization complete!")