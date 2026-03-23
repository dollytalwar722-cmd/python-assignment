
# ques 1 wap to chcek whether  a number is positive
a= int(input("enter a number:"))
if a > 0:
     print("positive")
     
# ques 2 wap to print eligible to vote if age is 18or above
age=int(input( " enter your age:"))
if age>=18:
    print("eligible to vote")

    
 # ques 3 check if number is divisible by 7
 num= int(input("enter a number:"))
if num/7:
    print("divisible by 7")

    
  # ques 4 wap to print "pass" if marks are greater than 40
marks = int(input(" enter your marks:"))
if marks>40:
    print("pass")

# ques 5 check number greater than 100
num= int(input( "enter a number:"))
if num>100:
    print("greater number")

    
   # ques 6 display a message if temperature exceeds 45
temperature = int(input("enter the temperature:"  ))
if temperature>45:
    print("hot")

    
# ques 7 check if string length more than 8 characters
text=input("enter a string :"  )
if len(text)>8:
     print("string length is more than 8 characters")
     
 #  ques 8 print logged in if password matches admin123    
password= input("enter password:")
if password=="admin123":
            print("logged in") 

#  ques 9 check if number is multiple of 10
 
num= int(input("enter a number:"))
if num%10==0:
    print("mutliple of 10")
    
# ques 10 print a warning balance is below minimu limit
balance= float(input("enter account balance:"))
minimum=1000
if balance<minimum:
     print("warning balance is below minimum limit")
 # ques 11 check whether the number is even or odd
