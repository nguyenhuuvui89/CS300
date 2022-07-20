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
3.
After a blank line, the same output, but applied to Archibald Montague Abercrombie
4.
After a blank line, the same output, but applied to Cleopatra Anastasia Montgomery
'''

welcome="Greetings from a beginning Python programmer."
address="Do you want to be addressed as ...\n"
x=".......................................======>"
name1_line1="Jane Margaret Doe?"
name1_line2="Jane Doe?"
name1_line3="Mr./Ms. Jane Margaret Doe?"
name1_line4="Dear Jane?\nor"
name1_line5="Doe,Jane Margaret?\n"

name2_line1="Archibald Montague Abercrombie?"
name2_line2="Archibald Abercrombie?"
name2_line3="Mr./Ms. Archibald Montague Abercrombie?"
name2_line4="Dear Archibald?\nor"
name2_line5="Abercrombie,Archibald Montague?\n"

name3_line1="Cleopatra Anastasia Montgomery?"
name3_line2="Cleopatra Montgomery?"
name3_line3="Mr./Ms. Cleopatra Anastasia Montgomery?"
name3_line4="Dear Cleopatra?\nor"
name3_line5="Montgomery,Cleopatra Anastasia?"

print(welcome)
print(address)
print(x+name1_line1)
print(x+name1_line2)
print(x+name1_line3)
print(x+name1_line4)
print(x+name1_line5)

print(x+name2_line1)
print(x+name2_line2)
print(x+name2_line3)
print(x+name2_line4)
print(x+name2_line5)

print(x+name3_line1)
print(x+name3_line2)
print(x+name3_line3)
print(x+name3_line4)
print(x+name3_line5)
