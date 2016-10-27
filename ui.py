__author__ = 'nithin'


import urllib2
import urllib
import os
from memory import *

from ctypes import *
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
windll.Kernel32.SetConsoleTextAttribute(h, 756)
os.system('cls')

from time import localtime,strftime
from api import *
import time
clear='\n'*5
clear1='\n'*5

LF_FACESIZE = 18
STD_OUTPUT_HANDLE = -11
import ctypes

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 10
font.dwFontSize.X = 10
font.dwFontSize.Y = 18
font.FontFamily = 55
font.FontWeight = 400
font.FaceName = "Lucida Console"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
    handle, ctypes.c_long(False), ctypes.pointer(font))
os.system("mode con:cols=100 lines=1000")
import msvcrt
def passinput():
    print "\t\tEnter Password:",
    ch=''
    i=0
    pas = ''
    pasw=[]
    while True :
        ch=msvcrt.getch()
        if (ord(ch)==12 or ord(ch)==13):
            break
        elif (ord(ch) == 8):
            if(i>0):
                msvcrt.putch('\b')
                msvcrt.putch(' ')
                msvcrt.putch('\b')
                i-=1
                pas=pas[:i]

        elif (ord(ch) in range(37,40)):
            pass
        #elif (ord(ch) in range(32,126)):
        elif (ord(ch)>=65 and ord(ch)<=90) or (ord(ch)>=97 and ord(ch)<=122) or (ord(ch)>=48 and ord(ch)<=57):
            i+=1
            pas=pas+ch
            msvcrt.putch ('*')
        else:
            pas=pas[:i]
    return pas
def blk():
    windll.Kernel32.SetConsoleTextAttribute(h, 752)
    pass
def dbl():
    windll.Kernel32.SetConsoleTextAttribute(h, 753)
def dgn():
    windll.Kernel32.SetConsoleTextAttribute(h, 754)
def dsb():
    windll.Kernel32.SetConsoleTextAttribute(h, 755)
def bro():
    windll.Kernel32.SetConsoleTextAttribute(h, 756)
def dvi():
    windll.Kernel32.SetConsoleTextAttribute(h, 757)
def dol():
    windll.Kernel32.SetConsoleTextAttribute(h, 758)
def lgr():
    windll.Kernel32.SetConsoleTextAttribute(h, 759)
def dgr():
    windll.Kernel32.SetConsoleTextAttribute(h, 760)
def blu():
    windll.Kernel32.SetConsoleTextAttribute(h, 761)
def lgn():
    windll.Kernel32.SetConsoleTextAttribute(h, 762)
def sbl():
    windll.Kernel32.SetConsoleTextAttribute(h, 763)
def red():
    windll.Kernel32.SetConsoleTextAttribute(h, 764)
def pin():
    windll.Kernel32.SetConsoleTextAttribute(h, 765)
def yel():
    windll.Kernel32.SetConsoleTextAttribute(h, 766)
def wht():
    windll.Kernel32.SetConsoleTextAttribute(h, 767)

def loading():
    os.system('cls')
    print "\n"*8
    blu()
    print "\t\t\t\t\t\tLoading"
    print "\t\t\t\t",
    dgn()
    for i in range(20):
        time.sleep(0.05)
        print ".",
    os.system('cls')
def printSucces():
    bro()
    os.system('cls')
    print clear
    print "\t\t\t\t"+"User Succesfully added!!"
    raw_input("\t\t Press Enter to continue....")
def printSucces1():
    bro()
    os.system('cls')
    print clear
    print "\t\t\t\t"+"Succesfully added!!\n"
    raw_input("\t\t\tPress Enter to continue....")
def invalid():
    red()
    os.system('cls')
    print "\n"*5
    print "\t\t\t\t"+"Invalid Input"

    raw_input("\t\t\tPress Enter to continue....")

