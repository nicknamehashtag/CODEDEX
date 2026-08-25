print("hello human, welcome to the age calculator and health analyzer")
a=int(input("enter your age:"))
b=2026-a
print("you were born in the year",b)
print("you will be 100 years old in the year",b+100)
print('do you think you\'re going to live till 100??? ')
print("let me analyze your health and tell you if you will live till 100 or not")
c=float(input("enter your weight in kg:"))
d=float(input("enter your height in m:"))
bmi=c/(d**2)
print("your bmi is", bmi)
if bmi<18.5:
    print("you are underweight, you need to eat more and take care of your health")
elif 18.5<bmi<24.9:
    print("you are healthy, keep it up")
elif bmi>24.9:
    print("you are overweight, you need to exercise more and take care of your health")
input("you can add any comments if you wish")
