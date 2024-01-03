def main():
    x = int(input("What's x? "))
    print ("x cubed is", cube(x))

def cube(n):
    return pow(n, 3)

main()
