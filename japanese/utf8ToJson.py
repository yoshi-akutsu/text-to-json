import json
import re

# Import Japanese tokenizer Sudachi
from sudachipy import tokenizer
from sudachipy import dictionary

tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.C

# Open book txt file
book = open("encodedJp.txt","r")

bookContents = book.readlines()

# Set global variables
newChapter = []
newParagraph = []
chapter = ''
counter = 1

#  Removes furigana
regex = "\《.*?\》"
cleanedBookArray = []

# Create class and instantiate BookObj object
class BookObj():
    pass
myBook = BookObj()

for line in bookContents:
    cleanedBookArray.append(re.sub(regex, "", line))

# Iterates each line in book
for paragraph in cleanedBookArray:
    # Finds line starting new chapter
    if "は中見出し" in paragraph:
        
        chapter = 'chapter' + str(counter)
        print(chapter)
        counter += 1
        newChapter = []
        newParagraph = []
    # If not a new chapter, add it to the paragraph array
    else:
        if "END" in paragraph:
            setattr(myBook, chapter, newChapter)
            newParagraph = []
        else: 
            newParagraph = [m.surface() for m in tokenizer_obj.tokenize(paragraph, mode)]
            newChapter.append(newParagraph)
            newParagraph = []
        
with open('bookJp.json', "w") as file_write:
    json.dump(myBook.__dict__, file_write)

book.close()