#------------------------- MAIN MENU----------------------------
def access_menu():
    while True:
        os.system('cls')
        dvi()
        print "\n\n\t\t\t\t   WELCOME TO GROUP-3 FORUMS PORTAL\n\n"

        print "\t------------------------------------MAIN MENU-------------------------------------\n\n"
        dol()
        print "\tChoose an option from the below :\n"
        dbl()
        print "\t\t1. User Management"
        print "\t\t2. Free Users"
        print "\t\t3. Exit"
        print clear
        dgn()
        data=raw_input("\tEnter your choice here  :")
        try:
            if data == '1':
                os.system('cls')
                authentication()
            elif data == '2':
                os.system('cls')
                get_forum_details1()
            elif data == '3':
                exit(0)
            else:
                invalid()
                access_menu()
        except:
            print "Please Enter a Valid Input!!"






#----------------------- FORUM MENU------------------------
def forum_menu(email):
    os.system('cls')
    dvi()
    print "\n\n\t\t\t\t-------------LOGIN PAGE----------------\n\n"
    print "\t\t\t\tWelcome User",email,"...!!!\n"
    dol()
    print "\tChoose an option from the below:\n"
    dbl()
    print "\t\t1. Add a Forum"
    print "\t\t2. Add Question to a forum"
    print "\t\t3. Add answer to a question"
    print "\t\t4. Get forum details"
    print "\t\t5. Sub-Forum options"
    print "\t\t6. Logout!"
    print clear
    dgn()
    data=raw_input("\n\tEnter your choice here  :")
    try:
        if data == '1':
            addForum(email)
        elif data == '2':
            os.system('cls')
            add_que_to_forum(email)
        elif data == '3':
            os.system('cls')
            add_answer_to_a_que_in_a_forum(email)
        elif data=='4':
            os.system('cls')
            get_forum_details(email)
        elif data=='5':
            os.system('cls')
            sub_forum_menu(email)
        elif data=='6':
            os.system('cls')
            authentication()
        else:
            invalid()
            forum_menu(email)
    except:
        print "Please Enter a Valid Input!!"

def sub_forum_menu(email):
    os.system('cls')
    dvi()
    print "\n\n\t\t\t\t-------------SUB-FORUMS PAGE----------------\n\n"
    print "\t\t\t\tWelcome User",email,"...!!!\n"
    dol()
    print "\tChoose an option from the below:\n"
    dbl()
    print "\t\t1. Add a sub-Forum"
    print "\t\t2. Add Question to a sub-forum"
    print "\t\t3. Add answer to a sub-question"
    print "\t\t4. Get sub-forum details"
    print "\t\t5. Back to previous menu"
    print clear
    dgn()
    data=raw_input("\n\tEnter your choice here  :")
    try:
        if data == '1':
            addSubForum(email)
            raw_input("\t\t\t\tPress Enter to continue")
        elif data == '2':
            add_que_to_subforum(email)
            raw_input("\t\t\t\tPress Enter to continue")
        elif data == '3':
            add_answer_to_a_que_in_a_subforum(email)
            raw_input("\t\t\t\tPress Enter to continue")
        elif data=='4':
            os.system('cls')
            get_subforum_details(email)
        elif data=='5':
            os.system('cls')
            forum_menu(email)
        else:
            invalid()
            sub_forum_menu(email)
    except:
        "Please Enter a Valid Input!!"

def get_forum_details(email):
    os.system('cls')
    dgn()
    print "\n\n\t\t\t\t-------------FORUMS PAGE----------------\n\n"
    dol()
    print "\tChoose an option from the below:\n"
    dvi()
    print "\t\t1. View available Forums"
    print "\t\t2. View Questions in a Forum"
    print "\t\t3. View Answers to a Question"
    print "\t\t4. About"
    print "\t\t5. Back to previous Menu"
    print clear
    dol()
    input=raw_input("\n\tEnter your choice here  :")
    bro()
    try:
        if input=='1':
            getForums()
            raw_input("\t\t\t\tPress Enter to continue")
            get_forum_details(email)
        elif input=='2':
            get_list_of_que_in_forum(email)
            raw_input("\t\t\t\tPress Enter to continue")
            get_forum_details(email)
        elif input=='3':
            get_list_of_ans_in_a_forum(email)
            raw_input("\t\t\t\tPress Enter to continue")
            get_forum_details(email)
        elif input=='4':
            red()
            print "\t\tNothing to be shown!"
        elif input=='5':
            forum_menu(email)
        else:
            invalid()
            get_forum_details(email)
    except:
        print "Please Enter a Valid Input!!"


