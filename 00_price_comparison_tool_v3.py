

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

            if response >= low and response <= high:
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

# Function to determine the best value for money sneaker

def get_best_value_sneaker(affordable_sneakers):

    # For simplicity, assuming the best value is the lowest price within the budget

    return min(affordable_sneakers.items(), key=lambda item: item[1]['price'])

# main routine goes here

yes_no_list = ["yes", "no"]

# Updated List of sneakers and their prices

# Given dictionary with explanations
sneakers = {
    1: {"name": "Alexander McQueen Oversized Sneaker", "price": 550,},
    2: {"name": "Balenciaga Triple S", "price": 900,},
    3: {"name": "Nike Blazer Mid '77", "price": 100,},
    4: {"name": "Sacai x Nike LDWaffle", "price": 580,},
    5: {"name": "Crocs", "price": 75, "explanation": "Comfortable and affordable option for casual wear."},
    6: {"name": "Birkenstock Boston", "price": 200,},
    7: {"name": "Nike Air Max 90", "price": 120,},
    8: {"name": "Jordan 4 Retro", "price": 350,},
    9: {"name": "Dior Jordan 1 Low", "price": 5000, },
    10: {"name": "Nike SB Dunk Ben & Jerry's", "price": 1100,},
}

want_instructions = yes_no("Do you want to know how the price comparison tool functions? (y/n): ")

if want_instructions == "yes":
    print("\nThis price comparison tool is available to help users to make informed"
          "\ndecisions by comparing the cost effectiveness of various different sneakers"
          "\nThis tool allows the user to set the specific budget they have available and"
          "\nshow list of products within that set budget. The most expensive shoe we"
          "\ncurrently have in stock is the Nike x Dior Jordan 1 low, at a starting price of"
          "\n$5000. For each product within the users budget there will be an assigned number"
          "\nto help the user pick which shoe they are interested in.")
    print()

budget = num_check("\nWhat is your budget for today? $", 50, 5000
)

# Find affordable sneakers
affordable_sneakers = {k: v for k, v in sneakers.items() if v['price'] <= budget}

# Display affordable sneakers
if affordable_sneakers:
    print("\nAffordable sneakers within your budget:")
    for key, sneaker in affordable_sneakers.items():
        print(f"{key}: {sneaker['name']} - ${sneaker['price']}")

# Recommend the best value for money sneaker
    best_value_key, best_value_sneaker = get_best_value_sneaker(affordable_sneakers)
    print(f"\nRecommended as the best value for money: {best_value_sneaker['name']} for ${best_value_sneaker['price']}")
    print(f"Why it's the best value for money: {best_value_sneaker['explanation']}\n")

    # User selection loop
    while True:
        try:
            selected_key = int(input("\nSelect the number of the sneaker you are interested in: "))
            if selected_key in affordable_sneakers:
                selected_sneaker = affordable_sneakers[selected_key]
                print(f"\nYou selected: {selected_sneaker['name']} for ${selected_sneaker['price']}")
                break  # Exit the loop
            else:
                print("\nInvalid selection. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")
else:
    print("\nSorry, no sneakers are available within your budget.")

print("\nThank you for using this price comparison tool.")











