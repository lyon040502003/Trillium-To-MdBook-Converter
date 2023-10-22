# Trillium-To-MdBook-Converter
This is a very simple Trillium notes to MdBook converter

it allows you to write your documentation or other text based data and then convert it to html so you could for example host it on github sites. 


#### Export From Trillium

export an trillium tree that you want to convert to an md book 

export it as markdown and unpack it after you downloaded it 

#### Generate Book

run the main.py file and give the path to the downloaded trillium export and the name for your mdbook seperated by a collum 

example : 

/path/to/trillium-exp, book\_name, /path/to/book

do not use anny spaces in the name 

#### Test Server Book

cd into your books directory 

then runn :  mdbook serve  
 

#### build your book

while your still in your books directory just runn : mdbook build 
