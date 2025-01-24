with open("scrabble.txt", "r") as f:
    scrabble = f.readlines()

scrabble = [word.strip() for word in scrabble]

with open("liste.de.mots.francais.frgut.txt", "r", encoding="utf-8") as f:
    dictionary = f.readlines()

dictionary = [word.strip() for word in dictionary]

# Put all the words in dictionary in uppercase and without accents
dictionary = [word.upper() for word in dictionary]

# # Compute the intersection between the scrabble words and the dictionary
# intersection = set(scrabble).intersection(set(dictionary))
intersection = set(dictionary)

# Get rid of the words with less than 3 characters
intersection = [word for word in intersection if len(word) >= 3]


# Lemmatize the intersection
from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer
lemmatizer = FrenchLefffLemmatizer()

lemmatized_intersection = []
for word in intersection :
    for m in lemmatizer.lemmatize(word, 'all'):
        if m[1] != "np":
            lemmatized_intersection.append(m[0])

lemmatized_intersection = set(lemmatized_intersection)

# Open some ebooks to get another set to do an intersection with
from bs4 import BeautifulSoup
from pathlib import Path
import ebooklib
from ebooklib import epub

ebook_folder = Path("Ebooks")
all_words = set()

for file in ebook_folder.iterdir():
    book = epub.read_epub(file)

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content = BeautifulSoup(item.content, 'html.parser').get_text()

            for word in content.split():
                word = word.lower().strip('.,!?;:()[]{}"\'')
                all_words.add(word)

# do the intersection
intersection_with_books = lemmatized_intersection.intersection(all_words)

print(f"Number of words in the dictionary: {len(dictionary)}")
print(f"Number of words in the scrabble list: {len(scrabble)}")
print(f"Number of words in common: {len(intersection)}")
print(f"Number of words in common after lemmatization: {len(lemmatized_intersection)}")
print(f"Number of words in the intersection with the ebooks: {len(intersection_with_books)}")

# Sort the intersection
intersection_with_books = sorted(list(intersection_with_books))

# # Write the intersection to a file
# with open("intersection.txt", "w", encoding="utf-8") as f:
#     for word in intersection_with_books:
#         f.write(f"{word}\n")