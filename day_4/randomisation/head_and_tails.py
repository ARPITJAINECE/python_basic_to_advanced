import random

print("this game is for head and tails!!!")
random_head_and_tails_number = random.randint(0, 1)
if random_head_and_tails_number == 0:
    print("its heads")
else:
    print("its tails")
