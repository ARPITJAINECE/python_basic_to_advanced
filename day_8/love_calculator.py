def love_calculator(name1, name2):
    name1 = name1.lower().strip().replace(" ", "")
    name2 = name2.lower().strip().replace(" ", "")

    combined_names = name1 + name2

    t_count = r_count = u_count = e_count = l_count = o_count = v_count = 0

    for letter in combined_names:
        if letter == "t":
            t_count += 1
        elif letter == "r":
            r_count += 1
        elif letter == "u":
            u_count += 1
        elif letter == "e":
            e_count += 1
        elif letter == "l":
            l_count += 1
        elif letter == "o":
            o_count += 1
        elif letter == "v":
            v_count += 1

    true_score = t_count + r_count + u_count + e_count
    love_score = l_count + o_count + v_count + e_count

    final_score = str(true_score) + str(love_score)

    return final_score


print("Lets find your love score!!!\n")
name1 = input("Enter first name : ")
name2 = input("Enter second name : ")

print(f"Your love score is : {love_calculator(name1,name2)}")
