__author__ = 'Nishanth'

import struct


def config():
    with open('project.dat','wb') as f:
        f.write(struct.pack('i', (3*1024*1024)))  # start add of forum Data
        f.write(struct.pack('i', (3*1024*1024)))  # next free_space for forum Data
        f.write(struct.pack('i', (3*1024*1024)))  # end add of forum Data
        f.write(struct.pack('i', ((7*1024*1024)/2)))  # next free_space for sub_forum Data
        f.write(struct.pack('i', (4*1024*1024)))  # next free_space for que and ans
        f.write(struct.pack('i', 1024))  # start add of User Data
        f.write(struct.pack('i', 1024))  # add of next free space for User Data
        f.write(struct.pack('i', 1024))  # end add of User Data
        f.seek(512)
        f.write(struct.pack('48s','Nishanth Reddy'))
        f.write(struct.pack('32s','123@123@123'))
        f.seek(1024)
        temp = (3*1024*1024)
        while f.tell() < temp:  # links to User Data
            f.seek(252,1)
            f.write(struct.pack('i',f.tell()+4))
        temp = (7*1024*1024)/2
        while f.tell() < temp:  # links for forums
            f.seek(60, 1)
            f.write(struct.pack('i',f.tell()+4))
        temp = 4194288
        while f.tell() < temp:  # link for sub_forums
            f.seek(52, 1)
            f.write(struct.pack('i',f.tell()+4))
        f.seek(16,1)
        temp = (1024*1024*1024)
        while f.tell() < temp:  # link for que & ans
            f.seek(1020, 1)
            f.write(struct.pack('i',(f.tell()+4)))


def getString(fname):
    for i in range(len(fname)):
        if fname[i] == '\0':
            break
    return fname[:i]


def get_AdminInfo():
    adminInfo = []
    with open('project.dat', 'rb+')as f:
        f.seek(512)
        adminInfo.append(getString(struct.unpack('48s',f.read(48))[0]))
        adminInfo.append(getString(struct.unpack('32s',f.read(32))[0]))
        return adminInfo


def get_freespace_user():
    with open('project.dat', 'rb+')as f:
        f.seek(24)
        freeadd = struct.unpack('i',f.read(4))[0]
        f.seek(freeadd+252)
        nextfreeadd = struct.unpack('i',f.read(4))
        f.seek(24)
        f.write(struct.pack('i', nextfreeadd[0]))
        return freeadd


def get_freespace_forum():
    with open('project.dat', 'rb+') as f:
        f.seek(4)
        freeadd = struct.unpack('i',f.read(4))[0]
        f.seek(freeadd+60)
        nextfreeadd = struct.unpack('i',f.read(4))
        f.seek(4)
        f.write(struct.pack('i',nextfreeadd[0]))
        return freeadd


def get_freespace_sub_forum():
    with open('project.dat', 'rb+') as f:
        f.seek(12)
        freeadd = struct.unpack('i',f.read(4))[0]
        f.seek(freeadd+52)
        nextfreeadd = struct.unpack('i',f.read(4))
        f.seek(12)
        f.write(struct.pack('i',nextfreeadd[0]))
        return freeadd


def get_freespace_que_ans():
    with open('project.dat', 'rb+') as f:
        f.seek(16)
        freeadd = struct.unpack('i',f.read(4))[0]
        f.seek(freeadd+1020)
        nextfreeadd = struct.unpack('i',f.read(4))
        f.seek(16)
        f.write(struct.pack('i',nextfreeadd[0]))
        return freeadd


def add_UserData(list1):
    with open('project.dat', 'rb+')as f:
        var = get_freespace_user()
        f.seek(var)
        f.write(struct.pack('48s',list1[0]))#username
        f.write(struct.pack('32s',list1[1]))# Password
        f.write(struct.pack('156s',list1[2])) # Email
        f.write(struct.pack('4s',list1[3]))#dataof birth
        f.write(struct.pack('12s',list1[4]))#phono
        f.write(struct.pack('i',0))
        f.seek(28)
        f.seek(struct.unpack('i',f.read(4))[0]+252)
        f.write(struct.pack('i', var))
        f.seek(28)
        f.write(struct.pack('i', var))
        return "User Added SuccessFully"


