from spy_details import spy,friends
from steganography.steganography import Steganography
from datetime import datetime
from spy_details import Spy,ChatMessage
import csv


print "Hello!" #welcome msgs for user
print 'Let\'s get started.'
STATUS_MESSAGES = ['Cant talk spychat only','Available','Always busy','At work','in a meeting']

def load_frnd():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)

        for row in reader[4:]:
            if row:
                name = row[0]
                age = (row[2])
                rating = (row[3])
                is_online = [4]
        for row in reader:
            spy = Spy(name,age,rating,is_online)
            spy = Spy(row[0],row[1],row[2],row[3])
            friends.append(spy)


load_frnd()

def load_chats():
        reader = list(csv.reader(chats_data))

        for row in reader[4:]:
            if row:
                name_of_sender = row[0]
                message_sent_to = row[1]
                text = row[2]
                sent_by_me = row[4]
                new_chat = ChatMessage(name_of_sender,message_sent_to,text,sent_by_me)
                chats.append(new_chat)
                cm = ChatMessage(row[0],row[1])
                chats_data.append(cm)

def load_history():

    with open('history.csv','rb') as history_data:
        reader = csv.reader(history_data)
        for row in reader:

            history.append(load_chats())

load_history()

def add_status (C_S_M) : #function to add status C_S_M is the variable it can bt changed
    if C_S_M != None : #if C_S_M is not equal to none then print statement will execute
        print "your current status is " + C_S_M
    else: #if C_S_M is equal to none then print statement will execute
        print "there is no current status"
    user_choice = raw_input("Select from old status? Y or N: ")
    if user_choice.upper() == 'Y': # if user_choice is yes then old status will be displayed via list
        serial_no = 1
        for old_status in STATUS_MESSAGES:
            print str(serial_no) + "." + old_status
            serial_no = serial_no + 1
        new_status = raw_input("Write your status: ")
        STATUS_MESSAGES.append(new_status)
    else: # when any other input is given then else statement will execute
        print "Invalid Entry"
    return new_status

def  add_friend() :
    frnd = Spy('','',0,0.0)
    frnd.name =  raw_input("write your name: ")
    frnd.age = input("write the age of the frnd: ")
    frnd.salutation = raw_input("Mr. or Ms.: ")
    frnd.name = frnd.salutation+ " " + frnd.name
    frnd.rating = input('write the rating of frnd: ')
    frnd.is_online = True

    if len(frnd.name)>2 and 50>=frnd.age>=12 and frnd.rating>= spy.rating:
        friends.append(frnd)
        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([frnd.name, frnd.rating, frnd.age, frnd.is_online])


    else:
        print("frnd with these values cant be added")
    return len(friends)


def select_frnd() :
    serial_no = 1
    for frnd in friends:
        print str(serial_no) + " " + frnd['name']
        serial_no = serial_no + 1
    user_selected_frnd = input("To whom you want to send or read the message? :")
    user_index = friends[user_selected_frnd - 1]
    return user_index

def send_message():
    selected_frnd = select_frnd()
    message = raw_input("What is your secret message? ")
    original_image = raw_input("What is the name of your image? ")
    output_path = "output.png"
    Steganography.encode(original_image,output_path,message)
    new_chat = {
        "message": message,
        "time": datetime.now(),
        "sent_by_me": True
    }
    friends[selected_frnd]['chats'].append(new_chat)
    print "Message Encrypted"

def read_message() :
    choosen_frnd = select_frnd()
    output_path = raw_input("Name of image to be decoded: ")
    secret_text = Steganography.decode(output_path)
    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }
    friends[choosen_frnd]['chats'].append(new_chat)
    print "Your secret message is " + secret_text

def spy_chat(spy): #function is created with name spy_chat

    current_status_message = None #initally there is no current status
    show_menu = True #menu will be displayed only when value is true
    while show_menu : #while loop to continuiously execute menu_choice
        menu_choice = input("What would you like to do? \n 1. Add a Status \n 2.Add a Friend \n 3. Send a message \n 4. Read A Message \n 0. Exit \n")#features which will be same for new and old user
        if menu_choice == 1:
            updated_status_message = add_status(current_status_message)
            print 'Your updated status is:' + updated_status_message
        elif menu_choice == 2:
           no_of_frnds = add_friend()
           print "I have" + " " + str(no_of_frnds) +" "+"friends"
        elif menu_choice == 3:
            send_message()
        elif menu_choice == 4:
            read_message()
        elif menu_choice ==0:
            show_menu = False #exits
        else:
            print "Invalid Choice"

question = raw_input(" Are you a new user? Y or N :") #getting input from user to know that if user is new
if question.upper() == "N": #.upper class changes the input into upper case
    print "We already have your details...glad to see you again" #if user says no then a msg will be displayed.
    spy_chat(spy)#function uses values from spy_details
elif question.upper() =="Y": #if user says yes then he needs to provide this details
    spy = Spy('','',0,0.0)
    print "What's Up?" #"" '' both types of inverted commas can be used to print a statement
    spy.name = raw_input("What is your name?")#raw_input gets string values from user
    if len(spy.name)>3: #if name length is greater than 3 only then user will be allowed to enter the system
        print 'Welcome ' + spy.name +' Glad to have you back with us.' #concatenation of strings
        spy.salutation = raw_input("What should i call you? Mr. or Ms.")
        if spy.salutation == "Mr." or spy.salutation == "Ms." or spy.salutation == "mr." or spy.salutation == "ms.": #no other value will be used for salutaion
            spy.name = spy.salutation +" " + spy.name #" " is used to provide space
            print spy.name
            print "Alright" + " " + spy.name + " " + "i would like to know more about you before we proceed..."
        else:
            print "Enter a valid slutation" #if any salutaion other than the salutaions mentioned in if statement like rr then this msg will display

        spy.age = input("What is your age?") #input is used to get integer values from user
        if spy.age > 12 and spy.age < 50: #if entered age is btw 12 and 50 only then next input will be asked for
            spy.rating = input("What is your spy rating?")
            if spy.rating > 4.5: # gradation of spies on basis of rating
                print 'best spy...!'
            elif spy.rating > 3.5 and spy.rating <= 4.5:
                print 'good spy...you can do much better'
            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                print 'fine spy..need to do better'

                spy.is_online = True #after entering all the details now spy is online
                print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(
                    spy.rating) + " Proud to have you onboard" #str() is used to join integers and strings or for typecasting
                spy_chat(spy.name, spy.age, spy.rating)#all the values will be passed to fun spy_chat
        else:
            print "Your age is not valid"#age less than 12 or greater than 50
            print 'We can always use somebody to help in the office.'
    else:
        print"Please enter a valid name of 4 characters"#more than 3 characters required to enter a valid name
else:
    print"Invalid Entry" #other input is given rather than Y or N



