

# function to see if user has selected yes or no

def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes or no")

# function to check if the user had input a valid integer

def num_check(question, low, high):

    error = f"Enter the number between {low} and {high}"

    while True:
        try:
            response = int(input(question))

            if response >= low and response < high:
                return response

            else:
                print(error)

        except ValueError:
            print("Please enter an integer.")


# function to check that user has not left answer blank

def not_blank(question):
    while True:
        response = input(question)
        if response:
            return response
        else:
            print("Sorry this can't be blank. Please try again")

# function to check that the user has selected on of the 2 responses

def string_checker(question, num_letters, valid_responses):
    error = f"Please choose {valid_responses[0]} or {valid_responses[1]}"
    while True:
        response = input(question).lower()
        for item in valid_responses:
            if response in (item[:num_letters], item):
                return item
        print(error)

# main routine goes here

yes_no_list = ["yes", "no"]

# List of sneakers and their prices

sneakers = {
    "\nAlexander McQueen Oversized Sneaker": 550,
    "\nBalenciaga Triple S": 900,
    "\nNike Blazer Mid '77": 100,
    "\nSacai x Nike LDWaffle": 580,
    "\nCrocs": 75,
    "\nBirkenstock Boston": 200,
    "\nNike Air Max 90": 120,
    "\nJordan 4 Retro": 350,
    "\nDior Jordan 1 Low": 5000,
    "\nNike SB Dunk Ben & Jerry's": 1100,
}

want_instructions = yes_no("Do you want to know how the price comparison tool functions? (y/n): ")

if want_instructions == "yes":
    print("\nThis price comparison tool is available to help users to make informed"
            "\ndecisions by comparing the cost effectiveness of various different sneakers"
            "\nThis tool allows the user to set the specific budget they have available and"
            "\nshow list of products within that set budget. For each product there will be a"
            "\nexplanation on why that product is value for money")

budget = num_check("\nWhat is your budget for today? $", 50, 5000)

while budget <= 5000:

    if budget < 49:
        print("\nSorry you dont have a high enough budget for any of our products. ")
        increase_budget = string_checker("\nWould you like to increase your budget? (y/n): ", 1, yes_no_list)


        if increase_budget == "yes":
            budget = num_check("\nWhat is your budget for today? $", 50, 5000)
        else:
            break

    else:
        print("\nHere are the sneakers within yor budget.")

print("See ya")