def get_subforum_details(email):
    os.system('cls')
    dgn()
    print "\n\n\t\t\t\t-------------SUB-FORUMS PAGE----------------\n\n"
    dol()
    print "\tChoose an option from the below:\n"
    dvi()
    print "\t\t1. View available Sub-Forums"
    print "\t\t2. View Questions in a Sub-Forum"
    print "\t\t3. View Answers to a Question in a sub-forum"
    print "\t\t4. About"
    print "\t\t5. Back to previous Menu"
    print clear
    dol()
    input=raw_input("\n\tEnter your choice here  :")
    bro()
    try:
        if input=='1':
            getsubForums()
            raw_input("\t\t\t\tPress Enter to continue")
            get_subforum_details(email)
        elif input=='2':
            get_list_of_que_in_subforum(email)
            raw_input("\t\t\t\tPress Enter to continue")
            get_subforum_details(email)
        elif input=='3':
            get_list_of_ans_in_a_subforum(email)
            raw_input("\t\t\t\tPress Enter to continue")
            get_subforum_details(email)
        elif input=='4':
            red()
            print "\t\tNothing to be shown!"
        elif input=='5':
            sub_forum_menu(email)
        else:
            invalid()
            get_subforum_details(email)
    except:
        print "Please Enter a Valid Input!!"


#--------------------------------FREE USER-------------------------
def get_forum_details1():
    os.system('cls')
    dgn()
    print "\n\n\t\t\t\t------------FREE USER MENU--------------\n\n"
    print "\t\t\t\tWelcome to Free User...!!!\n"
    dol()
    print "\tChoose an option from the below:\n"
    dvi()
    print "\t\t1. View available Forums"
    print "\t\t2. View Questions in a Forum"
    print "\t\t3. View Answers to a Question in a Forum"
    print "\t\t4. Go to sub-Forums Menu "
    print "\t\t5. About"
    print "\t\t6. Back to previous Menu"
    print clear
    dol()
    input=raw_input("\n\tEnter your choice here  :")
    bro()
    try:
        if input=='1':
            getForums()
            raw_input("\t\t\t\tPress Enter to continue")
            get_forum_details1()
        elif input=='2':
            get_list_of_que_in_forum(None)
            raw_input("\t\t\t\tPress Enter to continue")
            get_forum_details1()
        elif input=='3':
            get_list_of_ans_in_a_forum(None)
            raw_input("\t\t\t\tPress Enter to continue")
            get_forum_details1()
        elif input=='4':
            get_subforum_details_for_freeUser(None)
            raw_input("\t\t\t\tPress Enter to continue")
            get_forum_details1()
        elif input=='5':
            red()
            print "\t\tNothing to be shown!"
            get_forum_details1()
        elif input=='6':
            access_menu()
        else:
            invalid()
            get_forum_details1()
    except:
        print "Please Enter a Valid Input!!"

def get_subforum_details_for_freeUser(email):
    os.system('cls')
    dgn()
    print "\n\n\t\t\t\t-------------SUB-FORUMS PAGE----------------\n\n"
    dol()
    print "\tChoose an option from the below:\n"
    dvi()
    print "\t\t1. View available Sub-Forums"
    print "\t\t2. View Questions in a Sub-Forum"
    print "\t\t3. View Answers to a Question in a sub-forum"
    print "\t\t4. About"
    print "\t\t5. Back to previous Menu"
    print clear
    dol()
    input=raw_input("\n\tEnter your choice here  :")
    bro()
    try:
        if input=='1':
            getsubForums()
            raw_input("\t\t\t\tPress Enter to continue")
            get_subforum_details_for_freeUser(None)
        elif input=='2':
            get_list_of_que_in_subforum(None)
            get_subforum_details_for_freeUser(None)
        elif input=='3':
            get_list_of_ans_in_a_subforum(None)
            get_subforum_details(email)
        elif input=='4':
            red()
            print "\t\tNothing to be shown!"
        elif input=='5':
            get_forum_details1()
        else:
            invalid()
            get_subforum_details_for_freeUser(None)
    except:
        print "Please Enter a Valid Input!!"