def get_UserDatatoMemory():
    list_UserData = []
    with open('project.dat', 'rb+') as f:
        f.seek(20)
        startadd = struct.unpack('i',f.read(4))[0]
        f.seek(4,1)
        endadd = struct.unpack('i', f.read(4))[0]
        while startadd != endadd:
            f.seek(startadd)
            temp = []
            temp.append(struct.unpack('48s',f.read(48))[0])
            temp.append(struct.unpack('32s',f.read(32))[0])
            temp.append(struct.unpack('156s',f.read(156))[0])
            temp.append(struct.unpack('4s',f.read(4))[0])
            temp.append(struct.unpack('12s',f.read(12))[0])
            startadd = struct.unpack('i', f.read(4))[0]
            list_UserData.append(temp)

        if startadd == endadd:
            f.seek(startadd)
            temp = []
            temp.append(struct.unpack('48s',f.read(48))[0])
            temp.append(struct.unpack('32s',f.read(32))[0])
            temp.append(struct.unpack('156s',f.read(156))[0])
            temp.append(struct.unpack('4s',f.read(4))[0])
            temp.append(struct.unpack('12s',f.read(12))[0])
            list_UserData.append(temp)

    return list_UserData


def get_Userlink(emailid):
    with open('project.dat','rb+')as f:
        f.seek(20)
        startadd = struct.unpack('i',f.read(4))[0]
        f.seek(4,1)
        endadd = struct.unpack('i',f.read(4))[0]
        count = 0
        while startadd!=endadd:
            f.seek(startadd+80)
            tempemail = getString(struct.unpack('156s',f.read(156))[0])
            if tempemail == emailid:
                break
            f.seek(16,1)
            startadd = struct.unpack('i',f.read(4))[0]
        if startadd==endadd:
            f.seek(startadd+80)
            tempemail = getString(struct.unpack('156s',f.read(156))[0])
            if tempemail == emailid:
                return startadd
        return startadd


def addForum(forum_data):
    with open('project.dat', 'rb+') as f:
        var = get_freespace_forum()
        f.seek(var)
        f.write(struct.pack('32s', forum_data[0]))  #forumname
        f.write(struct.pack('4s', forum_data[1]))  #validdate
        f.write(struct.pack('4s', forum_data[2])) #createddate
        f.write(struct.pack('i', get_Userlink(forum_data[3])))#userlink
        temp = get_freespace_sub_forum()
        f.write(struct.pack('i',temp))#link to sub_forums
        f.write(struct.pack('i', 0))#link to end of sub_forums
        temp = get_freespace_que_ans()
        f.write(struct.pack('i',temp))#link to start_que
        f.write(struct.pack('i', 0))#link to end_que
        f.write(struct.pack('i', 0))  #link to next forum
        f.seek(8)
        f.seek(struct.unpack('i', f.read(4))[0]+60)
        f.write(struct.pack('i', var))
        f.seek(8)
        f.write(struct.pack('i', var))
    return "Forum Added"


def addsub_forum(fname,subforum_data):
    with open('project.dat', 'rb+') as f:
        startadd = struct.unpack('i',f.read(4))[0]
        f.seek(4,1)
        endadd = struct.unpack('i',f.read(4))[0]
        f.seek(startadd)
        substart=None
        subend=None


        while startadd != endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(12,1)
                substart = struct.unpack('i',f.read(4))[0]
                subend = struct.unpack('i',f.read(4))[0]
                break
            f.seek(28,1)
            startadd = struct.unpack('i', f.read(4))[0]

        if startadd == endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(12,1)
                substart = struct.unpack('i',f.read(4))[0]
                subend = struct.unpack('i',f.read(4))[0]

        if substart:
            if subend == 0:
                f.seek(substart)
                f.write(struct.pack('32s', subforum_data[0]))#sub_forumname
                f.write(struct.pack('4s', subforum_data[1]))#validdate
                f.write(struct.pack('4s', subforum_data[2]))#createddate
                f.write(struct.pack('i', get_Userlink(subforum_data[3])))#userlink
                temp = get_freespace_que_ans()
                f.write(struct.pack('i',temp))#link to start_que
                f.write(struct.pack('i', 0))#link to end_que
                f.write(struct.pack('i', 0))#link to next sub_forum
                f.seek(startadd+48)
                f.write(struct.pack('i',substart))
                return "sub_forum Added"
            else:
                var = get_freespace_sub_forum()
                f.seek(var)
                f.write(struct.pack('32s', subforum_data[0]))#sub_forumname
                f.write(struct.pack('4s', subforum_data[1]))#validdate
                f.write(struct.pack('4s', subforum_data[2]))#createddate
                f.write(struct.pack('i', get_Userlink(subforum_data[3])))#userlink
                temp = get_freespace_que_ans()
                f.write(struct.pack('i',temp))#link to start_que
                f.write(struct.pack('i', 0))#link to end_que
                f.write(struct.pack('i',0))#link to next sub_forum
                f.seek(subend+52)
                f.write(struct.pack('i',var))
                f.seek(startadd+48)
                f.write(struct.pack('i',var))
                return "sub_forum Added"


