# def main():
#     first()
#     print(str(4) +": from function main")
# def first():
#     print(str(1) +": from function first")
#     second()
#     print(str(3) +": From function first")
# def second():
#     print(str(2) +": from function second")
# main()

# list1 = ["a", "e", "i", "o", "u"]
# list2 = []
# def f(y):
#     return y.upper()
# for x in list1:
#     print("x: ", x)
#     list2.append(f(x))
# print("List2: ", list2)

# print("List: ", [x.upper() for x in ["a", "e", "i", "o", "u"]])  # Same thing but for all Caps

# def total(arg1, arg2, arg3=10, arg4=20):  # has only 4 slots
#     arg1 = arg1 + 10
#     arg2 = arg2 + 10
#     print("Form within total() arg1: ", arg1)
#     print("Form within total() arg2: ", arg2)
#     return (arg1 ** arg2) + arg3 + arg4 
# arg1 = 2  # needs the arg code in order to operate
# arg2 = 3
# total(arg1=2,arg2=5)

# total(2,3)
# total(2,3,4)
# total(2,3,3,4)
# total(2,3,3,4,5)  # would not work because it does not have a 5th slot