#--------------------MAIN FEATURES-------------------------
def getForums():
    req = urllib2.Request(url='http://localhost:81/viewforums')
    f = urllib2.urlopen(req)
    data=((f.read()))
    data=data[1:-1].split(',')
    j=1
    for i in data:
        print j,'.',i
        j+=1



def replace(char,string):
    result=""
    for each in string:
        if each==char:
            result=result
        else:
            result+=each
    return result




def getKey(key,list1):

    list1=list1[1:-1].split(',')
    j=1
    for i in list1:
        i=replace("'",i)
        if key == j:

            return i
        j+=1
    return "not found"

def getsubForums():
    print "\t\t Select forum name:"
    getForums()
    key=(raw_input("\t\tEnter number :"))
    if key.isdigit():
        key=int(key)
        req = urllib2.Request(url='http://localhost:81/viewforums')
        f = urllib2.urlopen(req)
        data=((f.read()))
        forum_name=getKey(key,data)
        if(forum_name[0]==' '):
            forum_name=forum_name[1:]

        values={'forum_name':forum_name}
        databytes = urllib.urlencode(values)
        req = urllib2.Request(url='http://localhost:81/viewsubforums', data=databytes.encode('utf-8'))
        f = urllib2.urlopen(req)

        data=((f.read()))
        data=data[1:-1].split(',')
        j=1
        for i in data:
            print j,'. ',i
            j+=1
    else:
        red()
        print "\n\t\tEnter valid number"
        time.sleep(2)


def addForum(email):
    bro()
    forum_name=raw_input("\t\tEnter name of forum :")
    #    validity=raw_input("\t\texpiry date :")

    values={'forum_name':forum_name,'validity':strftime("%d-%m-%Y",localtime()),'createddate':strftime("%d-%m-%Y",localtime()),'email':email}
    databytes = urllib.urlencode(values)
    req = urllib2.Request(url='http://localhost:81/add_forum', data=databytes.encode('utf-8'))
    f = urllib2.urlopen(req)
    print("\t\t"+f.read())
    time.sleep(2)
    forum_menu(email)

def addSubForum(email):
    bro()
    print "\t\t Select a forum name..\n"
    getForums()
    key=(raw_input("\t\tEnter number :"))
    if key.isdigit():
        key=int(key)
        req = urllib2.Request(url='http://localhost:81/viewforums')
        f = urllib2.urlopen(req)
        data=((f.read()))
        forum_name=getKey(key,data)
        if(forum_name[0]==' '):
            forum_name=forum_name[1:]
        print "The forum you have selected is ",
        dsb()
        print forum_name
        bro()
        sub_forum_name=raw_input("\t\tEnter a name for the sub-forum:")

        #    validity=raw_input("\t\texpiry date :")

        values={'forum_name':forum_name,'subforum_name':sub_forum_name,'validity':strftime("%d-%m-%Y",localtime()),'createddate':strftime("%d-%m-%Y",localtime()),'email':email}
        databytes = urllib.urlencode(values)
        req = urllib2.Request(url='http://localhost:81/addsubforum', data=databytes.encode('utf-8'))
        f = urllib2.urlopen(req)
        print("\t\t\t"+f.read())
        time.sleep(2)
        sub_forum_menu(email)
    else:
        red()
        print "\n\t\tEnter valid number"
        time.sleep(2)

