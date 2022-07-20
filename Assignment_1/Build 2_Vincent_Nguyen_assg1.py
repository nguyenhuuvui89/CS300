'''
Intent: Begin to provide options for the form of one person to be addressed.

Postconditions: The following are on the console (excluding the numbering):
1.
Greetings from a beginning Python programmer.
2.
Do you want to be addressed as ...
.......................................======>Jane Margaret Doe?
.......................................======>Jane Doe?
.......................................======>Mr./Ms. Jane Margaret Doe?
.......................................======>Dear Jane?
or 
.......................................======>Doe, Jane Margaret?
'''

welcome="Greetings from a beginning Python programmer."
address="Do you want to be addressed as ..."
x=".......................................======>"
name1_line1="Jane Margaret Doe?"
name1_line2="Jane Doe?"
name1_line3="Mr./Ms. Jane Margaret Doe?"
name1_line4="Dear Jane?\nor"
name1_line5="Doe, Jane Margaret?"
print(welcome)
print(address)
print(x+name1_line1)
print(x+name1_line2)
print(x+name1_line3)
print(x+name1_line4)
print(x+name1_line5)
