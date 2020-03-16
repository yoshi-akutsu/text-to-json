import codecs

with codecs.open("jp.txt", mode='r', encoding='shiftjis') as file:
    lines = file.read()

with codecs.open("encodedJp.txt", mode='w') as file:
    for line in lines:
        file.write(line)