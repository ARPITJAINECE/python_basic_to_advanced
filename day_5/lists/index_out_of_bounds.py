states_of_india = ["rajasthan", "UP", "MP"]
print(f"states of india are : {states_of_india}")
print(f"first state of india is : {states_of_india[0]}")
print(f"last state in india is : {states_of_india[-1]}")

num_of_states = len(states_of_india)

print(f"number of states in india is : {num_of_states}")
# print(f"last state of india is : {states_of_india[num_of_states]}") # it will give index out of bounds exception
print(f"last state of india is : {states_of_india[num_of_states-1]}")
