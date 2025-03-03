# Enter a number:5

#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5

n = int(input("Enter a number:"))
for i in range(1, n+1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(j, end="")
    for k in range(2,i+1):
        print(k, end="")
    print()

