nbr = str(797114)
N = nbr[-3:]
U = nbr[:3]
print(N, U)

for i in range(int(N)):
    nbr = int(U)*13
    U = str(nbr)[-3:]
print(str(nbr)[-3:])