def get_forums():
    with open('project.dat', 'rb+') as f:
        foruminfo = []
        startadd = struct.unpack('i',f.read(4))[0]
        f.seek(4,1)
        endadd = struct.unpack('i',f.read(4))[0]

        while startadd != endadd:
            temp = []
            f.seek(startadd)
            temp.append(getString(struct.unpack('32s',f.read(32))[0]))
            temp.append(getString(struct.unpack('4s',f.read(4))[0]))
            temp.append(getString(struct.unpack('4s',f.read(4))[0]))
            useradd = struct.unpack('i',f.read(4))[0]
            tempadd = f.tell()
            f.seek(useradd+80)
            temp.append(getString(struct.unpack('156s', f.read(156))[0]))
            f.seek(tempadd+16)
            startadd = struct.unpack('i',f.read(4))[0]
            foruminfo.append(temp)

        if startadd == endadd:
            temp = []
            f.seek(startadd)
            temp.append(getString(struct.unpack('32s',f.read(32))[0]))
            temp.append(getString(struct.unpack('4s',f.read(4))[0]))
            temp.append(getString(struct.unpack('4s',f.read(4))[0]))
            useradd = struct.unpack('i',f.read(4))[0]
            tempadd = f.tell()
            f.seek(useradd+80)
            temp.append(getString(struct.unpack('156s',f.read(156))[0]))
            foruminfo.append(temp)
            return foruminfo


def get_subforums_forum(fname):
    with open('project.dat', 'rb+') as f:
        startadd = struct.unpack('i',f.read(4))[0]
        f.seek(4,1)
        endadd = struct.unpack('i',f.read(4))[0]
        f.seek(startadd)
        substart=None
        subend=None
        subforuminfo=[]

        while startadd != endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(12,1)
                substart = struct.unpack('i',f.read(4))[0]
                subend = struct.unpack('i',f.read(4))[0]
                break
            f.seek(28,1)
            startadd = struct.unpack('i', f.read(4))[0]

        if startadd == endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(12,1)
                substart = struct.unpack('i',f.read(4))[0]
                subend = struct.unpack('i',f.read(4))[0]

        if substart:
            subforuminfo = []
            while substart != subend:
                temp = []
                f.seek(substart)
                temp.append(getString(struct.unpack('32s',f.read(32))[0]))
                temp.append(getString(struct.unpack('4s',f.read(4))[0]))
                temp.append(getString(struct.unpack('4s',f.read(4))[0]))
                useradd = struct.unpack('i',f.read(4))[0]
                tempadd = f.tell()
                f.seek(useradd+80)
                temp.append(getString(struct.unpack('156s', f.read(156))[0]))
                f.seek(tempadd+8)
                substart = struct.unpack('i',f.read(4))[0]
                subforuminfo.append(temp)

            if substart == subend:
                temp = []
                f.seek(substart)
                temp.append(getString(struct.unpack('32s',f.read(32))[0]))
                temp.append(getString(struct.unpack('4s',f.read(4))[0]))
                temp.append(getString(struct.unpack('4s',f.read(4))[0]))
                useradd = struct.unpack('i',f.read(4))[0]
                tempadd = f.tell()
                f.seek(useradd+80)
                temp.append(getString(struct.unpack('156s',f.read(156))[0]))
                subforuminfo.append(temp)

        return subforuminfo


