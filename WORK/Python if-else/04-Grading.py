s1 = int(input("คะแนนเก็บ/30: "))
s2 = int(input("คะแนนสอบกลางภาค/30: "))
s3 = int(input("คะแนนสอบปลายภาค/40: "))


allscore = s1 + s2 + s3
print("Total score: ",allscore)

if(allscore >= 80 and allscore <= 100):
    print("A")
elif(allscore >= 75 and allscore <= 79):
    print("B+")
elif(allscore >= 70 and allscore <= 74):
    print("B")
elif(allscore >= 65 and allscore <= 69):
    print("C+")
elif(allscore >= 60 and allscore <= 64):
    print("C")
elif(allscore >= 55 and allscore <= 59):
    print("D+")
elif(allscore >= 50 and allscore <= 54):
    print("D")
elif(allscore <= 49):
    print("F")

