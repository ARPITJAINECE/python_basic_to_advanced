# tuples are immutable

tupl = (
    "blacktea",
    "green",
    "oolong",
)
print(tupl)
# tupl[0] = "abc"
# print(tupl)
more_tea = ("herbal",)

final_tea = tupl + more_tea

print(final_tea)
