n = int(input("enter your number: "))   # รับค่าจำนวนเต็มบวก n
total = 0

for number in range(1,n+1):   # เริ่มจาก 1 ถึง n
    total += number
    
print("Total number is ", total)