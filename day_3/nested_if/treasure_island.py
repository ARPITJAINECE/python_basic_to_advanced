print(
    "welcome to treasure island......\nYour mission is to find the treasure!!!!!!!!!!!!"
)
print(
    r"""
.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
.            _.,.__       .                                   .
.           ((o\\o\))     .                                   .
.     .-.    `  \\``      .    A tropical island              .
.  __(   )___.o"^^".,___  .                                   .
.     ===    ~~~~~~~~     .                                   .
.      ==             ldb .                                   .
.       =                 .                                   .
.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
"""
)
direction = input("Enter the direction : Left or Right ???????????").lower()
if direction == "right":
    print("Game over")
elif direction == "left":
    swim_wait = input("whether you want to swim or wait ?").lower()
    if swim_wait == "swim":
        print("game over")
    elif swim_wait == "wait":
        door = input(
            "which door you want to enter ??? either red, yellow or blue???"
        ).lower()
        if door == "blue" or door == "red":
            print("game over!!!!!!!!!")
        elif door == "yellow":
            print("you won, hurray!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("invalid door....")
    else:
        print("invalid choice....")
else:
    prin