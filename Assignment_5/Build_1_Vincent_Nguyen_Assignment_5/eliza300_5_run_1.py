import eliza300_5_functions_1

advice_per_type = [
    ['Get out more.', 'Take up a hobby that you love.'],
    ["Don't expect too much of people.", "Don't take offence easily."],
    ['Get counseling.', "Don't delay action on counseling."]]

print("Thank you for using Eliza300, a fun therapy program")
print("Please state your complaint:")
user_complaint=input()
observed_complaint_type = eliza300_5_functions_1.get_complaint_type(user_complaint)

for number in observed_complaint_type:
    for remedy in advice_per_type[number]:
        print(remedy)
