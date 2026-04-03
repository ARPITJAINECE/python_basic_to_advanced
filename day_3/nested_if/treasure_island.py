print(
    "welcome to treasure island......\nYour mission is to find the treasure!!!!!!!!!!!!"
)
direction = input("Enter the direction : Left or Right ???????????")
if direction.lower() == "right":
    print("Game over")
    exit()
else:
    swim_wait = input("whether you want to swim or wait ?")
    if swim_wait.lower() == "swim":
        print("game over")
    else:
        door = input("which door you want to enter ??? either red, yellow or blue???")
        if door.lower() == "blue" or door.lower() == "red":
            print("game over!!!!!!!!!")
        else:
            print("you won, hurray!!!!!!!!!!!!!!!!!!!!!!!!")