def add_queToForum(fname, que):
    with open('project.dat', 'rb+') as f:
        startadd = struct.unpack('i',f.read(4))[0]
        f.seek(4,1)
        endadd = struct.unpack('i',f.read(4))[0]
        f.seek(startadd)

        while startadd != endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(20,1)
                questart = struct.unpack('i',f.read(4))[0]
                queend = struct.unpack('i',f.read(4))[0]
                break
            f.seek(28,1)
            startadd = struct.unpack('i', f.read(4))[0]

        if startadd == endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(20,1)
                questart = struct.unpack('i',f.read(4))[0]
                queend = struct.unpack('i',f.read(4))[0]

        if questart:
            length = len(que)
            if queend == 0:
                f.seek(questart)
                f.write(struct.pack('i', length))
                f.write(struct.pack('1000s', que))
                f.write(struct.pack('i',0))  #link to discussion start
                f.write(struct.pack('i',0))  #link to discussion end
                f.seek(8, 1)
                f.write(struct.pack('i', 0))
                f.seek(startadd+56)
                f.write(struct.pack('i', questart))
                return "Question Added"
            else:
                var = get_freespace_que_ans()
                f.seek(var)
                f.write(struct.pack('i', length))
                f.write(struct.pack('1000s', que))
                f.write(struct.pack('i',0))  #link to discussion start
                f.write(struct.pack('i',0))  #link to discussion end
                f.seek(8, 1)
                f.write(struct.pack('i', 0))
                f.seek(queend+1020)
                f.write(struct.pack('i',var))
                f.seek(startadd+56)
                f.write(struct.pack('i',var))
                return "Question Added"
        else:
            return " Forum Not Found"


def retrieve_Que_forum(fname):
    with open('project.dat', 'rb+') as f:
        queList = []
        startadd = struct.unpack('i',f.read(4))[0]
        f.seek(4,1)
        endadd = struct.unpack('i',f.read(4))[0]
        f.seek(startadd)

        while startadd != endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(20,1)
                questart = struct.unpack('i',f.read(4))[0]
                queend = struct.unpack('i',f.read(4))[0]
                break
            f.seek(28,1)
            startadd = struct.unpack('i', f.read(4))[0]

        if startadd == endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(20,1)
                questart = struct.unpack('i',f.read(4))[0]
                queend = struct.unpack('i',f.read(4))[0]
        if queend != 0:
            while questart!=queend :
                f.seek(questart+4)
                queList.append(getString(struct.unpack('1000s', f.read(1000))[0]))
                f.seek(16,1)
                questart = struct.unpack('i',f.read(4))[0]

            if questart==queend :
                f.seek(questart+4)
                queList.append(getString(struct.unpack('1000s',f.read(1000))[0]))
        if queList==[]:
            return " NO questions to display!!"
        else:
            return queList


def add_anstoQue_forum(fname,que,ans):
    with open('project.dat', 'rb+') as f:
        startadd = struct.unpack('i',f.read(4))[0]
        f.seek(4,1)
        endadd = struct.unpack('i',f.read(4))[0]
        f.seek(startadd)

        while startadd != endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(20,1)
                questart = struct.unpack('i',f.read(4))[0]
                queend = struct.unpack('i',f.read(4))[0]
                break
            f.seek(28,1)
            startadd = struct.unpack('i', f.read(4))[0]

        if startadd == endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(20,1)
                questart = struct.unpack('i',f.read(4))[0]
                queend = struct.unpack('i',f.read(4))[0]

        while questart!=queend:
            f.seek(questart+4)
            if que == getString(struct.unpack('1000s',f.read(1000))[0]):
                discussionstart = struct.unpack('i',f.read(4))[0]
                discussionend = struct.unpack('i',f.read(4))[0]
                break
            f.seek(16,1)
            questart = struct.unpack('i',f.read(4))[0]

        if questart == queend:
            f.seek(questart+4)
            if que == getString(struct.unpack('1000s',f.read(1000))[0]):
                discussionstart = struct.unpack('i',f.read(4))[0]
                discussionend = struct.unpack('i',f.read(4))[0]

        if discussionstart==0:
           varadd = get_freespace_que_ans()
           f.seek(varadd)
           length = len(ans)
           if length <= 1024:
                temp = str(length)+'s'
                f.write(struct.pack('i',length))
                f.write(struct.pack(temp,ans))
                temp = f.tell()
                f.seek(questart+1004)
                f.write(struct.pack('i',varadd))
                f.write(struct.pack('i',temp))
                return "Answer Added"
        else:
           f.seek(discussionend)
           length = len(ans)
           if length <= 1024:
                temp = str(length)+'s'
                f.write(struct.pack('i',length))
                f.write(struct.pack(temp,ans))
                temp = f.tell()
                f.seek(questart+1008)
                f.write(struct.pack('i',temp))
                return "Answer Added"


