for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range(0,110,10):
    print(j, end=' ')
print()

for k in range(20,0,-1):
    print(k, end=' ')
print()

number_of_stars = int(input("Number of stars? "))
for i in range(number_of_stars): # iterate over the range of the number held by the variable number_of_stars
    print("*", end=" ") # print star, end=" " stays on the same line
print() # move to next line once range has been iterated over

number_of_stars = int(input("Number of stars? "))
for i in range(1, number_of_stars + 1): # iterate from 1 up to and including number_of_stars
    print("*" * i) # print star for each iteration, (notice no end=" " therefore will print each iteration on following line
print() # move to next line once range has been iterated over