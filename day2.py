#Day 2: Functions, thier usage and Dictionaries

############### Task 1 ###############
print("############ TASK 1 ############")

# Task 1
#Create a function which returns the sum of all the element provided to it as an arguement. The arguement list will be dynamic.
def arg(*args):
    sum=0
    for i in args:
        if isinstance(i, int):
            sum=sum+i
    print(sum)
arg(1,2,3,4,5,10)

print("######## TASK 2 ##############")