num=int(input("enter a number:"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")
 # ques 12 find largest of two number
a= int(input("enter  first number:"))
b=int(input("enter second number:"))
if a>b:
    print("largestvalue",a)
else:
    print("largest value",b)
 #ques 13 check whether the person is eligible for driving license
age=int(input("enter your age:"))
if age>=18:
    print("eligible for driving license")
else:
    print("not eligible")   
#ques 14 print pass or fail based on marks
marks = int(input("enter your marks:"))
if marks>40:
    print("pass")
else:
    print("fail")
#ques 15 check whether number is positive or negative
num=int(input("enter a number:"))
if num >0:
     print("positive")
else:
   print("negative")
 
#ques16 check whether the character is vowel or consonant
ch="Y"
if ch=="A":
    print("vowel")
elif ch=="E":
    print("vowel")
elif ch=="I":
    print("vowel")
elif ch=="O":
    print("vowel")
elif ch=="U":
    print("vowel")
else:
    print("consonant")
    
# QUES 17 CHECK IF A YEAR IS LEAP YEAR OR NOT
year= int(input("enter a year:"))
if year%4==0:
    print("year is leap year")
else:
    print(" this year is not leap year")

    
#ques 19  check whether salary is taxable or not
salary=float(input("enter yoour salary:"))
if salary>500000:
    print("salary is taxable")
else:
     print("salary not taxable")    
     


#ques 18 print valid password or invalid password
password=input("enter password:")
if password=="Admin123":
    print("valid password")
else:
    print("invalid pasword")
#ques 20 chcek whether the number is greater than 50 or not
num=int(input("enter a number:"))
if num>50:
     print("number is greater than 50 ")
else:
    print("number is 50 or less")


#ques 21 find largest of three numbers

 a= int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
        if b>c:
            print(b)
        else:
                 print(C)
                 
#ques 22 chcek wehther the number is positive negative or zero
num= int(input("enter a number:"))
if num>=0:
    if num==0:
         print("number is zero")
    else:
        print( "number is psoitive")
else:
    print("number is negative")
    
 #ques 23 assign grades
marks=int(input("enter marks:"))
if marks>=60:
    if marks>=90:
        print("grade a")
else:
      if marks>=75:
          print("grade b")
      else:
          if marks>=60:
                    print("grade c")
                else:
                   print("fail")
# ques 24 check whether a triangle is equilateral,scalene or isosclese
a= int(input("enter side 1:"))
b=int(input("enter side 2:"))
c=int(input("enter side 3:"))
if a==b:
    if a==c:
        print("equilateral triangle")
    else:
        if a==c or b==c:
               print("isoclese triangle")
            else:
                 print("scalene triangle")
#ques 25 Check whether a character is uppercase, lowercase, digit, or special character. 

ch=input("enter a character:")
if ch>='0':
    if ch<='9':
        print("numeric value")
    else:
      if ch<="z":
         print("upper case")
      else:    
        if ch<="z":
            print("lower case")
        else:
            print("special chracter")
else:
    print("Special characters")
    
#26. Calculate electricity bill using slab-wise rates.

         
#ques 27 validate login using username and password
username=input("enter username:")
password=input("enter password:")
if username =="admin":
         if password == "1234":
                 print("loginsuccessful")
else:
    print("wromg password")
   else:
    print("invalid username")

 
 
#ques 28Check student result using marks of 3 subjects.


maths=int(input("enter marks of subject 1:"))
english=int(input("enter marks of subject 2:"))
sst=int(input("enter marks of subject 3:"))
if maths>=33:
    if english>=33:
        if sst>=33:
            print("pass")
        else:
            print("fail in subject3:")
    else:
         print("fail in subject 2:")
else:
    print("fail in subject 1:")
    
#ques 29 find second largest number among three number
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>b:
    if a<c:
        print("second largest number is :",a)
    else:
        if b>c:
          print("Second largest number is :",b)
        else:
            print("second largest number is :",c)
else:
    if b<c:
        print("second largest number is :",c)
    else:
        if a>c:
            print("second largest number is :",a)
        else:
            print("second largest number is :",c)
            
 #check loan eligibiltiy using age salary credit score
age=int(input("enter your age:"))
salary=float(input("enter your salary:"))
credit_score=int(input("enter yoiur credit score:"))
if age>=21:
    if salary>=30000:
        if credit_score>=650:
            print("loan approved")
        else:
            print("low credit score")
    else:
         print("salary too low")
else:
    print("age not eleigibile")

#ques 31 print day name using day number(1-7)
day=int(input("enter day number(1-7):"))
if day==1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wednesday")
elif day==4:
        print("thursday")
elif day==5:
    print("friday")
elif day==6:
    print("saturday")
elif day==7:
    print("sunday")
    
#ques 32 print month name using month number
month=int(input("enter month number(1-12):"))
if month==1:
    print("january")
elif month==2:
    print("february")
elif month==3:
    print("march")
elif month==4:
        print("april")
elif month==5:
    print("may")
elif month==6:
    print("june")
elif month==7:
    print("july")
elif month==8:
    print("august")
elif month==9:
        print("september")
elif month==10:
    print("october")
elif month==11:
    print("november")
elif month==12:
    print("december")    
#ques 33display grade based on percentage
per=float(input("enter percentage:"))
if per>=90:
    print("grade a")
elif per>=75:
    print("grade b")
elif per>=60:
    print("grade c")
elif per>=50:
    print("grade d")
else:
    print("fail")
    
#ques 34display bonus percentage based on experience years
exp=int(input("enter years of experience:"))
if exp>=10:
    print("bonus:20%")
elif exp>=5:
    print("bonus:10%")
elif exp>=2:
    print("bonus:5%")
else:
    print("no bonus")
    
#ques 35 identify traffic signal meaning
signal=input("enter signal color:")
if signal=="red":
    print("stop")
elif signal=="yellow":
    print("wait")
elif signal=="green":
    print("go")
else:
    print("invald signal")
    
#ques 36 categorise temperature as cold warm hot
temp=float(input("enter temperature:"))

temp=float(input("enter temperature:"))
if temp>=45:
    print("very hot")
elif temp>=30:
    print("warm")
elif temp>=10:
    print("cold")
else:
    print("snow")

                 
#ques 37 categorise employee based on salary
salary=float(input("enter salary:"))
if salary<20000:
    print("low salary")
elif salary<=50000:
    print("medium salary")
else:
    print("high salary")
#ques 38print discount percentage based on purchase amount
amount= int(input("enter purchase amount:"))
if amount>=50000:
    print("discount:20%")
elif amount>=20000:
    print("discount:10%")
elif amount>=10000:
    print("discount:5%")
else:
    print("no discount")
#ques 39 identify number type single digit double multi
num=int(input("enternumber:"))
if-9<= num <=9:
    print("single digit")
elif -9 <=num<= -99:
    print("double digit")
else:
    print("multi digit")
#ques 40 assign performance using poor average good excellent
score=int(input("enter your score:"))
if score>=90:
    print("excellent")
elif score>=75:
    print("good")
elif score>=60:
    print("average")
else:
    print("poor")
#ques41 chcek whrther the number is divisble by 5 or 11
num= int(input("enter numbre:"))
if num%5==0 and num%11==0:
    print("divisible by 5 and 11")
else:
    print("not divisible by 5 and 11")
    
             
#ques 42 chcek if person is eligible for loan age>=21 salary>=25000 credit score>=700
age= int(input("enter your age:"))
salary=float(input("enter salary:"))
credit_score=int(input("enter score:"))
if age>=21 and salary>=25000 and credit_score>=700:
    print("loan approved")
else:
    print("not eligible for loan")
#ques 43 validate login using username and password
username=input("enter userename:")
password=input("enter password:")
if username=="Admin" and password=="12345":
    print("login successful")
else:
    print("invalid login")

#ques44 check student pass condition all subjects>=40 agerage >=50
maths=int(input("enter marks of subject 1:"))
english=int(input("enter marks of subject 2:"))
sst=int(input("enter marks of subject 3:"))
avg=(maths+english+sst)/3
if maths>=40 and english>=40 and sst>=40 and avg>=50:
    print("student passed")
else:
    print("failed")
#ques45 check if number lies between 10 and 100
num=int(input("enter number:"))
if num>10 and num<100:
    print("number lies betweeen 10 and 100:")
else:
    print("not in range")
#ques 46 chcek exam eligibilty attendance 75% or medical certificate avaible
attendance=int(input("attendance%:"))
medical=input("enter certificate(yes/no):")
if attendance>=75 or medical =="yes":
               print("eligible for exam")
else:
    print("not eligible for exam")

#ques 47 validate date using conditions
day=int(input("enter day:"))
month=int(input("enter month:"))
if 1<= month<=12:
        if 1 <= day<=31:
          print("valid date")
        else:
            print("invalid day")
else:
    print("invalid month")
       
#ques 48 chcek whether the email format is valid
email=input("enter email:")
if "@" in email and"." in email:
    print("valid email")
else:
    print("invallid")
#ques 49  determine insurance using age health status iincome
age= int(input("enter age"))
health =input("enter health status(good/bad:")
income=int(input("enter income:"))
if age<60 and health =="good" and income>=20000:
    print("eligible for insurnace")
else:
    print("not eligible for insurance")
#ques 50 check leap year using complete leap year logic
year=int(input("enter year:"))
if (year%4==0 and year%100!=0 or year%400==0):
    print("leap year")
else:
    print("not leap year")
    
#ques 51 wap to calculate income tax using slab
#0-250000  no tax
#250001-500000 5%
#500001-1000000 10%
#1000001-1500000 15%
#above 1500001    20%
income= int(input("enter iincome:"))
if income<=250000:
      tax=0
elif income<=5000000:
    tax=income*0.05
elif income<=1000000:
    tax=income*0.10
elif income<=1500000:
    tax=income*0.15
else:
    tax=income*0.20
    print("tax",tax)
    
 #ques 52 create an atm withdrawal program with balance checks
balance=10000
amount=int(input("enter withdrawal amount:"))
if amount<=balance:
    balance=balance-amount
    print("withdrawal successful")
    print("remaining balance:",balance)
else:
    print("insufficient balance")
#ques53 check promotion eligibility using experience and performance
exp=int(input("experinec:"))
performace=input("performance(good/average):")
if exp>=5 and performance=="good":
    print("promoted")
else:
    print("not promoted")

#ques 54  implement grading system suing nested if else
marks=int(input("enter marks:"))
if marks>=50:
    if marks>=90:
        print("grade a")
    elif marks>=75:
        print("grade b")
    else:
        print("grade c")
else:
    print("fail")
#ques 55 validate strong passwordds using multiple conditions
password=input("enter strong password:")
if len(password)>=8 and password!=password.upper() and password!=password.lower() and ("0" in password or"1" in password or"2"in password
or"3" in password or"4" in password or"5" in password or "6" in password or"7" in password or"8" in pasword or "9" in password):
    print("strong password")
else:
    print("weak password")

    #ques 56 calaculte delivery charges based on loaction and order amount
amount=int(input("enter amount:"))
location=input("enter loaction:")
if location=="local":
    if amount>=500:
        print("free delivery")
    else:
        print("delivery charge:50")
else:
      if amount>=1000:
          print("free delivery")
      else:
          print("delivery charge:100")
    
        
                 

    print("Special charcters")
#ques 57 Determine online exam qualification.
attendance=int(input("enter attendance:"))
permission=input("special permission (yes/no):")
if attendance>=75 or permission=="yes":
    print("eligible for online exam")
else:
    print("not eligible fro exam")

#58. Create movie ticket pricing logic based on age & show time.
    #age<122-100
    #age 12-60-200
    #age>60   - 150
    #evening show after 6 pm -50 extra
age=int(input("enter age:"))
time=int(input("enter show time(24-hour format):"))
if age<12:
    price=100
elif age<=60:
    price=200
else:
    price=150
if time>=18:
    price=price+50
    print("ticket price",price)
    
#59. Determine bank account type based on balance.
#balance<10000-basic
#10000-50000-saving
#>50000-premium
if balance<10000:
    print("basic account")
elif balance<=50000:
    print("savings account")
else:
    print("premium")
    
#60. Create a menu-driven program using if–elif–else.
print("1. even/odd")
print("2. addition")
print("3. exit")
choice=int(input("enter your choice:"))
if choice==1:
    num=int(input("enter number:"))
    if num%2==0:
        print("even")
    else:
        print("odd")
elif choice==2:
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    print("sum",a+b)
elif choice==3:
    print("program end")
else:
    print("invalid choice")
                
