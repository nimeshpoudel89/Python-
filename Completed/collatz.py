import matplotlib.pyplot as plt



sequence = []
def collatz(n):
    while n>1:
        sequence.append(n)
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n +1
starting_number = int(input("Enter the starting integer: "))
collatz(starting_number)

x = range(len(sequence))
print(f'Sequence is {sequence}.\n Its length is {len(sequence)}.\n Its maximum value is {max(sequence)}.')


plt.plot(x,sequence)

plt.title(f'Collatz(3n + 1) graph of {starting_number}.')
plt.xlabel("Steps")
plt.ylabel("Itterated Result")
plt.show()


""" with open("Text.txt","w") as f:
    for i in sequence:
        f.write(str(i))
        f.write('\n') """