def add_que_to_forum(email):
    bro()
    print "\t\t Select forum name:"
    getForums()
    key=(raw_input("\t\tEnter number :"))
    if key.isdigit():
        key=int(key)
        req = urllib2.Request(url='http://localhost:81/viewforums')
        f = urllib2.urlopen(req)
        data=((f.read()))
        forum_name=getKey(key,data)
        forum_name=replace(" ",forum_name)
        print "The forum you have selected is ",
        dsb()
        print forum_name
        bro()
        que=raw_input("\t\tenter Question :")

        #    validity=raw_input("\t\tEnter validity of the question in format: DD-MM-YYYY")
        values={'forum_name':forum_name,'question':que,'validity':strftime("%d-%m-%Y",localtime()),'createddate':strftime("%d-%m-%Y",localtime())}
        databytes = urllib.urlencode(values)
        req = urllib2.Request(url='http://localhost:81/add_que_to_a_forum', data=databytes.encode('utf-8'))
        f = urllib2.urlopen(req)
        print("\t\t"+f.read())
        time.sleep(2)
        os.system('cls')
        forum_menu(email)
    else:
        red()
        print "\n\t\tEnter valid number"
        time.sleep(2)

def viewsubforums1(forum_name):
    try:
        data=str(d.get_sub_forums(forum_name))
        data=data[1:-1].split(',')
        j=1
        for i in data:
            print j,'. ',i
            j+=1
    except:
        return "oops!!something went wrong"

def add_que_to_subforum(email):
    bro()
    print "\t\tSelect a forum:"
    getForums()
    key=(raw_input("\t\tEnter number :"))
    if key.isdigit():
        key=int(key)
        req = urllib2.Request(url='http://localhost:81/viewforums')
        f = urllib2.urlopen(req)
        data=((f.read()))
        forum_name=getKey(key,data)
        if(forum_name[0]==' '):
            forum_name=forum_name[1:]
        print "The forum you have selected is ",
        dsb()
        print forum_name
        bro()
        print "\t\tSelect a sub-forum"
        viewsubforums1(forum_name)
        values={'forum_name':forum_name}
        databytes = urllib.urlencode(values)
        req = urllib2.Request(url='http://localhost:81/viewsubforums', data=databytes.encode('utf-8'))
        f = urllib2.urlopen(req)
        data=f.read()
        key=raw_input("\t\tEnter a number:")
        if key.isdigit():
            key=int(key)
            sub_forum_name=getKey(key,data)
            if(sub_forum_name[0]==' '):
                sub_forum_name=sub_forum_name[1:]
            print "The sub-forum you have selected is ",
            dsb()
            print sub_forum_name
            bro()
            que=raw_input("\t\tenter Question :")

            #    validity=raw_input("\t\tEnter validity of the question in format: DD-MM-YYYY")
            values={'forum_name':forum_name,'subforumname':sub_forum_name,'question':que,'validity':strftime("%d-%m-%Y",localtime()),'createddate':strftime("%d-%m-%Y",localtime())}
            databytes = urllib.urlencode(values)
            req = urllib2.Request(url='http://localhost:81/addquetosubforum', data=databytes.encode('utf-8'))
            f = urllib2.urlopen(req)
            print("\t\t"+f.read())
            time.sleep(2)
            sub_forum_menu(email)
    else:
        red()
        print "\n\t\tEnter valid number"
        time.sleep(2)

def get_list_of_que_in_forum(email):
    dvi()
    print "\t\t Select forum name...."
    getForums()
    key=(raw_input("\t\tEnter number :"))
    if key.isdigit():
        key=int(key)
        req = urllib2.Request(url='http://localhost:81/viewforums')
        f = urllib2.urlopen(req)
        data=((f.read()))
        forumname=getKey(key,data)
        forumname=replace(" ",forumname)
        print "The forum you have selected is ",
        dsb()
        print forumname
        bro()
        values={'forum_name':forumname}
        databytes = urllib.urlencode(values)
        req = urllib2.Request(url='http://localhost:81/view_que', data=databytes.encode('utf-8'))
        f = urllib2.urlopen(req)
        data=(f.read())
        #print data
        data=data[1:-1].split(',')
        j=1
        for i in data:
            print j,'. ',i
            j+=1
    else:
        red()
        print "\n\t\tEnter valid number"
        time.sleep(2)


