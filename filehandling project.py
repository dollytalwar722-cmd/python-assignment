"""
file handling project
This is a console based project 
Library Tracker Pro
member(member_id,member_name,member_Add,member_mobile)
book(book_id,book_name,book_author,qty)
issue(issue_id,member_id,book_id,status,issue_date,return_date)

1.Add member
2.View all member
3- Delete member
4- Add book
5-View books
6-Seach book
7-Issue book
8-Return book
9-View issued books
10-update book               
11-View returned books
12-Fine calculation
13-Exit
"""
#import libraries
import pickle
import os
from datetime import datetime
#method to add member
def addmember():
    file=open('member.bin','ab')
    member_id=input("\n\t enter member_id:")
    member_name=input("\n\t enter member name:")
    member_add=input("\n\t enter member address:")
    member_mobile=input("\n\t enter member mobile:")
    data = [member_id, member_name, member_add, member_mobile]  
    pickle.dump(data, file)
    print("\n\tMember Added Successfully")
    file.close()
    input("Press enter to continue")
    
#method to view all member
def viewallmember():
    file=open('member.bin','rb')
    try:
        while True:
            data=pickle.load(file)
            print("\n\tmember_id:",data[0])
            print("\n\tmember_name:",data[1])
            print("\n\tmember_add:",data[2])
            print("\n\tmember_mobile:",data[3])
    except EOFError:
           print("\n\t Here Is All Member")
    file.close()
    input("\t Press Enter to Continue....")
#method to delete a member:
def deletemember():
    file1=open('member.bin','rb')
    file2=open('temp.bin','wb')
    member_id=input("enter member id to delete:").strip()
    flag=0
    try:
        while True:
            data=pickle.load(file1)
            if data[0].strip()==member_id:
                print("member_name:",data[1])
                print("member_add:",data[2])
                print("member_mobile:",data[3])
                flag=1
            else:
                pickle.dump(data,file2)
    except EOFError:
        if flag==1:
            print("\n\t Member Deleted Successfully")
        else:
            print("\n\t Member Not Found")
    file1.close()
    file2.close()
    os.remove('member.bin')
    os.rename('temp.bin','member.bin')
    input("\t Press Enter To Continue")
                
                

#method to add book
def addbook():
    file=open('book.bin','ab')
    book_id=input("\n\t create book_id:")
    book_name=input("\n\tenter book name:")
    book_author=input("\n\t enter name of author:")
    qty=input("\n\t enter quantity")
    data=[ book_id,book_name,book_author,qty]
    pickle.dump(data,file)
    file.close()
    input("Press Enter To Continue")
# method to view books
def viewbooks():
    file=open('book.bin','rb')
    try:
        while True:
            data=pickle.load(file)
            print("\n\tbook_id:",data[0])
            print("\n\tbook_name:",data[1])
            print("\n\tbook_author:",data[2])
            print("\n\tqty:",data[3])
    except EOFError:
        print("\n\t Here Is All Books")
    file.close()
    input("\t Press Enter To Continue....")
#method to search book
def searchbook():
    file=open('book.bin','rb')
    book_name=input("\n\t enter name of book to search:")
    found=False
    try:
        while True:
            data=pickle.load(file)#one record read
            if book_name.lower() in data[1].lower():
                print("\n book found:",data)
                found=True
    except EOFError:
        pass
    if not found:
        print("Book Not Found")
        
    file.close()
    input("Press Enter To Continue")
#method to issue tthe book
def issuebook():
    file=open('issue.bin','ab')
    issue_id=input("\n\t enter issue id :")
    member_id=input("enter member id:")
    book_id=input("enter book id:")
    status=input("enter status :")
    issue_date=input("enter  issue date:")
    return_date=input("enter return date:")
    data=[issue_id,member_id,book_id,status,issue_date,return_date]
    pickle.dump(data,file)
    
    file.close()
    print("\n\t Booked Issued Successfully")
    input("\t Press Enter To Continue")