def retrive_ansToQue_forum(fname,que):
    with open('project.dat', 'rb+') as f:
        ansList = []
        startadd = struct.unpack('i',f.read(4))[0]
        f.seek(4,1)
        endadd = struct.unpack('i',f.read(4))[0]
        f.seek(startadd)

        while startadd != endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(20,1)
                questart = struct.unpack('i',f.read(4))[0]
                queend = struct.unpack('i',f.read(4))[0]
                break
            f.seek(28,1)
            startadd = struct.unpack('i', f.read(4))[0]

        if startadd == endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(20,1)
                questart = struct.unpack('i',f.read(4))[0]
                queend = struct.unpack('i',f.read(4))[0]

        while questart!=queend:
            f.seek(questart+4)
            if que == getString(struct.unpack('1000s',f.read(1000))[0]):
                discussionstart = struct.unpack('i',f.read(4))[0]
                discussionend = struct.unpack('i',f.read(4))[0]
                break
            f.seek(16,1)
            questart = struct.unpack('i',f.read(4))[0]

        if questart == queend:
            f.seek(questart+4)
            if que == getString(struct.unpack('1000s',f.read(1000))[0]):
                discussionstart = struct.unpack('i',f.read(4))[0]
                discussionend = struct.unpack('i',f.read(4))[0]

        if discussionstart:
            while discussionstart!=discussionend:
                f.seek(discussionstart)
                length = struct.unpack('i',f.read(4))[0]
                temp = str(length)+'s'
                ansList.append(struct.unpack(temp,f.read(length))[0])
                discussionstart = f.tell()
            print ansList
            return ansList
        else:
            return " No Answer to question Yet!!!!!!!!!"


def add_queToSubforum_forum(fname,subname,que):
    with open('project.dat', 'rb+') as f:
        startadd = struct.unpack('i',f.read(4))[0]
        f.seek(4,1)
        endadd = struct.unpack('i',f.read(4))[0]
        f.seek(startadd)

        while startadd != endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(12,1)
                substart = struct.unpack('i',f.read(4))[0]
                subend = struct.unpack('i',f.read(4))[0]
                break
            f.seek(28,1)
            startadd = struct.unpack('i', f.read(4))[0]

        if startadd == endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(12,1)
                substart = struct.unpack('i',f.read(4))[0]
                subend = struct.unpack('i',f.read(4))[0]

        if substart:
            while substart!=subend:
                f.seek(substart)
                if subname == getString(struct.unpack('32s',f.read(32))[0]):
                    f.seek(12,1)
                    questart = struct.unpack('i', f.read(4))[0]
                    queend = struct.unpack('i', f.read(4))[0]
                    break
                f.seek(20,1)
                substart = struct.unpack('i',f.read(4))[0]
            if substart==subend:
                f.seek(substart)
                if subname == getString(struct.unpack('32s',f.read(32))[0]):
                    f.seek(12,1)
                    questart = struct.unpack('i', f.read(4))[0]
                    queend = struct.unpack('i', f.read(4))[0]
        else:
            return " Sub_forum Not Found"

        if questart:
            length = len(que)
            if queend == 0:
                f.seek(questart)
                f.write(struct.pack('i', length))
                f.write(struct.pack('1000s', que))
                f.write(struct.pack('i',0))  #link to discussion start
                f.write(struct.pack('i',0))  #link to discussion end
                f.seek(8, 1)
                f.write(struct.pack('i', 0))
                f.seek(substart+48)
                f.write(struct.pack('i', questart))
                return "Question Added"
            else:
                var = get_freespace_que_ans()
                f.seek(var)
                f.write(struct.pack('i', length))
                f.write(struct.pack('1000s', que))
                f.write(struct.pack('i',0))  #link to discussion start
                f.write(struct.pack('i',0))  #link to discussion end
                f.seek(8, 1)
                f.write(struct.pack('i', 0))
                f.seek(queend+1020)
                f.write(struct.pack('i', var))
                f.seek(substart+48)
                f.write(struct.pack('i',var))
                return "Question Added"