def get_list_of_que_in_subforum(email):
    dvi()
    print "\t\t Select forum name..."
    getForums()
    key=(raw_input("\t\tEnter number :"))
    if key.isdigit():
        key=int(key)
        req = urllib2.Request(url='http://localhost:81/viewforums')
        f = urllib2.urlopen(req)
        data=((f.read()))
        forum_name=getKey(key,data)
        if(forum_name[0]==' '):
            forum_name=forum_name[1:]
        print "The forum you have selected is ",
        dsb()
        print forum_name
        bro()
        print "\t\tSelect a sub-forum"
        viewsubforums1(forum_name)
        values={'forum_name':forum_name}
        databytes = urllib.urlencode(values)
        req = urllib2.Request(url='http://localhost:81/viewsubforums', data=databytes.encode('utf-8'))
        f = urllib2.urlopen(req)
        data=f.read()
        key=raw_input("\t\tEnter a number:")
        if key.isdigit():
            key=int(key)
            sub_forum_name=getKey(key,data)
            if(sub_forum_name[0]==' '):
                sub_forum_name=sub_forum_name[1:]
            print "The sub-forum you have selected is ",
            dsb()
            print sub_forum_name
            bro()
            values={'forum_name':forum_name,'subforumname':sub_forum_name}
            databytes = urllib.urlencode(values)
            req = urllib2.Request(url='http://localhost:81/getquesinsf', data=databytes.encode('utf-8'))
            f = urllib2.urlopen(req)
            data=(f.read())
            #print data

            data=data[1:-1].split(',')
            j=1
            for i in data:
                print j,'. ',i
                j+=1

#            raw_input("\t\t press enter to continue")
    else:
        red()
        print "\n\t\tEnter valid number"
        time.sleep(2)

def add_answer_to_a_que_in_a_subforum(email):
    dbl()
    print "\t\t Select forum name:"
    getForums()
    key=(raw_input("\t\tEnter number :"))
    if key.isdigit():
        key=int(key)
        req = urllib2.Request(url='http://localhost:81/viewforums')
        f = urllib2.urlopen(req)
        data=((f.read()))
        forum_name=getKey(key,data)
        if(forum_name[0]==' '):
            forum_name=forum_name[1:]
        print "The forum you have selected is ",
        dsb()
        print forum_name
        bro()
        print "\t\tSelect a sub-forum"
        viewsubforums1(forum_name)
        values={'forum_name':forum_name}
        databytes = urllib.urlencode(values)
        req = urllib2.Request(url='http://localhost:81/viewsubforums', data=databytes.encode('utf-8'))
        f = urllib2.urlopen(req)
        data=f.read()
        key=raw_input("\t\tEnter a number:")
        if key.isdigit():
            key=int(key)
            sub_forum_name=getKey(key,data)
            if(sub_forum_name[0]==' '):
                sub_forum_name=sub_forum_name[1:]
            print "The subforum you have selected is",\
            dsb()
            print sub_forum_name
            bro()
            print "\n\t\tSelect a question.."
            get_que_in_subforum1(forum_name,sub_forum_name)
            values={'forum_name':forum_name,'subforumname':sub_forum_name}
            databytes = urllib.urlencode(values)
            req = urllib2.Request(url='http://localhost:81/getquesinsf', data=databytes.encode('utf-8'))
            f = urllib2.urlopen(req)
            data=(f.read())
            key=raw_input("\t\tEnter a number:")
            if key.isdigit():
                key=int(key)
                que=getKey(key,data)
                if(que[0]==' '):
                    que=que[1:]
                print "The question you have selected is ",\
                dsb()
                print que
                bro()
                ans = raw_input("\t\tEnter the answer :")
                values = {'forum_name':forum_name,'subforumname':sub_forum_name,'question':que,'answer':ans,'createddate':strftime("%d-%m-%Y",localtime())}
                databytes = urllib.urlencode(values)
                req = urllib2.Request(url='http://localhost:81/addanstosubforum', data=databytes.encode('utf-8'))
                f = urllib2.urlopen(req)
                print("\t\t"+f.read())
                time.sleep(2)
                sub_forum_menu(email)
    else:
        red()
        print "\n\t\tEnter valid number"
        time.sleep(2)

