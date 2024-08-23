


def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main routine goes here
get_int = num_check("What is your budget for today? $",
                    "Please enter an amount more than 75\n",
                    int)
get_cost = num_check("How much are you willing to spend? $",
                     "PLease enter a number more than 75\n",
                     float)
print("You need: {}".format(get_int))
print("It costs: ${}".format(get_cost))