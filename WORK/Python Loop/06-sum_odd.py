n = int(input("enter your number: "))  # รับค่าจำนวนเต็มบวก n
sum_odd = 0

for number in range(1, n, 2):   # เริ่มจาก 1 ถึง n โดยเพิ่มทีละ 2
    sum_odd += number

print("sum odd: ", sum_odd)
