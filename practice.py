cal_in_sec = 24
name_of_unit = "hours"


def days_to_unit(num_of_days):
      return(f"{num_of_days} days are in {num_of_days*cal_in_sec} {name_of_unit}")
    
    

def validate_and_execute():
   #if user_input.isdigit():
   try: 
      user_input_number = int(user_input)
      if user_input_number > 0:
        my_calculated_result = days_to_unit(user_input_number)
        print(my_calculated_result)
      elif user_input_number == 0:
       print("you entered 0, please enter a positive number")
      else:
         print("invalid number,conversion can not work")
   #else:
   except ValueError:
      print("your input is not a number, please enter a valid number")


user_input = input("hey! user, type the value that will be used in calculating the number of days\n")
validate_and_execute()