def retrive_QueSubforum_forum(fname,subname):
    with open('project.dat', 'rb+') as f:
        queList = []
        startadd = struct.unpack('i',f.read(4))[0]
        f.seek(4,1)
        endadd = struct.unpack('i',f.read(4))[0]
        f.seek(startadd)

        while startadd != endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(12,1)
                substart = struct.unpack('i',f.read(4))[0]
                subend = struct.unpack('i',f.read(4))[0]
                break
            f.seek(28,1)
            startadd = struct.unpack('i', f.read(4))[0]

        if startadd == endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(12,1)
                substart = struct.unpack('i',f.read(4))[0]
                subend = struct.unpack('i',f.read(4))[0]

        if substart:
            while substart!=subend:
                f.seek(substart)
                if subname == getString(struct.unpack('32s',f.read(32))[0]):
                    f.seek(12,1)
                    questart = struct.unpack('i', f.read(4))[0]
                    queend = struct.unpack('i', f.read(4))[0]
                    break
                f.seek(20,1)
                substart = struct.unpack('i',f.read(4))[0]
            if substart==subend:
                f.seek(substart)
                if subname == getString(struct.unpack('32s',f.read(32))[0]):
                    f.seek(12,1)
                    questart = struct.unpack('i', f.read(4))[0]
                    queend = struct.unpack('i', f.read(4))[0]
        else:
            return " Sub_forum Not Found"

        while questart!=queend :
            f.seek(questart+4)
            queList.append(getString(struct.unpack('1000s', f.read(1000))[0]))
            f.seek(16,1)
            questart = struct.unpack('i',f.read(4))[0]

        if questart==queend :
            f.seek(questart+4)
            queList.append(getString(struct.unpack('1000s',f.read(1000))[0]))
        if queList==[]:
            return " No questions to display!"
        else:
            return queList


def add_ansToQue_subforum_forum(fname,subname,que,ans):
    with open('project.dat', 'rb+') as f:
        startadd = struct.unpack('i',f.read(4))[0]
        f.seek(4,1)
        endadd = struct.unpack('i',f.read(4))[0]
        f.seek(startadd)

        while startadd != endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(12,1)
                substart = struct.unpack('i',f.read(4))[0]
                subend = struct.unpack('i',f.read(4))[0]
                break
            f.seek(28,1)
            startadd = struct.unpack('i', f.read(4))[0]

        if startadd == endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(12,1)
                substart = struct.unpack('i',f.read(4))[0]
                subend = struct.unpack('i',f.read(4))[0]

        if substart:
            while substart!=subend:
                f.seek(substart)
                if subname == getString(struct.unpack('32s',f.read(32))[0]):
                    f.seek(12,1)
                    questart = struct.unpack('i', f.read(4))[0]
                    queend = struct.unpack('i', f.read(4))[0]
                    break
                f.seek(20,1)
                substart = struct.unpack('i',f.read(4))[0]
            if substart==subend:
                f.seek(substart)
                if subname == getString(struct.unpack('32s',f.read(32))[0]):
                    f.seek(12,1)
                    questart = struct.unpack('i', f.read(4))[0]
                    queend = struct.unpack('i', f.read(4))[0]
        else:
            return "Sub_forum Not Found"
        while questart!=queend:
            f.seek(questart+4)
            if que == getString(struct.unpack('1000s', f.read(1000))[0]):
                discussionstart = struct.unpack('i', f.read(4))[0]
                discussionend = struct.unpack('i', f.read(4))[0]
                break
            f.seek(16,1)
            questart = struct.unpack('i',f.read(4))[0]

        if questart == queend:
            f.seek(questart+4)
            if que == getString(struct.unpack('1000s', f.read(1000))[0]):
                discussionstart = struct.unpack('i', f.read(4))[0]
                discussionend = struct.unpack('i', f.read(4))[0]

        if discussionstart==0:
           varadd = get_freespace_que_ans()
           f.seek(varadd)
           length = len(ans)
           if length <= 1024:
                temp = str(length)+'s'
                f.write(struct.pack('i',length))
                f.write(struct.pack(temp,ans))
                temp = f.tell()
                f.seek(questart+1004)
                f.write(struct.pack('i',varadd))
                f.write(struct.pack('i',temp))
                return "Answer Added"
        else:
           f.seek(discussionend)
           length = len(ans)
           if length <= 1024:
                temp = str(length)+'s'
                f.write(struct.pack('i',length))
                f.write(struct.pack(temp,ans))
                temp = f.tell()
                f.seek(questart+1008)
                f.write(struct.pack('i',temp))
                return "Answer Added"


