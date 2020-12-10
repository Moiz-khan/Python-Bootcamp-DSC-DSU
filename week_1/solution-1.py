name = str(input("Enter Name: "))



for i in range(len(name)):
    for j in range(len(name)):
        if i==j:
            print(name[i], end="")
            
        else:
            print(' ', end="")
            
    print('\n')