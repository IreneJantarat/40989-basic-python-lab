Num = int(input('Enter Your Loop: 4'))
NumTotal = []
for i in range(Num):
    data = int(input('Enter your Data: '))
    NumTotal += [data]
print(NumTotal)
NumTotal.sort()
print(NumTotal)