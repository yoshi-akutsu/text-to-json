# text-to-json

A python script used to turn text files from both Project Gutenberg into JSON files for upload to a database. 
English text files we parsed based on lines into chapter-key - paragraph-array-value pairs. 
Paragraph-array-values were divided into line-arrays. 
The Japanese text files, sourced from Aozora Bunko, were parsed in a similar fashion without lines after 
conversion to UTF-8 from SHIFT-JIS.

