__author__="nithin"

from ui import *
from bottle import route, run, request
from memory import *

d.get_details_initial()
d.add_forum_initial()
@route('/registration',method='POST')
def register1():
    user_details=[]
    try:
        uname=request.POST['username']
        pword=request.POST['password']
        email=request.POST['email']
        dob=request.POST['dob']
        date_format=dob.split('-')
        date=int(date_format[0])
        month=int(date_format[1])
        year=int(date_format[2])

        mob=request.POST['mob']
        print uname,pword,email,dob,mob
        print validate(uname,pword,email,date,month,year,mob)
        res=validate(uname,pword,email,date,month,year,mob)
        print res
        if res=="success":
            # user_details.append(uname)
            # user_details.append(pword)
            # user_details.append(email)
            # user_details.append(str(MB_Date_Compress(date,month,year)))
            # user_details.append(mob)
            msg=d.get_details_from_api(uname+","+pword+","+email+","+str(MB_Date_Compress(date,month,year))+","+mob)
            #msg=get_details(user_details)
            return msg

        else:
            return res
    except:
        return "Invalid Details ..Try again!! "

@route('/login',method='POST')
def login():
    try:
        details=[]
        email=request.POST['email']
        pword=request.POST['password']
        details.append(email)
        details.append(pword)
        val=d.check_login_details(email+","+pword)
        print val
        if val==0:
            return "Invalid Details !!"
        elif val==1:
            return "login successful"
        else:
            return val
    except:
        return "oops!! something went wrong"
def validate(uname,pword,email,day,month,year,mob):

    flag1=0
    if len(uname)>48:
        return "user name exceeded the required number of characters"

    if len(pword)>32 or len(pword)<8:
        return "password is weak"
    if len(email)>156:
        return "email data exceeded"
    if email.find('@') == -1 or email.find('.com')==-1 :
        return "invalid email address !! please enter a valid email !"
    month_set1=[01,03,05,07,8,10,12]
    month_set2=[04,06,9,11]
    if year>2007 or year<1950:
        print "invalid date"
    if month in month_set1 and day>31 or month in month_set2 and day>30:
        return "Invalid Date"
    if year/4==0 and year/100 == 0 and year/400 == 0 and month==2 and day>29:
        return "invalid date"
    if month==2 and day>28:
        return "invalid date"
    if month>12 or day>31:
        return "invalid Date"
    if len(mob)==12:
        for each in mob:
            if each.isdigit() !=1:
                flag1=1
        if flag1==1:
            return "Invalid number"
    if len(mob)!=12:
        return "invalid number"

    else:
        return "success"

@route('/add_forum',method='POST')
def add_forum():
    try:
        forum_details=[]

        forum_name=request.POST['forum_name']
        created_date=request.POST['createddate']
        email=request.POST['email']
        valid_date=request.POST['validity']
        c_date=created_date.split('-')
        v_date=valid_date.split('-')

        res=validate1(forum_name,valid_date,created_date)
        if res=="success":
            # forum_details.append(forum_name)
            # forum_details.append(MB_Date_Compress(int(v_date[0]),int(v_date[1]),int(v_date[2])))
            # forum_details.append(MB_Date_Compress(int(c_date[0]),int(c_date[1]),int(c_date[2])))
            # forum_details.append(email)
            val=d.add_forum(forum_name+","+str(MB_Date_Compress(int(v_date[0]),int(v_date[1]),int(v_date[2])))+","+str(MB_Date_Compress(int(c_date[0]),int(c_date[1]),int(c_date[2])))+","+email)
            if val==0:
                return "forum already exists"
            else:
                return val
                # try:
                # print get_details(user_details)
                #except:
                #    assert True
        else:
            return res
    except:
        return "oops!!something went wrong"

def validate1(forum_name,valid_date,created_date):
    flag=0
    for i in forum_name:
        if i.isalpha() or i.isdigit():
            flag=1
        else:
            flag=0
            break
    if flag!=1:
        return "forum_name should contain only alphabets and numbers"

    else:
        return "success"

