from spy_details import spy
print "Hello!" #welcome msgs for user
print 'Let\'s get started.'
STATUS_MESSAGES = ['Cant talk spychat only','Available','Always busy','At work','in a meeting']
friends =[{'name':'raj','age':26,'rating':5.8,'is_online':True} ,{'name':'simran','age':36,'rating':6.8,'is_online':True}]



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
    frnd = {
        'name': '',
        'age': 0,
        'rating': 0.0,
        'is_online': True
    }
    frnd['name'] =  raw_input("write your name: ")
    frnd['age'] = input("write the age of the frnd: ")
    frnd_sal = raw_input("Mr. or Ms.: ")
    frnd['_name'] = frnd_sal+ " " + frnd['name']
    frnd['rating'] = input('write the rating of frnd: ')

    if len(frnd['name'])>2 and 50>=friends['age']>=12 and friends['rating']>= spy['rating']:
        friends.append(frnd)

    else:
        print("frnd with these values cant be added")
    return len(friends)


def spy_chat(spy_name,spy_age,spy_rating): #function is created with name spy_chat

    current_status_message = None #initally there is no current status
    show_menu = True #menu will be displayed only when value is true
    while show_menu : #while loop to continuiously execute menu_choice
        menu_choice = input("What would you like to do? \n 1. Add a Status \n 2.Add a Friend \n 0. Exit \n")#features which will be same for new and old user
        if menu_choice == 1:
            updated_status_message = add_status(current_status_message)
            print 'Your updated status is:' + updated_status_message
        elif menu_choice ==2:
           no_of_frnds = add_friend()
           print "I have" + " " + str(no_of_frnds) +" "+"friends"
        elif menu_choice ==0:
            show_menu = False #exits
        else:
            print "Invalid Choice"

question = raw_input(" Are you a new user? Y or N :") #getting input from user to know that if user is new
if question.upper() == "N": #.upper class changes the input into upper case
    print "We already have your details...glad to see you again" #if user says no then a msg will be displayed.
    spy_chat(spy['name'],spy['age'],spy['rating'])#function uses values from spy_details
elif question.upper() =="Y": #if user says yes then he needs to provide this details
    spy = {
        'name': '',
        'age': 0 ,
        'rating': 0.0,
        'is_online': True
    }
    print "What's Up?" #"" '' both types of inverted commas can be used to print a statement
    spy['name'] = raw_input("What is your name?")#raw_input gets string values from user
    if len(spy['name'])>3: #if name length is greater than 3 only then user will be allowed to enter the system
        print 'Welcome ' + spy['name'] +' Glad to have you back with us.' #concatenation of strings
        spy_salutation = raw_input("What should i call you? Mr. or Ms.")
        if spy_salutation == "Mr." or spy_salutation == "Ms." or spy_salutation == "mr." or spy_salutation == "ms.": #no other value will be used for salutaion
            spy['name'] = spy_salutation +" " + spy['name'] #" " is used to provide space
            print spy['name']
            print "Alright" + " " + spy['name'] + " " + "i would like to know more about you before we proceed..."
        else:
            print "Enter a valid slutation" #if any salutaion other than the salutaions mentioned in if statement like rr then this msg will display

        spy['age'] = input("What is your age?") #input is used to get integer values from user
        if spy['age'] > 12 and spy['age'] < 50: #if entered age is btw 12 and 50 only then next input will be asked for
            spy['rating'] = input("What is your spy rating?")
            if spy['rating'] > 4.5: # gradation of spies on basis of rating
                print 'best spy...!'
            elif spy['rating'] > 3.5 and spy['rating'] <= 4.5:
                print 'good spy...you can do much better'
            elif spy['rating'] >= 2.5 and spy['rating'] <= 3.5:
                print 'fine spy..need to do better'

                spy['is_online'] = True #after entering all the details now spy is online
                print "Authentication complete. Welcome " + spy['name'] + " age: " + str(spy['age']) + " and rating of: " + str(
                    spy['rating']) + " Proud to have you onboard" #str() is used to join integers and strings or for typecasting
                spy_chat(spy['name'], spy['age'], spy['rating'])#all the values will be passed to fun spy_chat
        else:
            print "Your age is not valid"#age less than 12 or greater than 50
            print 'We can always use somebody to help in the office.'
    else:
        print"Please enter a valid name of 4 characters"#more than 3 characters required to enter a valid name
else:
    print"Invalid Entry" #other input is given rather than Y or N



