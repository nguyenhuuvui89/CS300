'''
Eliza300: Postconditions
1. (Welcome): A welcome message is on the console
2. (Complaint): A complaint was entered by the user in response to a prompt
3. (Duration): A duration in months was entered by user in response to a prompt
4. (Error check): EITHER the user entered an integer between 1 and 100 for duration after being given up to two chances OR the application quit after suggesting a re-run.
5. (Action Recommended): EITHER how_long exceeds 2 months, and the phrase
   “ … months is too much time to go without help! Let's schedule a few 
   sessions" is on the console OR the following is on the console:
   "Come back in a couple of months if this persists".
'''
print("Thank you for using Eliza300, a fun therapy program.")
x=input("Please state your complaint: \n")
y=input("How many months has it  been that have you experienced '{}'?\n".format(x))
if y.isnumeric() and 1<int(y)<100:
    if int(y)>2:
        print("{} months is too much time to go without help! Let's schedule a few sessions.".format(y))
    else:
        print('"Come back in a couple of months if this persists".')
else:
    z=input("Please try one more time to enter duration in months less than 100\n")
    if z.isnumeric() and 1<int(z)<100:  
        if int(z)>2:
            print("{} months is too much time to go without help! Let's schedule a few sessions.".format(z))
        else:
            print('"Come back in a couple of months if this persists".')
    else:
        print("Sorry, try running Eliza again.")
        
