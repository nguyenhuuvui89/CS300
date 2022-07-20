# Eliza300
# Intent: A list of helpful actions that a troubled person could take. Build 2

possible_actions = ['taking up yoga', 'sleeping eight hours a night', 'relaxing', 
        'not working on weekends', 'spending two hours a day with friends']

'''
Precondition: possible_actions is the list defined above

Postconditions:

1. (Welcome): A welcome message is on the console

2. (user_complaint): user_complaint is the user's response to
"Please describe your emotional complaint--in one punctuation-free line: "

3. (how_long): how_long is the user's string response to
"How many months (between 1 and 99) have you experienced ...?"

4. (Month validity): EITHER how_long has the requested form
OR this terminated AND "Sorry, illegal input. Eliza is quitting; run Eliza again."
is on the console

5. (Advice): EITHER how_long >= 3
OR "Please return in * months" is on the console where * is 3 - how_long

6. (actions_not_taken): actions_not_taken consists of the actions (elements) in
possible_actions that the user answered 'n' to when questioned "Have you tried..."

7. (Summarized): Eliza300 recommended that the user take the actions in
actions_not_taken
'''

print("Thank you for using Eliza300, a fun therapy program.")
x=input("Please describe your emotional complaint--in one punctuation-free line:\n")
y=input("How many months (between 1 and 99) have you experienced...? '{}'?\n".format(x))
if y.isnumeric() and 1<int(y)<99:
    y=int(y)
    if y<3:
        print("Please return in {} months".format(3-y))
    else:
        print("{} months is significant. Sorry to hear it".format(y))
        actions_not_taken=[]
        for i in possible_actions:
            z=input("Have you tried...{}? Please answer y or n:\n".format(i))
            if z.lower()=="n":
                actions_not_taken.append(i)
        print("After careful analysis:), here is Eliza300's advice:")
        for actions in actions_not_taken:
            print(actions)
else:
    print("Sorry, illegal input. Eliza is quitting; run Eliza again.")
