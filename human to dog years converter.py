# Human to Dog years converter

hu_yr = float(input("Human Years: "))
dog_yr = 0

if hu_yr <= 2:
    dog_yr = hu_yr * 10.5
    print("Dog Years: " + str(dog_yr))
else: 
    dog_yr = ((hu_yr - 2) * 4) + 21
    print("Dog Years: " + str(dog_yr))
