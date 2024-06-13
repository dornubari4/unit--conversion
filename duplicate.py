#print("there are " + str(24) + " secs in one day")
cal_in_sec = 24
name_of_unit = "hours"
#print("20 days are in " + str(20*cal_in_sec) + " hrs")
#print(f"20 days are in {20*cal_in_sec} hrs")


def days_to_unit(num_of_days):
    #check = (num_of_days > 0)
    #print(type(check))
    if num_of_days > 0: #this line was remove and placed undet another fnction that is createdd as a nested if else statement
      return(f"{num_of_days} days are in {num_of_days*cal_in_sec} {name_of_unit}")
    #print ("it is well")
    elif num_of_days == 0:
       return("you entered 0, please enter a positive number")
    else:
       return("invalid number,so no conversion can be done")

#my_var = days_to_unit(20)
#print(my_var)
user_input = input("hey! user, type the value that will be used in calculating the number of days\n")
#print(type(user_input))
if user_input.isdigit():
   user_input_number = int(user_input)
# we can also nest in a function call instead of passing the function int() to a variable and calling the variable in the next line we can save ourselves the stress by doing this
# deleteting the aboveline of code which is 
#user_input_number = int(user_input)
#and  we rewrite the below code as this, this is called a nested
# my_calculated_result = days_to_unit(int(user_input))
   my_calculated_result = days_to_unit(user_input_number)
#print(type(user_input_number))
   print(my_calculated_result)
else:
   print("your input is not a number, please enter a valid number")