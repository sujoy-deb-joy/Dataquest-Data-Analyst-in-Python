tup = (1, 2, 3, 4, 5)
for item in tup:
    print(item)
    if item == 4:
        break
else:
    print("No items left.")

print("this line will execute regardless of break or not")