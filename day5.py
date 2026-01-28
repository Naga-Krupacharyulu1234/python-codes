#conditional statement elifand elsif
1.score = int(input())
if score==100:
    print("perfect score")
elif score>=80:
    print("Almost perfect score")
else:
    print("Nice try")
# Update the blanks in the code below to solve the problem

2.r, k = map(int, input().split())

if r>k:
    print("Ram is heavier than Karan")
elif r<k:
    print("Karan is heavier than Ram")
elif r==k:
    print("Ram & Karan have the same weight")

3.a = 0
b = -10

if a >= b:
   print("a is greater or equal to b.")
if a == 0:
   print("a is 0.")
if a <= 5:
   print("a is not more than 5.")
print("Program ends")
