pattern_size = int(input("Enter the size of the pattern: "))
no_of_row = 0
while no_of_row < pattern_size:
    for dmmy in range(pattern_size):
        print("*", end=" ")
    no_of_row += 1
    print()