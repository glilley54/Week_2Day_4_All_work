# function will take an integer as an argument
def fizzbuzz(input):
    # check if we have received an integer:
    if type(input) != int:
        # return error message
        return "Please enter an integer"
    # check if it is divisible by both:
    elif input % 3 == 0 and input % 5 == 0:
        # return fizzbuzz
        return "fizzbuzz" 
    # check if number is divisible by 3:
    elif input % 3 == 0:
        # return fizz
        return "fizz"
    # check if it is divisible by 5:
    elif input % 5 == 0:
        # return buzz
        return "buzz"
    # else return input as string
    return str(input)