

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

def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
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

while True:
    want_instructions = yes_no("Do you want to know how the price comparison tool functions? ")

    if want_instructions == "yes":
        print("This price comparison tool is available to help users to make informed"
              "\ndecisions by comparing the cost effectiveness of various different sneakers"
              "\nThis tool allows the user to set the specific budget they have available and"
              "\nshow list of products within that set budget. For each product there will be a"
              "\nexplanation on why that product is value for money")

    budget = num_check("What is your budget for today? ")

    if budget < 75:
        print("Sorry you dont have enough money for any of our products")

    if budget >5000:
        print("Sorry that is too much for our store please enter a lower amount"
              "\n(within $5000) ")

    else:
        print("Here are some sneakers within your price range")