def add_answer_to_a_que_in_a_forum(email):
    dbl()
    print "\t\t Select forum name...."
    getForums()
    key=(raw_input("\t\tEnter number :"))
    if(key.isdigit()):
        key=int(key)
        req = urllib2.Request(url='http://localhost:81/viewforums')
        f = urllib2.urlopen(req)
        data=((f.read()))
        f_name=getKey(key,data)
        f_name=replace(" ",f_name)
        print "The forum you have selected is ",
        dsb()
        print f_name
        bro()
        print "\t\tSelect a Question"
        get_ques1(f_name)
        values={'forum_name':f_name}
        databytes = urllib.urlencode(values)
        req = urllib2.Request(url='http://localhost:81/view_que', data=databytes.encode('utf-8'))
        f = urllib2.urlopen(req)
        data=(f.read())
        key=(raw_input("\n\t\tEnter a number:"))
        if(key.isdigit()):
            key=int(key)

            que=getKey(key,data)

            if(que[0]==' '):
                que=que[1:]
            print "The question you have selected is",\
            dsb()
            print que
            bro()
            ans = raw_input("\t\tEnter the answer :")
            values = {'forum_name':f_name,'question':que,'answer':ans,'createddate':strftime("%d-%m-%Y",localtime())}
            databytes = urllib.urlencode(values)
            req = urllib2.Request(url='http://localhost:81/addanswer', data=databytes.encode('utf-8'))
            f = urllib2.urlopen(req)
            print("\t\t"+f.read())
            time.sleep(2)
            forum_menu(email)
    else:
        red()
        print "\n\t\tEnter valid number"
        time.sleep(2)


def get_list_of_ans_in_a_forum(email):
    dvi()
    print "\t\t Select forum name:"
    getForums()
    key=(raw_input("\t\tEnter number :"))
    if key.isdigit():
        key=int(key)
        req = urllib2.Request(url='http://localhost:81/viewforums')
        f = urllib2.urlopen(req)
        data=((f.read()))
        f_name=getKey(key,data)
        f_name=replace(" ",f_name)
        print "The forum you have selected is ",
        dsb()
        print f_name
        bro()
        print "\t\tSelect a Question"
        get_ques1(f_name)
        values={'forum_name':f_name}
        databytes = urllib.urlencode(values)
        req = urllib2.Request(url='http://localhost:81/view_que', data=databytes.encode('utf-8'))
        f = urllib2.urlopen(req)
        data=(f.read())
        key=(raw_input("\n\t\tEnter a number:"))
        if(key.isdigit()):
            key=int(key)

            que=getKey(key,data)

            if(que[0]==' '):
                que=que[1:]
            print "The question you have selected is",
            dsb()
            print que
            bro()
            values = {'forum_name':f_name,'question':que,'createddate':strftime("%d-%m-%Y",localtime())}
            databytes = urllib.urlencode(values)
            req = urllib2.Request(url='http://localhost:81/view_ans', data=databytes.encode('utf-8'))
            f = urllib2.urlopen(req)
            data=(f.read())
            data=data[1:-1].split(',')
            j=1
            for i in data:
                print j,'. ',i
                j+=1
    else:
        red()
        print "\n\t\tEnter valid number"
        time.sleep(2)

