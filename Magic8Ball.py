import random
import time

username = str(input("What is your name : "))
question = str(input("What is your question : "))

ans1 = "Without a doubt"
ans2 = "Yes"
ans3 = "Most Likely"
ans4 = "that I wouldn't count on it"
ans5 = "No"
ans6 = "Very Doubtful"
ans7 = "that I ask that you try again later"
ans8 = "Cannot predict now"

choice = random.randint (1,8)

answer = ""

if choice == 1:
    answer = ans1
elif choice == 2:
    answer = ans2
elif choice == 3:
    answer = ans3
elif choice == 4:
    answer = ans4
elif choice == 5:
    answer = ans5
elif choice == 6:
    answer = ans6
elif choice == 7:
    answer = ans7
else:
    answer = ans8

print()
print("S", end="")
time.sleep(0.3)
print(" h", end="")
time.sleep(0.3)
print(" a", end="")
time.sleep(0.3)
print(" k", end="")
time.sleep(0.3)
print(" i", end="")
time.sleep(0.3)
print(" n", end="")
time.sleep(0.3)
print(" g", end="")
time.sleep(0.3)
print(" .", end="")
time.sleep(0.3)
print(" .", end="")
time.sleep(0.3)
print(" .")
time.sleep(3.3)

print()
print(username, ", my answer is",answer)