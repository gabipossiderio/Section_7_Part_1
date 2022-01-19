number = int(input('Enter the number of lines you want for your Pascal Triangle: '))

for i in range(1, number + 1):
    for j in range(0, number - i + 1):
        print(' ', end='')

    c = 1
    for j in range(1, i + 1):
        print(' ', c, sep='', end='')
        c = c * (i - j) // j
    print()
