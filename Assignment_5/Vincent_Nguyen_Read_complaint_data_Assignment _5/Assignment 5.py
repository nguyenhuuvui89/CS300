complaint_types = []
key_words = []


def read_complaint_data():
    '''
    Intent: Get complaint_types and key_words from local ElizaData.txt

    Precondition =========

    ElizaData.txt is a local file consisting of paragraphs of the form

    On first line: 'Key Words for '<phrase describing a complaint category>
    On second line: <words, separated by blanks, that may occur within a
    description of the corresponding category>

    Example of ElizaData.txt:

    Key Words for Depression
    depress sad

    Key Words for Human Relations
    conflict argument mistreat

    Postconditions =========

    (1) complaint_types = list of the phrases in ElizaData.txt describing all
    complaint categories
    {2) key_words = list of lists of words in ElizaData.txt that may occur
    within phrases that describe the corresponding complaint category

    '''
    data_file = open("ElizaData.txt", "rt")
    read_line = data_file.readline().rstrip()
    while read_line != "":
        word_index = read_line.index("for")
        complaint_word = read_line[word_index + 4:]
        complaint_types.append(complaint_word)
        read_line = data_file.readline().rstrip()
        key_words.append(read_line.split(" "))
        read_line = data_file.readline().rstrip()
    data_file.close()


read_complaint_data()  # need to execute this here

print("Printing complaint_types and key_words from ...runtime_data...")
print(complaint_types)
print(key_words)





