# A list of types of emotional complaints and corresponding key words for each 
complaint_type = ['Depression', 'Human Relations', 'Substance Abuse']
key_words = [['depress', 'sad', 'down'],
             ['conflict', 'argument', 'mistreat', 'quarrel'],
             ['drug', 'alcohol', 'drink', 'cocaine', 'opioid', 'heroin']]


def get_complaint_type(a_user_complaint):
    '''
    Precondition: 
    1. a_user_complaint is a string
    2. complaint_type is a list of strings
    3. key_words is a list of lists of strings
    3. complaint_type and key_words are the same length
 
    Returns: observed_complaint_type, which consists of the indices in
    complaint_type that correspond to key_words elements partly in a_user_complaint.
    
    Example: if the user enters “I’ve been saddened by world conflicts”,
    the function returns the set consisting of 0 and 1 because “I’ve been saddened …”       
    contains “sad” and “conflict”.	
    '''
    complaint_set=set()
    for index in range(len(key_words)):
        for i in key_words[index]:
            if i in a_user_complaint.lower():
                complaint_set.add(index)
                break
    return complaint_set  

'''
Postconditions
1 (Welcome): A welcome message is on the console  
2 (user_complaint): user_complaint is the user's response in reply to "Please state your complaint:"
3 (observed_complaint_types): observed_complaint_types = get_complaint_type(user_complaint)
4 (Indices displayed): observed_complaint_types is on the monitor
'''

print("Thank you for using Eliza300, a fun therapy program")
print("Please state your complaint:")
user_complaint=input()
observed_complaint_type = get_complaint_type(user_complaint)
print(observed_complaint_type)
