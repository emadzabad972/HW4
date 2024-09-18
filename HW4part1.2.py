# start

friends: int = int(input("how many friends came to danny's? "))

slices: int = int(input("how many pizza slices were ordered? "))

ate = slices // friends
left = slices % friends

print("the number of pizza slices that each of danny's friends ate:", ate)
print("the number of pizza slices left:", left)

# end