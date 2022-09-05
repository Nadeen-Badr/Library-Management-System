import datetime
from multiprocessing.sharedctypes import Value
import os
from sqlite3 import connect
class LMS:
    def __init__(self,listofbooks,library_name):
        self.listofbooks="listofbooks.txt"
        self.library_name= library_name
        self.books_dict={}
        id=101
        with open(self.listofbooks) as bk:
            content=bk.readlines()
            for line in content:
              
               self.books_dict.update({str(id):{"bookstitle":line.replace("\n",""),"lendername":"","Issuedate":"","Status":"Available"}})
               id=id+1
    def displaybooks(self):    
        print("----------------------------List of Books----------------------------")
        print("Books ID","\t","Title")
        print("---------------------------------------------------------------------")       
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get("bookstitle"), "- [",value.get("Status"),"]")
    
    def issuebooks(self):
        bookid=input("Enter book ID : ")
        currentdate=datetime.datetime.now().strftime("%T-%m_%D %H:%M:%S")
        if bookid in self.books_dict.keys():
            if not self.books_dict[bookid]["Status"]=="Available":
                ## lendDate=self.books_dict[bookid]["IssueDate"]
                #print(f"This book is already issued to"+lendName )
                #print("On " + lendDate)
                print(f"This book is already issued to {self.books_dict[bookid]['lenderName']} \
                   on {self.books_dict[bookid]['IssueDate']}")
                return self.issuebooks()
            elif self.books_dict[bookid]["Status"]=="Available":
                YourName=input("Enter your name: ")
                self.books_dict[bookid]["lenderName"]=YourName
                self.books_dict[bookid]["IssueDate"]=currentdate
                self.books_dict[bookid]["Status"]="Already Issued"
                print("Book Issued Successfully !!! \n")
        else:
            print("Book ID not found ")
            #return self.issuebooks()
    def AddBook(self):
        newbook=input("Enter Book title: ")
        if newbook=="":
            return self.AddBook()
        elif len(newbook) >25:
            print("Book title length is too long")
            return self.AddBook()
        else:
            with open(self.listofbooks,"a") as bk:
                bk.writelines(f"{newbook}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'bookstitle':newbook,'lenderName':"",'IssueDate':"",'Status':"Available"}})
                print(f"This book has been added successfully")
    def book_re(self):
        bookid=input("Enter Book ID: ")
        if bookid in self.books_dict.keys():
            if self.books_dict[bookid]["Status"]=="Available":
                print("This book is already available in library , please check your book ID")
                return self.book_re()
            elif not self.books_dict[bookid]["Status"]=="Available":
                self.books_dict[bookid]["lenderName"]=""
                self.books_dict[bookid]["IssueDate"] =""
                self.books_dict[bookid]["Status"]="Available"
                print("Successfully returned\n")
            else:
                print("book ID is not found")
                
try:
    mylms=LMS("listofbooks.txt","pythonlib")
    press_key_list={"D":"Display Books","I":"Issue Book","A":"Add Book","R":"Return Book","Q":"Quit"}
    key_press=False
    while not (key_press=="q"):
        print(f"\n---------- Welcome---------")
        for key,value in press_key_list.items():
            print("press",key,"to",value)
        key_press=input("Press key: ".lower())
        if key_press=="i":
                print("\n current selection : Issue Book\n")
                mylms.issuebooks()
        elif key_press=="a":
                print("\n current selection Add Book\n")
                mylms.AddBook()
        elif key_press=="d":
                print("\n current selection : Display Books \n")
                mylms.displaybooks()
        elif key_press=="r":
                print("\n current selection: Return Book\n")
                mylms.book_re()
        elif key_press=="q":
                break
        else:
                continue
except Exception as e:
        print("something went wrong please check your input")    
                           
#l=(LMS("listofbooks.txt","pythonlib"))
#print(l.displaybooks())


