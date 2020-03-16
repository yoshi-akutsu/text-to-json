import json

# Open book txt file
book = open("trimmedEng.txt","r")

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
for line in bookContents:
    # Finds line starting new chapter
    if "CHAPTER" in line:
        chapter = 'chapter' + str(counter)
        counter += 1
        newChapter = []
        newParagraph = []
    # If not a new chapter, add it to the paragraph array
    else:
        words = line.split(" ")
        # Ignores empty lines
        if words[0].isspace() == False:
            newParagraph.append(words)
        else:
            newChapter.append(newParagraph)
            newParagraph = []
    if 'END' in line:
        setattr(myBook, chapter, newChapter)
        
with open('book.json', "w") as file_write:
    json.dump(myBook.__dict__, file_write)

book.close()