def main():
    print_square(2)

def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            #print brick
           print("#", end="")
        print()
main()



