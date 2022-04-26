
# def get_number():
#     return 5
# def set_number(num):
#     number = num 
#     print("From set_number, num is: ", str(num))
#     return number
# num = get_number() 
# set_number(6)
# print("End of program. Num is:", str(num))

# def add_number(num1, num2):
#     val = num1 + num2
#     print("from add_number, val is: ", str(val))

# output = add_number(2, 5) # 7
# print("Output of {} and {} is {}".format(str(2), str(5), output))

# def get_firstname(full_name): #Pheng Yang
#     space = full_name.index(" ")
#     first_name = full_name [:space]
#     return first_name
# my_name = get_firstname("Pheng Yang")
# print("Hello, my name is " + my_name + ".") # Pheng

# names = ["Lucas Phan", "Joe Biden", "Mike Tyson", "Tom Brady", "Kobe Bryant"]
# for name in names: 
#     my_name = get_firstname(name)
#     if my_name == "Tom":
#         print(my_name + " plays football!")
#     elif my_name == "Kobe":
#         print(my_name + " plays basketball!")
#     elif my_name == "Mike":
#         print(my_name + " is into boxing")
#     else: 
#         print(my_name + " is not into sports")

# def pay(wage, hours):  # Original Code
#     if hours <= 40:
#         amount = wage * hours
#     else:
#         amount = (wage * 40) + ((1.5) * wage * (hours - 40))
#     return amount
# hourlyWage = eval(input("Enter the hourly wage: "))
# hoursworked = eval(input("Enter the number of hours worked: "))
# print("Earnings: ${0:,.2f}".format(pay(hourlyWage, hoursworked)))

# def pay(wage, hours): # Adjusted Code
#     if hours <= 40:
#         print("Here!")
#         amount = wage * hours
#     else:
#         amount = (wage * 40) + ((1.5) * wage * (hours - 40))
#     return amount
# hourlyWage = eval(input("Enter the hourly wage: "))
# hoursworked = eval(input("Enter the number of hours worked: "))
# result = pay(hourlyWage, hoursworked)
# print("Earnings: ${0:,.2f}".format(pay(hourlyWage, hoursworked)))

# def isVowelWord (word):
#     word = word.upper()
#     vowel = ('A', 'E', 'I', 'O', 'U')
#     for vowel in vowel:
#         # if vowels not in word:  # can be simplified to this last one
#         #     return False
#         # return True
#         return False if vowel not in word else True  # This one
# word = input("Enter a word: ")
# if isVowelWord (word):
#     print(word, "contains vowel.")
# else:
#     print(word, "does not contain every vowel.")

def main(): 
    x = 2
    print(str(x) + ": function main")
    trivial()
    print(str(x) + ": function main")

def trivial(): 
    x = 3
    print(str(x) + ": function trivial")
main() 
