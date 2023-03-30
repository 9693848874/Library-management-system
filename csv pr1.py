import pandas as pd
import matplotlib.pyplot as plt
import datetime
def login():
    un = int(input("Enter username"))
    pwd = int(input("Enter password"))
    df = pd.read_csv(r"E:\PROJECT\users.csv")
    df = df.loc[df["userid"] == un]
    if df.empty:
        print("invalid username given")
        return False
    else:
        df = df.loc[df["password"] == pwd]
        if df.empty:
            print("invalid password")
            return false
        else:
            print("username and passwords are matched successfully")
            return True


def showMenu():
    print("----------------------------------------------------")
    print("            NATIONAL DIGITAL LIBRARY ASSOCIATION               ")
    print("-----------------------------------------------------")
    print("\nPress 1-Add a New Book")
    print("\nPress 2-Search for a Book")
    print("\nPress 3-Delete a Book")
    print("\nPress 4-Show all books")
    print("\nPress 5-Add a New Members")
    print("\nPress 6-Search for a Member")
    print("\nPress 7-Delete a Memer")
    print("\nPress 8-Show all Members")
    print("\nPress 9- issue a Book")
    print("\nPress 10- Return a Book")
    print("\nPress 11-Show all issued  Book")
    print("\nPress 12-Delete a issue Book")
    print("\nPress 13-To view charts")
    print("\nPress 14-To exit")
    choice = int(input("Enter your choice:"))
    return choice

def addNewBook():
    bookid = int(input("enter a book id "))
    title = input("Enter book title")
    author = input("Enter author of the book")
    publisher = input("Enter book publisher")
    edition = input("Enter edition of the book")
    cost = int(input("Enter the cost of the book"))
    category = input("Enter th category of the book")
    bdf = pd.read_csv(r"E:\PROJECT\book.csv")
    n = bdf["bookid"].count()
    bdf.at[n] = [bookid, title, author, publisher, edition, cost, category]
    bdf.to_csv(r"E:\PROJECT\book.csv", index=False)
    print("Book Added Successfully")
    print(bdf)

def addNewmember():
    mid = int(input("Enter a member id :"))
    mname = input("Enter member name :")
    phoneno = int(input("Enter phone number"))
    no_issue = int(input("Enter the no of books"))
    mdf = pd.read_csv(r"E:\PROJECT\member.csv")
    n = mdf["mid"].count()
    mdf.at[n] = [mid, mname, phoneno, no_issue]
    mdf.to_csv(r"E:\PROJECT\member.csv", index=False)
    print("New member added successfully")
    print(mdf)

def issueBooks():
    book_name = input("Enter book name :")
    bdf = pd.read_csv(r"E:\PROJECT\book.csv")
    print(bdf)
    bdf = bdf.loc[bdf["title"] == book_name]
    if bdf.empty:
        print("No book found in the library")
        return
    m_name = input("Enter member name :")
    mdf = pd.read_csv(r"E:\PROJECT\member.csv")
    print(mdf)
    mdf = mdf.loc[mdf["m_name"] == m_name]
    if mdf.empty:
        print("No such members found")
        return
    noofbissued = int(input("Enter number of book issued :"))
    bdf = pd.read_csv(r"E:\PROJECT\issuebooks.csv")
    n = bdf["book_name"].count()
    bdf.at[n] = [book_name, m_name, datetime.date.today(), noofbissued, ""]
    bdf.to_csv(r"E:\PROJECT\issuebooks.csv", index=False)
    print("Book issued Successfully")
    print(bdf)

def searchBook():
    title = input("Enter a book name :")
    bdf = pd.read_csv(r"E:\PROJECT\book.csv")
    df = bdf.loc[bdf["title"]==title]
    if df.empty:
        print("No book found with given code")
    else:
        print("Books details are :")
        print(df)

def deleteBook():
    bookid = float(input("Enter a book id :"))
    bdf = pd.read_csv(r"E:\PROJECT\book.csv")
    df = bdf.drop(bdf[bdf["bookid"]==bookid].index)
    bdf.to_csv(r"E:\PROJECT\book.csv", index=False)
    print("book deleted successfully")
    print(df)

def showBooks():
    bdf = pd.read_csv(r"E:\PROJECT\book.csv")
    print(bdf)

def searchMember():
    mname = input("Enter a member name :")
    bdf = pd.read_csv(r"E:\PROJECT\member.csv")
    df = bdf.loc[bdf["mname"]== mname]
    if df.empty:
        print("No member found with given name")
    else:
        print("Members details are :")
        print(df)

def deleteMember():
    mid = float(input("Enter a member id :"))
    bdf = pd.read_csv(r"E:\PROJECT\member.csv")
    bdf = bdf.drop(bdf[bdf["mid"]==mid].index)
    bdf.to_csv(r"E:\PROJECT\member.csv", index=False)
    print("Member deleted successfully")

def showMembers():
    bdf = pd.read_csv(r"E:\PROJECT\member.csv")
    print(bdf)

def returnBook():
    m_name = input("Enter a member name :")
    book_name = input("Enter a book name")
    idf = pd.read_csv(r"E:\PROJECT\issuebooks.csv")
    idf = idf.loc[idf["book name"] == book_name]
    if idf.empty:
        print("the book is not issued in records")
    else:
        idf = idf.loc[idf["m_name"]== m_name]
    if idf.empty:
        print("the book is not issued to the member")
    else:
        print("Book can be returned")
        ans = input("Are u sure u want to return the book :")
        if ans.lower() == "yes":
            idf = pd.read_csv(r"E:\PROJECT\issuebooks.csv")
            idf = idf.drop(idf[idf["book name"] == book_name].index)
            idf.to_csv(r"E:\PROJECT\issuebooks.csv", index=False)
            print("Book returned successfully")
        else:
            print("Return operation cancelled")

def showissuedBooks():
    idf = pd.read_csv(r"E:\PROJECT\issuebooks.csv")
    print(idf)

def deleteissuedbooks():
    book_name = input("Enter a book name :")
    bdf = pd.read_csv(r"E:\PROJECT\issuebooks.csv")
    bdf = bdf.drop(bdf[bdf["book name"]== book_name].index)
    bdf.to_csv(r"E:\PROJECT\issuebooks.csv", index=False)
    print("deleted issued books successfully")
    print(bdf)

def showcharts():
    print("Press 1 - Books and their cost")
    print("Press 2 - number of books issued by members")
    ch = int(input("Enter your choice"))
    if ch == 1:
        df = pd.read_csv(r"E:\PROJECT\book.csv")
        df = df[["title", "cost"]]
        df.plot("title", "cost", kind='bar')
        plt.xlabel('title----->')
        plt.ylabel('cost---->')
        plt.show()

    if ch == 2:
        df = pd.read_csv(r"E:\PROJECT\issuebooks.csv")
        df = df[["number of books issued by members", "m_name"]]
        df.plot(kind='bar', color='red')
        plt.show()
if login():
    while True:
        ch = showMenu()
        if ch == 1:
            addNewBook()
        elif ch ==5:
            addNewmember()
        elif ch ==9:
            issueBooks()
        elif ch == 2:
            searchBook()
        elif ch == 3:
            deleteBook()
        elif ch == 4:
            showBooks()
        elif ch == 6:
            searchMember()
        elif ch == 7:
            deleteMember()
        elif ch == 8:
            showMembers()
        elif ch == 9:
            returnBook()
        elif ch == 11:
            showissuedBooks()
        elif ch == 12:
            deleteissuedbooks()
        elif ch == 13:
            showcharts()
        elif ch == 14:

            break