def retrive_ansListToQue_subforum_forum(fname,subname,que):
    with open('project.dat', 'rb+') as f:
        ansList = []
        startadd = struct.unpack('i',f.read(4))[0]
        f.seek(4,1)
        endadd = struct.unpack('i',f.read(4))[0]
        f.seek(startadd)

        while startadd != endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(12,1)
                substart = struct.unpack('i',f.read(4))[0]
                subend = struct.unpack('i',f.read(4))[0]
                break
            f.seek(28,1)
            startadd = struct.unpack('i', f.read(4))[0]

        if startadd == endadd:
            fname1 = getString(struct.unpack('32s',f.read(32))[0])
            if fname == fname1:
                f.seek(12,1)
                substart = struct.unpack('i',f.read(4))[0]
                subend = struct.unpack('i',f.read(4))[0]

        if substart:
            while substart!=subend:
                f.seek(substart)
                if subname == getString(struct.unpack('32s',f.read(32))[0]):
                    f.seek(12,1)
                    questart = struct.unpack('i', f.read(4))[0]
                    queend = struct.unpack('i', f.read(4))[0]
                    break
                f.seek(20,1)
                substart = struct.unpack('i',f.read(4))[0]
            if substart==subend:
                f.seek(substart)
                if subname == getString(struct.unpack('32s',f.read(32))[0]):
                    f.seek(12,1)
                    questart = struct.unpack('i', f.read(4))[0]
                    queend = struct.unpack('i', f.read(4))[0]
        else:
            return " Sub_forum Not Found"

        while questart!=queend:
            f.seek(questart+4)
            if que == getString(struct.unpack('1000s', f.read(1000))[0]):
                discussionstart = struct.unpack('i', f.read(4))[0]
                discussionend = struct.unpack('i', f.read(4))[0]
                break
            f.seek(16,1)
            questart = struct.unpack('i',f.read(4))[0]

        if questart == queend:
            f.seek(questart+4)
            if que == getString(struct.unpack('1000s', f.read(1000))[0]):
                discussionstart = struct.unpack('i', f.read(4))[0]
                discussionend = struct.unpack('i', f.read(4))[0]

        if discussionstart:
            while discussionstart!=discussionend:
                f.seek(discussionstart)
                length = struct.unpack('i',f.read(4))[0]
                temp = str(length)+'s'
                ansList.append(struct.unpack(temp,f.read(length))[0])
                discussionstart = f.tell()
            return ansList
        else:
            return " No Answer to question Yet!!!!!!!!!"

#config()
#get_AdminInfo()
#add_UserData(['Nishanth2','132@132@132','reddynishanth162@gmail.com','1234','917799219811'])
#get_UserDatatoMemory
#addForum(['animals5','1234','5678','reddynishanth162@gmail.com'])
# i=1
# while i<101:
#     addForum(['animals'+str(i),'1234','5678','reddynishanth162@gmail.com'])
#     i += 1
#print len(get_forums())

#addsub_forum('animals2',['animals2-3','1234','5678','reddynishanth162@gmail.com'])
#get_subforums_forum('animals2')
# i=1
# j=1
# while i<101:
#     j=1
#     while j<101:
#         add_queToForum('animals'+str(i), 'Which is Fav animal'+str(j))
#         j += 1
#     i += 1
#print len(retrieve_Que_forum('animals1'))

#i=1
#j=1
#while i<101:
#    j=1
#    while j<101:
#        k=1
#        while k<11:
#           add_anstoQue_forum('animals'+str(i),'Which is Fav animal'+str(j),'Tiger'+str(k))
#           k += 1
#        j += 1
#    i += 1
#add_queToForum('animals1', 'Which is Fav animal2')
#add_anstoQue_forum('animals1','Which is Fav animal2','Tiger1')
#print retrive_ansToQue_forum('animals1','Which is Fav animal1?')
#add_queToSubforum_forum('animals2','animals2-1', 'Which is Your fav Animal2-3?')
#retrive_QueSubforum_forum('animals2','animals2-1')
#add_ansToQue_subforum_forum('animals2','animals2-1', 'Which is Your fav Animal2-2?','Tiger3')
#retrive_ansListToQue_subforum_forum('animals2','animals2-1', 'Which is Your fav Animal2-2?')