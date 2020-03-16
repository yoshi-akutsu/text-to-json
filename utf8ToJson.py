import json

# Open book txt file
book = open("encodedJp.txt","r")

bookContents = book.readlines()

# Set global variables
newChapter = []
newParagraph = []
chapter = ''
counter = 1

# Create class and instantiate BookObj object
class BookObj():
    pass
myBook = BookObj()

# Iterates each line in book
for paragraph in bookContents:
    # Finds line starting new chapter
    if "中見出し" in paragraph:
        chapter = 'chapter' + str(counter)
        print(chapter)
        counter += 1
        newChapter = []
        newParagraph = []
    # If not a new chapter, add it to the paragraph array
    else:
        words = paragraph.split(" ")
        # Ignores empty lines
        if words[0].isspace() == False:
            newParagraph.append(words)
        else:
            newChapter.append(newParagraph)
            newParagraph = []
    if 'END' in paragraph:
        setattr(myBook, chapter, newChapter)
        
with open('bookJp.json', "w") as file_write:
    json.dump(myBook.__dict__, file_write)

book.close()