#method to return book
def returnbook():
    file1=open('issue.bin','rb')
    file2=open('temp.bin','ab')
    book_id=input("\n\t enter book id to return:")
    found=False
    try:
        while True:
            data=pickle.load(file1)
            if data[2]==book_id and data[3]=='issued':
                data[3]='returned'
                found= True
                print("\t book returned successfully:")
                pickle.dump(data,file2)
    except EOFError:
        pass
    file1.close()
    file2.close()
    os.remove ('issue.bin')
    os.rename('temp.bin','issue.bin')
    if not found:
        print("\n\tBook Not Found")
    input("\n\t Press Enter To Continue")
    
    
# method to view issued books
def viewissuedbook():
    file=open('issue.bin','rb')
    
    found=False
    try:
        while True:
            data=pickle.load(file)
            if data[3]=='issued':
                print("\n\tissue_id:",data[0])
                print("\n\tmember_id:",data[1])
                print("\n\tbook_id:",data[2])
                print("\n\tstatus:",data[3])
                print("\n\tissue_date:",data[4])
                print("\n\treturn_date:",data[5])
                found=True

    except EOFError:
        pass
    if not found:
        print("\n\t  No  Issued Records Found")
    file.close()
    input("Press Enter To Continnue")
# method to update book
def updatebook():
    file1 =open('book.bin','rb')
    file2=open('temp.bin','ab')
    book_id=input("enter book id to update:")
    found=False
    try:
        while True:
            data=pickle.load(file1)
            if data[0]==book_id:
                found=True
                print("\t current data:",data)
                new_name=input("enter new book name:")
                new_author=input("enter new author name:")
                new_qty=input("enter new qty:")
                data=[book_id,new_name,new_author,new_qty]
                print("\n\t book updated succesfully")
                pickle.dump (data,file2)
    except EOFError:
        pass
    file1.close()
    file2.close()
    os.remove('book.bin')
    os .rename('temp.bin','book.bin')
    input("Press Enter To Continue")
                
#method to view returned books
def viewreturnedbook():
    file=open('issue.bin','rb')
    found=False
    try:
        while True:
            data=pickle.load(file)
            if data[3]=='returned':
                print("\n\tissue_id:",data[0])
                print("\n\tmember_id:",data[1])
                print("\n\tbook_id:",data[2])
                print("\n\tstatus:",data[3])
                print("\n\tissue_date:",data[4])
                print("\n\treturn_date:",data[5])
                found=True
    except EOFError:
        pass
    if not found:
        print("\n\t No Retruned Records")
    file.close()
    input("\n\tPress Enter  To Continue")
#method to fine calculation
def finecalculation():
    file=open('issue.bin','rb')
    found=False
    try:
        while True:
            data=pickle.load(file)
            if data[3].lower()=='returned':
                due_date = datetime.strptime(data[5], "%d-%m-%Y")
                today = datetime.today()
                late_days = (today - due_date).days

                if late_days > 0:
                    fine = late_days * 2

                    print("\n\tIssue ID:", data[0])
                    print("\tMember ID:", data[1])
                    print("\tBook ID:", data[2])
                    print("\tLate Days:", late_days)
                    print("\tFine: ₹", fine)

                    found = True
    except EOFError:
        pass

    file.close()

    if not found:
        print("\n\tNo Fine Records")

    input("\n\tPress Enter To Continue")
    
                

    
#dashboard
while True:
        print("\n\t******   Library Tacker Pro  ******")
        print('''
                1.Add member
                2.View all member
                3- Delete member
                4- Add book
                5-View books
                6-Seach book
                7-Issue book
                8-Return book
                9-View issued books
                10-update book               
                11-View returned books
                12-Fine calculation
                13-Exit

                ''')
        ch=int(input("\tEnter your choice:"))
        if ch==13:
           print("\n\t BYE BYE ADMIN!")
           break
        elif ch==1:
          addmember()
        elif ch==2:
            viewallmember()
        elif ch==3:
            deletemember()
        elif ch==4:
            addbook()
        elif ch==5:
            viewbooks()
        elif ch==6:
            searchbook()
        elif ch==7:
            issuebook()
        elif ch==8:
            returnbook()
        elif ch==9:
            viewissuedbook()
        elif ch==10:
            updatebook()
        elif ch==11:
            viewreturnedbook()
        elif ch==12:
            finecalculation()
                
