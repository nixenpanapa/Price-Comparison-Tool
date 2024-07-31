

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
    "Alexander McQueen Oversized Sneaker": 550,
    "Balenciaga Triple S": 900,
    "Nike Blazer Mid '77": 100,
    "Sacai x Nike LDWaffle": 580,
    "Crocs": 75,
    "Birkenstock Boston": 200,
    "Nike Air Max 90": 120,
    "Jordan 4 Retro": 350,
    "Dior Jordan 1 Low": 5000,
    "Nike SB Dunk Ben & Jerry's": 1100,
}


want_instructions = yes_no("Do you want to know how the price comparison tool functions? (y/n): ")

if want_instructions == "yes":
    print("\nThis price comparison tool is available to help users to make informed"
            "\ndecisions by comparing the cost effectiveness of various different sneakers"
            "\nThis tool allows the user to set the specific budget they have available and"
            "\nshow list of products within that set budget. For each product there will be a"
            "\nexplanation on why that product is value for money")
    print()

budget = num_check("\nWhat is your budget for today? $", 50, 5000)

# Print the available sneakers within the budget
print("\nHere are the sneakers you can afford with your budget:")
affordable_sneakers = {name: price for name, price in sneakers.items() if price <= budget}

if affordable_sneakers:
    for name, price in affordable_sneakers.items():
        print(f"{name}: ${price}")
else:
    print("Sorry, no sneakers are available within your budget.")













