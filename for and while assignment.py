#ASSIGNMENT FOR AND WHILE LOOP
#1. Write a program to print numbers from 1 to 100.
for i in range(1,101):
    print(i)
#2. Write a program to print all even numbers between 1 and 50.
for i in range(1,51):
    if i%2==0:
        print(i)
#3. Write a program to print the sum of first n natural numbers.
total=0
n=int(input("enter number:"))
for i in range(1,n+1):
    total=total+i
    print("sum=",total)
    
#4. Write a program to print the multiplication table of a given number.
number=int(input("enter number:"))
for i in range(1,11):
    print(n,"x" ,i,"=",n*i)

#5. Write a program to print all elements of a list using a for loop.
li=[12,34,56,78]
for i in li:
    print(i)
#6. Write a program to count the number of vowels in a string.
string = input("Enter string: ")
count = 0
for ch in string:
    if ch.lower() in "aeiou":
        count += 1
print("Vowels:", count)
#7. Write a program to find the largest number in a list.
li=[12,34,55,67,98]
largest= li[0]
for i in li:
    if i>largest:
        largest=i
        print("largest =",i)
        
#8. Write a program to print all prime numbers between 1 and 100
n=int(input("enter number:"))
count=0
for i in range(2,101):
    if n%i==0:
        print(i)
        count=count+1
print("total factors:",count)
if count==2:
    print("prime")
else:
    print("not prime")


#9. Write a program to calculate the factorial of a number using a for loop.
n=int(input("enter number:"))
count=0
for i in range(1,n+1):
    if n %i==0:
        print(i)
        count=count+1
#10. Write a program to print the reverse of a string using a for loop.
text=input("enter string:")
rev=""
for i in text:
    rev=i+rev
print("reversed string:",rev)
"""
    
#WHILE Loop – Programming Questions 
#11. Write a program to print numbers from 1 to 50 using a while loop.
a=1
while a<=50:
    print(a)
    a=a+1
    
#12. Write a program to print all odd numbers between 1 and 50.
a=1
while a<=50:
    if a%2!=0:
        print(a)
    a=a+1
    
#13. Write a program to calculate the sum of digits of a number.
num=int(input("enter number:"))
sum=0
while num>0:
   digit=num%10
   sum=sum+digit
   num=num//10
print(sum)    

#14. Write a program to reverse a number using a while loop.
num=int(input("enter nummber:"))
rev=0
while num>0:
    digit=num%10
    rev=rev+10+digit
    num=num//10
print("reversed number:",rev)    

#15. Write a program to find the factorial of a number using a while loop.
num=int(input("enter number:"))
i=1
while i<=num:
    if num%i==0:
        print(i)
    i=i+1    
#16. Write a program to keep taking input from the user until the user enters 0.
num=1
while num!=0:
    num=int(input("enter number(0 to stop):"))
#17. Write a program to find the largest digit in a number.
num=int(input("enter number:"))
largest=0
while num>0:
    digit=num%10
    if digit>largest:
        largest=digit
    num=num//10
print("largest digit:",largest)

#18. Write a program to check whether a number is a palindrome.
num=int(input("enter nymber:"))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev+10+digit
    num=num//10
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")

#19. Write a program to print the Fibonacci series up to n terms.
n=int(input("enter number of terms:"))
a=0
b=1
i=1
while i<=n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i=i+1
#20. Write a program to implement a number guessing game using a while loop. 
#Mixed (FOR + WHILE) 
#21. Write a program to print a number pattern using loops.
num=int(input("enter number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
    

#22. Write a program to count the frequency of each character in a string.
text=input("enter string:")
for ch in text:
    count=0
    for c in text:
        if ch==c:
            count=count+1
    print(ch,"=" ,count)    
#23. Write a program to print all Armstrong numbers between 1 and 1000.
a=1
temp=a
sum=0
while a<=1000:
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp//10
if sum==num:
    print(num)
num=num+1
    
#24. Write a program to simulate an ATM menu using a while loop.
balance=1000
while true:
    print("/n atm menu")
    print("1. check balance")
    print("2.deposit money")
    print("3. withdraw money")
    print("4,.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("your balance is:"balance)
    elif choice==2:
        amount=int(input("enter amount to deposit:")
                   balanace=balance+amount
                   print("amount ddposited:")
    elif choice==3:
                 amount=int(input("enter amount to withdraw:")
                  if amount<=balance:
                            balance=balance-amount
                            print("please collect your mooney:")
                   else:
                       print("insufficiennt balanve:")
     elif choice==4:
         print("thank you for using atm:")
         break
     else:
         print("invalid choice")

#25. Write a program to find the GCD of two numbers using loops. greatest commom divsior
a=int(input("enter number:"))
b=int(input("enter number:"))
gcd=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print("gcd=",gcd)
