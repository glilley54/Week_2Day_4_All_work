#Part 1
#Using single list comprehension, and the following list:
#ages = [5, 15, 64, 27, 84, 26]
#Return a list of only the odd ages.

ages = [5, 15, 64, 27, 84, 26]
odd_ages = [age for age in ages if age %2 != 0]

print(odd_ages)

#Part 2
#Using single list comprehension, and the following list:
#chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
#Return a list with chickens whose name is more than 10 characters
#Return a list of chickens whose name starts with the letter H#

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]

chicken_name_length = [chicken for chicken in chicken_names if len(chicken) > 10]

print(chicken_name_length)


