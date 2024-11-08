#ask user for grades

# grade = input("What is your grade: ")
# grades = [grade]

# excellent = 0
# good = 0
# passing = 0
# fail = 0

# continuously ask for grade until negative is inputted
# while int(grade) >= 0:
#     grade = int(input("What is your grade: "))
#     grades.append(str(grade))

# looks through each grade in the list and print if they are either Excellent, Good, Passing, or fail while adding one to the values Excellent, Good, Passing, or fail accordingly

# for grade in grades:
#     if int(grade) >= 90:
#         print("Excellent")
#         excellent = excellent + 1
#     elif int(grade) <= 89 and int(grade) >= 70:
#         print("Good")
#         good = good + 1
#     elif int(grade) <= 69 and int(grade) >= 50:
#         print("Passing")
#         passing = passing + 1
#     elif int(grade) < 50 and int(grade) >= 0:
#         print("Fail")
#         fail = fail + 1

# print("Excellent: " + str(excellent))
# print("Good: " + str(good))
# print("Passing: " + str(passing))
# print("Failing: " + str(fail))




# 

firstnum = int(input("What is your starting number? "))
secondnum = int(input("What is your ending number? "))
numbers = firstnum, secondnum
print(numbers)
for x in range(firstnum, secondnum):
    if x == 10 and x < 10 and x % 2 == 0:
        print("special even number")
        even = ""
        even = even + 1
    elif x < 20 and not x % 2 == 0:
        print("special odd number")
        odd = ""
        odd = odd + 1

print(even)
print(odd)