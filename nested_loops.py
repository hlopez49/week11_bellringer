#nested loop= a loop within another loop (outer,inner)
#              outer loop:
#                   inner loop:
#for x in range(1,10):
    #print(x)

# puts a space
# for x in range(1,10):
    # print(x, end=" ")


# for x in range(3):
#     for y in range(1,10):
#         print(y, end="")


# for x in range(3):
#     for y in range(1,10):
#         print(y, end="")
#     print()

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of colums: "))
symbol = input("Enter a symbol to use")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()