def get_list_of_ans_in_a_subforum(email):
    dvi()
    print "\t\t Select forum name:"
    getForums()
    key=(raw_input("\t\tEnter number :"))
    if key.isdigit():
        key=int(key)
        req = urllib2.Request(url='http://localhost:81/viewforums')
        f = urllib2.urlopen(req)
        data=((f.read()))
        forum_name=getKey(key,data)
        if(forum_name[0]==' '):
            forum_name=forum_name[1:]
        print "The forum you have selected is ",
        dsb()
        print forum_name
        bro()
        print "\t\tSelect a sub-forum"
        viewsubforums1(forum_name)
        values={'forum_name':forum_name}
        databytes = urllib.urlencode(values)
        req = urllib2.Request(url='http://localhost:81/viewsubforums', data=databytes.encode('utf-8'))
        f = urllib2.urlopen(req)
        data=f.read()
        key=raw_input("\t\tEnter a number:")
        if key.isdigit():
            key=int(key)
            sub_forum_name=getKey(key,data)
            if(sub_forum_name[0]==' '):
                sub_forum_name=sub_forum_name[1:]
            print "The sub-forum you have selected is",\
            dsb()
            print sub_forum_name
            bro()
            print "\n\t\tSelect a question.."
            get_que_in_subforum1(forum_name,sub_forum_name)
            values={'forum_name':forum_name,'subforumname':sub_forum_name}
            databytes = urllib.urlencode(values)
            req = urllib2.Request(url='http://localhost:81/getquesinsf', data=databytes.encode('utf-8'))
            f = urllib2.urlopen(req)
            data=(f.read())
            key=raw_input("\t\tEnter a number:")
            if key.isdigit():
                key=int(key)
                que=getKey(key,data)
                if(que[0]==' '):
                    que=que[1:]
                print "The Question you hahve selected is ",
                dsb()
                print que
                bro()
                values = {'forum_name':forum_name,'subforumname':sub_forum_name,'question':que,'createddate':strftime("%d-%m-%Y",localtime())}
                databytes = urllib.urlencode(values)
                req = urllib2.Request(url='http://localhost:81/getansinsf', data=databytes.encode('utf-8'))
                f = urllib2.urlopen(req)
                data=(f.read())
                data=data[1:-1].split(',')
                j=1
                for i in data:
                    print j,'. ',i
                    j+=1
    else:
        red()
        print "\n\t\tEnter valid number"
        time.sleep(2)


def get_ques1(forumname):
    try:
        data= str(d.retrieve_questions(forumname))
        data=data[1:-1].split(',')
        j=1
        for i in data:
            print j,'. ',i
            j+=1
    except:
        return "\t\toops!!something went wrong!!"



def get_que_in_subforum1(forumname,sforumname):
    try:
        data= str(d.retrieve_questions_sub_forum(forumname,sforumname))
        data=data[1:-1].split(',')
        j=1
        for i in data:
            print j,'. ',i
            j+=1
    except:
        return "\t\toops!!something went wrong!!"

#-----------USER MANAGEMENT-----------
def authentication():
    os.system('cls')
    dvi()
    print "\n\n\t\t\t\t   WELCOME TO GROUP-3 FORUMS PORTAL\n\n"

    dol()
    print "\n\n\t\t\t\tChoose an option from the below :\n"
    dvi()
    print "\t\t1. Login"
    print "\t\t2. Register if you are NewUser"
    print "\t\t3. Back to previous menu"
    print clear
    dol()
    input = raw_input("\tEnter your choice here  :")

    if input == '1':
        login()
    elif input == '2':
        register()
    elif input=='3':
        access_menu()
    else:
        invalid()

def login():
    bro()
    email=raw_input("\t\tEnter your email id:")

    pword=passinput()
    values = {'email':email,
              'password':pword}
    databytes = urllib.urlencode(values)
    req = urllib2.Request(url='http://localhost:81/login', data=databytes.encode('utf-8'))
    f = urllib2.urlopen(req)
    data=(f.read())
    print data
    if data=='login successful':
        os.system('cls')
        loading()
        forum_menu(email)
    else:
        invalid()
        authentication()


def register():
    dgn()
    uname=raw_input("\t\tEnter name:")
    print "\t\tPassword contains min. 8 characters"
    pword=passinput()

    print "\n\t\t(NOTE: This will be your Username)"
    email=raw_input("\t\tEnter your E-Mail id : ")

    dob=raw_input("\t\tEnter your date of birth(DD-MM-YYYY)\n\t\t")

    num="91"+raw_input("\t\tenter your mobile number : ")
    values = {'username':uname,
              'password':pword,
              'email':email,
              'dob':dob,
              'mob':num
    }
    #print values
    databytes = urllib.urlencode(values)
    req = urllib2.Request(url='http://localhost:81/registration', data=databytes.encode('utf-8'))
    f = urllib2.urlopen(req)
    data=(f.read())
    if data=="User Added SuccessFully":
        dgn()
    else:
        red()
    print "\t\t"+data
    time.sleep(2)
    authentication()
access_menu()