#A
#Take number from user
numbers = input("Enter numbers separated by spaces: ").split()
#Convert string to integer
numbers = [int(num) for num in numbers] 
print("Numbers:", numbers)
#Identify odd numbers
odd = [i for i in numbers if i % 2 != 0]
print("Odd numbers:", odd)

#B
#list of fruits
fruits = ['apple','banana','orange','cherry','mango']
#Corrected space character
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

#For output
print(f"Original fruit = {fruits}")
print(f"Capitalized fruits = {capitalized_fruits}")