
assignment 5

#1. Print numbers from 1 to 10 using a while loop.
a=1
while a<=10:
    print(a)
    a=a+1
   
#2. Print even numbers from 1 to 20.
a=1
while a<=20:
    if a%2==0:
      print(a)
    a=a+1
#3. Print odd numbers from 1 to 20.
a=1
while a<=20:
        print(a)
        a=a+2
    


#4. Print numbers from 10 to 1 (reverse order).
a=10
while a>=1:
    print(a)
    a=a-1

#5. Print multiplication table of 5 using while loop. 
i=1
while i<=10:
    print("5 x",i,"=",5*i)
    i=i+1
#Find the sum of first 10 natural numbers using while loop.
i=1
sum=0
while i<=10:
    sum=sum+i
    i=i+1
print("sum of first 10 natrual no:",sum)    

#7. Find factorial of a number entered by user.
n=int(input("enter number:"))
count=0
a=1
while a<=n:
    if n%a==0:
        print(a)
    a=a+1

#8. Count number of digits in a given number.
num=int(input("enter number:"))
count=0
while num!=0:
    num=num//10
    count=count+1
print("number of digits:",count)    


#9. Reverse a number using while loop.
num=int(input("enter number"))
rev=0
while num!=0:
     digit=num%10
     rev=rev*10+digit
     num=num//10
print("reveresed number:",rev)     

#10. Check whether a number is palindrome or not using while loop.
num=int(input("Enter number:"))
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if num== rev:
    print("palindrome number")
else:
    print("not palindrome number")
#Part 3 – Pattern Based 
#11. Print pattern: 
* 
** 
*** 
**** 
*****

i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print()
    i=i+1

#12. Print pattern: 
1 
12 
123 
1234 
12345

i=1
while i<=5:
    j=1
    while j<=i:
        print(i, end="")
        j=j+1
    print()
    i=i+1
    

#Part 4 – Logical / Real Scenario 
#13. Ask user to enter password until correct password is entered.
correct_pass="1234"
password=""
while password!=correct_pass:
    password=input("enter password:")
print("access granted")    
#14. Create a number guessing game: 
#• Generate a random number (1–10) 
#• Keep asking user until they guess correctly
import random
number=random.randint(1,10)
guess=0
while guess!=number:
    guess=int(input("guess number 1-10:"))
    if guess<number:
        print("too low")
    elif guess>number:
        print("too high")
print("correct guess:")        
        
#15. Keep taking input numbers until user enters 0, then print total sum.
total=0
num=1
while num!=0:
    num=int(input("enter number(0 to stop):"))
    total=total+num
print("total number is:",total)

#Bonus Challenge (Interview Level) 
#16. Print Fibonacci series up to N terms using while loop.
n=int(input("enter number of terms:"))
a=0
b=1
i=1
while i<=n:
    print(a)
    c=a+b
    a=b
    b=c
    i=i+1

#17. Check whether a number is Armstrong number.
num=int(input("enter number:"))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp//10
if sum==num:
    print("armstong number")
else:
    print("not armstrong number")
    

#18. Print prime numbers between 1 to 50 using while loop.
num=2
while num<=50:
    i=2
    is_prime=True
    while i<num:
        if num%i==0:
            is_prime=False
            break
        i=i+1
    if is_prime:
        print(num)
    num=num+1    
            


