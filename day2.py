#Day 2: Functions, thier usage and Dictionaries
# *args -> It deals with tuples
# **kwargs -> It deals with dictonary
# Point to note both works as Collector

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

print()
print("############ TASK 2 ############")
# Task 2: WAP to create a function in which the arguements are users and their marks and return three value.
# User with maximum mark, Average_marks, Users below failing marks. Below is sample of output:
# ("Raul": 99),("avg_marks","55"),["Hidan", "Goku", "Timon", "Sasuke", "Saitama"]
def my_result(**kwargs):
    max_marks=()
    failed =[ i for i in kwargs if kwargs[i] < 65 ]
    max_marks=[(i, max(kwargs.values())) for i in kwargs if max(kwargs.values()) == kwargs[i]]
    avg_marks=("avg_marks:", str(sum(kwargs.values())/len(kwargs)))
    return f"{max_marks},{avg_marks},{failed}"

print(my_result(raul=90,Hidan=50,Goku=30,Timon=50,Sasuke=60, Saitama=80))

print()
print("############ TASK 3 ############")
#TASK 3: WAP to traverse the below given dictionary and print every information about the user.

a_dict = [
    {
        "name": "gara",
        "power": "some sand related jutsu",
        "powerlevel": 199,
        "frieds": [
            {
                "name": "Naruto",
                "friend_points": 28,
                "enemies": ["Saitama"] 
            },
            {
                "name": "Boruto",
                "friend_points": 18,
                "enemies": ["Saitama"]
            }
        ]
    },
    {
        "name": "Alex",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Soniya",
            "friend_points": 128,
            "enemies": ["Saitama"] 
            }
        ]
    },
    {
        "name": "King",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Saitama",
            "friend_points": 128,
            "enemies": ["Naruto", "gara", "boruto"] 
            }
        ]
    }
    
]

for i in a_dict:
    print(i, end="\n")