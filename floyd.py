rows = int(input('Enter the number of row : '))
count = 1
for i in range(1, rows + 1) :
    for j in range(0, i) :
        print(count, end=' ')
        count += 1
    print()