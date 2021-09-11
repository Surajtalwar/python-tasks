# Day 1: Basic constructs like data structure and loops[for and while]

#### Task 1 STRING & INT ####
print("####### String Length #######")
s = 'my string' #Let's try to find the length of string
result = len(s)
print(result) #9
print("####### INT Iteration #######")
a = 10 # Let's try to print the numbers from 1 to 10

for i in range(1,a+1):
    print(i, end=' ')
print(end='\n')

####### Task 2 LOOP #######
print("####### LOOP #######")
l = [1,2,3,4]
for i in l:
    print(i, end=' ')
print(end='\n')

##### Generate table to 2,3,4 and 5 ######
print("####### TABLE #######")
table = [2,3,4,5]
for i in range(1,11):
    for j in table:
        print(j, "*",i, "=", i*j, " ", end=' ')
    print(end='\n')

######## Gnerate ODD and EVEN numbers #########
print("####### FOR LOOP #######", end = '\n')

even=[]
odd=[]
for i in range(1,21):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("Even:", even)
print("Odd:", odd)

print("####### WHILE LOOP #######", end = '\n')

even=[]
odd=[]
i = 1
while(i<21):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
    i+=1

print("Even:", even)
print("Odd:", odd)

########## FizzBuzz #########

for i in range(1,101):
    if ((i%3 == 0 and i%5 == 0)):
        print("FizzBuzz")
    elif(i%3 == 0):
        print("Fizz")
    elif(i%5 == 0):
        print("Buzz")
    else:
        print(i)

############### Difference between two array and when to use which on ############

# list = [1,2,3,4]             # In this first list we are running loop on the list & it is printing values
# for i in list:          #####  
#     print(i)   #########

# &

# list = [1,2,3,4]              # In this list we printing the values on the basis of their index
# i = 0                        ### We can use this logic when we need to print via index value
# for i in range(len(list)): ##
#     print(list[i])     ######

 

################## ANSWERS ####################

####### String Length #######
# 9
####### INT Iteration #######
# 1 2 3 4 5 6 7 8 9 10 
####### LOOP #######
# 1 2 3 4 
####### TABLE #######
# 2 * 1 = 2   3 * 1 = 3   4 * 1 = 4   5 * 1 = 5   
# 2 * 2 = 4   3 * 2 = 6   4 * 2 = 8   5 * 2 = 10   
# 2 * 3 = 6   3 * 3 = 9   4 * 3 = 12   5 * 3 = 15   
# 2 * 4 = 8   3 * 4 = 12   4 * 4 = 16   5 * 4 = 20   
# 2 * 5 = 10   3 * 5 = 15   4 * 5 = 20   5 * 5 = 25   
# 2 * 6 = 12   3 * 6 = 18   4 * 6 = 24   5 * 6 = 30   
# 2 * 7 = 14   3 * 7 = 21   4 * 7 = 28   5 * 7 = 35   
# 2 * 8 = 16   3 * 8 = 24   4 * 8 = 32   5 * 8 = 40   
# 2 * 9 = 18   3 * 9 = 27   4 * 9 = 36   5 * 9 = 45   
# 2 * 10 = 20   3 * 10 = 30   4 * 10 = 40   5 * 10 = 50   
####### FOR LOOP #######
# Even: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Odd: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
####### WHILE LOOP #######
# Even: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Odd: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# FizzBuzz
# 31
# 32
# Fizz
# 34
# Buzz
# Fizz
# 37
# 38
# Fizz
# Buzz
# 41
# Fizz
# 43
# 44
# FizzBuzz
# 46
# 47
# Fizz
# 49
# Buzz
# Fizz
# 52
# 53
# Fizz
# Buzz
# 56
# Fizz
# 58
# 59
# FizzBuzz
# 61
# 62
# Fizz
# 64
# Buzz
# Fizz
# 67
# 68
# Fizz
# Buzz
# 71
# Fizz
# 73
# 74
# FizzBuzz
# 76
# 77
# Fizz
# 79
# Buzz
# Fizz
# 82
# 83
# Fizz
# Buzz
# 86
# Fizz
# 88
# 89
# FizzBuzz
# 91
# 92
# Fizz
# 94
# Buzz
# Fizz
# 97
# 98
# Fizz
# Buzz