correct_password = "password123"
trial_count= 0
count_limit = 3
while (trial_count<count_limit):
    guess_password = input("Enter password")
    trial_count += 1
    if(correct_password==guess_password):
        print("correct password")
        break
    else:
        print("incorrect password")
else:
    print("you have exceeded your trials")


for item in range(1,10):
    print("item ",item)