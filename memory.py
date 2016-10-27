__author__ = 'Srija'
from io1 import *
def calculate_length(string):
    length = 0
    for letter in string:
        length+=1
    return length


class data_structure(object):
    def __init__(self):
        self.user_data=[[]]*2000
        self.forum_data=[None]*500


    def store_details_user(self,registration_details):
        registration_details_list=[]
        value=""
        for letter in registration_details:
            if letter == ',':
                registration_details_list.append(value)
                value = ""
                continue
            value+=letter
        registration_details_list.append(value)
        index=self.hash_function(registration_details_list[2],2000)
        if self.user_data[index] != []:
            return 0,registration_details_list
        else:
            temp=[]
            temp.append(registration_details_list[2])
            temp.append(registration_details_list[1])
            self.user_data[index]=temp
            return 1,registration_details_list


    def get_details_from_api(self,registration_details):
        val,registration_details_list=self.store_details_user(registration_details)
        if val == 1:
            msg = add_UserData(registration_details_list)
            print msg
            return msg
        else:
            print " success!!"
            return "User already registered"


    def hash_function(self,string,size):
        length=calculate_length(string)
        sum=0
        i=0
        while i < length:
            j=0
            product=1
            sub_sum=0
            while j < 4 and (i+j) < length:
                sub_sum+=ord(string[i+j])*product
                product*=256
                j+=1
            sum+=sub_sum
            i+=j
        return sum%size

    def parse_input_string(self,input):
        parsed_input=""
        for letter in input:
            if letter == '\0':
                break
            parsed_input+=letter
        print parsed_input
        return parsed_input

    def get_details_initial(self):
        user_data_lists=get_UserDatatoMemory()
        for user_data_list in user_data_lists:
                user=[]
                user.append(self.parse_input_string(user_data_list[2]))
                user.append(self.parse_input_string(user_data_list[1]))
                index=self.hash_function(user[0],2000)
                self.user_data[index]=user


    def check_login_details(self,login_details):
        user_id=""
        password=""
        cnt=0
        for letter in login_details:
            if letter == ',':
                cnt=1
                continue
            if cnt == 1:
                password+=letter
            else:
                user_id+=letter
        index=self.hash_function(user_id,2000)
        if self.user_data[index]!=None:
            if self.user_data[index][0] == user_id:
                if self.user_data[index][1] == password :
                    return 1
        return 0

    def add_forum(self,forum_details):
        forum_data_list=[]
        value=""
        for letter in forum_details:
            if letter == ',':
                forum_data_list.append(value)
                value = ""
                continue
            value+=letter
        forum_data_list.append(value)
        index=self.hash_function(forum_data_list[0],500)
        if self.forum_data[index]!=None:
            return 0
        else:
            self.forum_data[index]=forum_data_list[0]
            msg=addForum(forum_data_list)
            return msg

    def add_forum_initial(self):
        forum_list=get_forums()
        for forum in forum_list:
            index=self.hash_function(forum[0],500)
            self.forum_data[index]=forum[0]
        forum_data_list=[]
        for forum in self.forum_data:
            if forum!=None:
                forum_data_list.append(forum)
        return forum_data_list




    def add_question(self,question_details):
        print question_details
        question_details_list=[]
        value=""
        for letter in question_details:
            if letter == ',':
                question_details_list.append(value)
                value = ""
                continue
            value+=letter
        question_details_list.append(value)
        print question_details_list
        index=self.hash_function(question_details_list[0],500)
        if self.forum_data[index]!=None:
            questions_list=retrieve_Que_forum(question_details_list[0])
            for question in questions_list:
                #question=self.parse_input_string(question)
                if question==question_details_list[1]:
                    return " Question already exists"
            msg=add_queToForum(question_details_list[0],question_details_list[1])
            return msg
        else:
            return " Forum does not exist"


    def retrieve_questions(self,forum_name):
        questions_list=retrieve_Que_forum(forum_name)
        if questions_list:
            return questions_list
        else:
            return " No questions in forum"

    def add_answer_to_question(self,forum_name,question_in_forum,answer):
        index=self.hash_function(forum_name,500)
        if self.forum_data[index] == forum_name:
            questions_list=retrieve_Que_forum(forum_name)
            for question in questions_list:
                if question == question_in_forum:
                    msg=add_anstoQue_forum(forum_name,question_in_forum,answer)
                    return msg
            return " Question does not exist"
        return " Forum does not exist"

    def retrieve_answers(self,forum_name,question_in_forum):
        index=self.hash_function(forum_name,500)
        if self.forum_data[index] == forum_name:
            question_list=retrieve_Que_forum(forum_name)
            for question in question_list:
                if question == question_in_forum:
                    answers_list=retrive_ansToQue_forum(forum_name,question_in_forum)
                    return answers_list
            return " Question does not exist"
        return " Forum does not exist"

    def add_sub_forum(self,forum_details):
        sub_forum_details_list=[]
        value=""
        for letter in forum_details:
            if letter == ',':
                sub_forum_details_list.append(value)
                value = ""
                continue
            value+=letter
        sub_forum_details_list.append(value)
        forum_name=sub_forum_details_list[0]
        index=self.hash_function(forum_name,500)
        sub_forum_details_list=sub_forum_details_list[1:]
        if self.forum_data[index] == forum_name:
            sub_forums_list=get_subforums_forum(forum_name)
            for sub_forum in sub_forums_list:
                if sub_forum == sub_forum_details_list [1]:
                    return " Sub forum already exists"
        msg=addsub_forum(forum_name,sub_forum_details_list)
        return msg
    def add_subforum_question(self,sub_forum_question_details):
        sub_forum_que_list=[]
        value=""
        for letter in sub_forum_question_details:
            if letter == ',':
                sub_forum_que_list.append(value)
                value = ""
                continue
            value+=letter
        sub_forum_que_list.append(value)
        msg=add_queToSubforum_forum(sub_forum_que_list[0],sub_forum_que_list[1],sub_forum_que_list[2])
        return msg

    def add_answer_to_subforum(self,sub_forum_answer_details):
        sub_forum_answer_details_list=[]
        value=""
        for letter in sub_forum_answer_details:
            if letter == ',':
                sub_forum_answer_details_list.append(value)
                value = ""
                continue
            value+=letter
        sub_forum_answer_details_list.append(value)
        msg=add_ansToQue_subforum_forum(sub_forum_answer_details_list[0],sub_forum_answer_details_list[1],sub_forum_answer_details_list[2],sub_forum_answer_details_list[3])
        return msg

    def get_sub_forums(self,forum_name):
        sub_forums_list=[]
        sub_forum_details=get_subforums_forum(forum_name)
        #print sub_forum_details
        for sub_forum in sub_forum_details:
            sub_forums_list.append(sub_forum[0])
            #print sub_forum[0]
        # print sub_forums_list
        return sub_forums_list

    def retrieve_answers_subforum(self,forum_name,sub_forum_name,sub_forum_que):
        return retrive_ansListToQue_subforum_forum(forum_name,sub_forum_name,sub_forum_que)


    def retrieve_questions_sub_forum(self,forum_name,sub_forum):
        return retrive_QueSubforum_forum(forum_name,sub_forum)

    def get_forums(self):
        forums_list=[]
        for forum in self.forum_data:
            if forum != None:
                forums_list.append(forum)
        print forums_list
        return forums_list



d=data_structure()

