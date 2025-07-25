n = int(input("enter your number: "))  # รับค่าจำนวนเต็มบวก n
sum_even = 0

for number in range(2, n+1, 2):   # เริ่มจาก 2 ถึง n โดยเพิ่มทีละ 2
    sum_even += number

print("sum even: ", sum_even)
