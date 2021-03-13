
age = 10
if(age>=18):
    print("You are an adult")
else:
    print("You are a child ")

name = "enter your name"
if(name=="Gladys"):
    print("gladys is the correct name ")
else:
    print("Gladys is not your name")

list = [1,2,3,4,5,6,7,8,9,10]
print(list)
list.append(11)
list.insert(1,20)
print(list.index(20))
print(list)
for list_item in list:
    print("list item",list_item)

for item in range(20,30):
    print(item)
for letter in "Gladys":
    print(letter)

counter =0
while(counter<3):
    counter +=1
    print("I am running")

trial_counter = 0
trial_limit =3
while(trial_counter<trial_limit):
    trial_counter +=1
    correct_password = "password"
    user_password = input("enter a password")
    if (correct_password == user_password):
        print("Correct password")
    else:
        print("Incorrect password")