@route('/add_que_to_a_forum',method='POST')
def add_que_to_a_forum():
    try:
        forumname=request.POST['forum_name']
        que=request.POST['question']
        val=d.add_question(forumname+","+que)
        return val
    except:
        return "oops!!something went wrong!!"

@route('/addanswer',method='POST')
def add_answer():
    try:
        forumname=request.POST['forum_name']
        que=request.POST['question']
        ans=request.POST['answer']
        return d.add_answer_to_question(forumname,que,ans)
    except:
        return "oops!!something went wrong!!"

@route('/view_que',method='POST')
def get_ques():
    try:
        forumname=request.POST['forum_name']
        return str(d.retrieve_questions(forumname))
    except:
        return "\t\toops!!something went wrong!!"

@route('/view_ans',method='POST')
def get_ans():
    try:
        forumname=request.POST['forum_name']
        que=request.POST['question']
        return str(d.retrieve_answers(forumname,que))
    except:
        return "\t\toops!!something went wrong!!"


@route('/addsubforum',method='POST')
def add_subforum_to_forum():
    #try:
        forumname=request.POST['forum_name']
        sforumname=request.POST['subforum_name']
        created_date=request.POST['createddate']
        validity=request.POST['validity']
        email=request.POST['email']
        c_date=created_date.split('-')
        v_date=validity.split('-')


#        if sforumname in d.get_sub_forums(forumname):
#            return "subforum already exists"
#        else:
        return d.add_sub_forum(forumname+","+sforumname+","+str(MB_Date_Compress(int(c_date[0]),int(c_date[1]),int(c_date[2])))+","+str(MB_Date_Compress(int(v_date[0]),int(v_date[1]),int(v_date[2])))+","+email)
#    except:
#        return "\t\toops!!something went wrong!!"

@route('/addquetosubforum',method='POST')
def add_que_to_subforum():
    try:
        forumname=request.POST['forum_name']
        sforumname=request.POST['subforumname']
        que=request.POST['question']
        return d.add_subforum_question(forumname+","+sforumname+","+que)
    except:
        return "\t\toops!!something went wrong!!"


@route('/addanstosubforum',method='POST')
def add_ans_to_subforum():
    try:

        forumname=request.POST['forum_name']
        sforumname=request.POST['subforumname']
        que=request.POST['question']
        ans=request.POST['answer']
        return d.add_answer_to_subforum(forumname+","+sforumname+","+que+","+ans)

    except:
        return "\t\toops!!something went wrong"

def MB_Date_Compress(day,month,year):
    try:#this gives us the date of 2 bytes...if appox of 20000 would save..nearly 1mb+
        return ( year - 2000 ) * 512 + month * 32 + day  # return number which is to be stored
    except:
        return "invalid date!"


def MB_Date_Decompress(Date):  # Here date is the compressed date which u get from file
    #year, month, day = 0,0,0
    year = 2000 + (Date >> 9)
    month = (Date & 511 ) >> 5
    day = (Date & 31 )
    return [day,month,year]



@route('/viewforums')
def view_forums():
    try:
        list1= d.get_forums()
        print list1
        return str(list1)
    except:
        return "\t\toops!!something went wrong!!"

@route('/viewsubforums',method='POST')
def viewsubforums():
    try:
        forumname=request.POST['forum_name']
        return str(d.get_sub_forums(forumname))
    except:
        return "oops!!something went wrong"

@route('/getquesinsf',method='POST')
def get_que_in_subforum():
    try:
        forumname=request.POST['forum_name']
        sforumname=request.POST['subforumname']
        return str(d.retrieve_questions_sub_forum(forumname,sforumname))
    except:
        return "\t\toops!!something went wrong!!"

@route('/getansinsf',method='POST')
def get_ans_in_sforum():
    try:
        forumname=request.POST['forum_name']
        sforumname=request.POST['subforumname']
        que=request.POST['question']
        return str(d.retrieve_answers_subforum(forumname,sforumname,que))
    except:
        return "\t\toops!!something went wrong!!"
run(host='localhost', port=81, debug=True, reloader=True)