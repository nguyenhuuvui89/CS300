'''
Postconditions
1 (Welcome): A welcome message is on the console
2 (user_complaint): user_complaint is the user's response in reply to "Please state your complaint:"
3 (observed_complaint_types): observed_complaint_types = get_complaint_type(user_complaint)
4 (Remedies displayed): the remedies in advice_per_type corresponding to
observed_complaint_types are on the monitor, one line for each.

Example: the user entered “I’ve been saddened by world conflicts,” and the
following is on the console after execution:
Get out more.
Take up a hobby that you love.
Don't expect too much of people.
Don't take offence easily.
'''
from eliza300_5_runtime_data import complaint_types, key_words
def get_complaint_type(a_user_complaint):
    complaint_set = set()
    for index in range(len(key_words)):
        for i in key_words[index]:
            if i in a_user_complaint.lower():
                complaint_set.add(index)
                break
    return complaint_set