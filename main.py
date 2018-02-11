from spy_details import spy_name, spy_age, spy_rating,spy_salutation
print "Hello!" #welcome msgs for user
print 'Let\'s get started.'
STATUS_MESSAGES = ['Cant talk spychat only','Available','Always busy','At work','in a meeting']
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
        user_status_selection = input('Which one do u want to select this time?')
        new_status = STATUS_MESSAGES[user_status_selection - 1]
    elif user_choice.upper() =='N': #if user_choiceis no then new status will be added
        new_status = raw_input("Write your status: ")
        STATUS_MESSAGES.append(new_status)
    else: # when any other input is given then else statement will execute
        print "Invalid Entry"


def spy_chat(spy_name,spy_age,spy_rating): #function is created with name spy_chat
    current_status_message = None #initally there is no current status
    show_menu = True #menu will be displayed only when value is true
    while show_menu : #while loop to continuiously execute menu_choice
        menu_choice = input("What would you like to do? \n 1. Add a Status \n 2.Add a Friend \n 0. Exit \n")#features which will be same for new and old user
        if menu_choice == 1:
            updated_status_message = add_status(current_status_message)
            print 'Your updated status is:' + updated_status_message
        elif menu_choice ==2:
            print "will add a friend"#add a friend
        elif menu_choice ==0:
            show_menu = False #exit
        else:
            print "Invalid Choice"

question = raw_input(" Are you a new user? Y or N :") #getting input from user to know that if user is new
if question.upper() == "N": #.upper class changes the input into upper case
    print "We already have your details...glad to see you again" #if user says no then a msg will be displayed.
    spy_chat(spy_name,spy_age,spy_rating)#function uses values from spy_details
elif question.upper() =="Y": #if user says yes then he needs to provide this details
    print "What's Up?" #"" '' both types of inverted commas can be used to print a statement
    spy_name = raw_input("What is your name?")#raw_input gets string values from user
    if len(spy_name)>3: #if name length is greater than 3 only then user will be allowed to enter the system
        print 'Welcome ' + spy_name +' Glad to have you back with us.' #concatenation of strings
        spy_salutation = raw_input("What should i call you? Mr. or Ms.")
        if spy_salutation == "Mr." or spy_salutation == "Ms." or spy_salutation == "mr." or spy_salutation == "ms.": #no other value will be used for salutaion
            spy_name = spy_salutation +" " + spy_name #" " is used to provide space
            print spy_name
            print "Alright" + " " + spy_name + " " + "i would like to know more about you before we proceed..."
        else:
            print "Enter a valid slutation" #if any salutaion other than the salutaions mentioned in if statement like rr then this msg will display
        spy_age = 0 #inital values
        spy_rating = 0.0
        spy_is_online = False #boolean values
        spy_age = input("What is your age?") #input is used to get integer values from user
        if spy_age > 12 and spy_age < 50: #if entered age is btw 12 and 50 only then next input will be asked for
            spy_rating = input("What is your spy rating?")
            if spy_rating > 4.5: # gradation of spies on basis of rating
                print 'best spy...!'
            elif spy_rating > 3.5 and spy_rating <= 4.5:
                print 'good spy...you can do much better'
            elif spy_rating >= 2.5 and spy_rating <= 3.5:
                print 'fine spy..need to do better'

                spy_is_online = True #after entering all the details now spy is online
                print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(
                    spy_rating) + " Proud to have you onboard" #str() is used to join integers and strings or for typecasting
                spy_chat(spy_name, spy_age, spy_rating)#all the values will be passed to fun spy_chat
        else:
            print "Your age is not valid"#age less than 12 or greater than 50
            print 'We can always use somebody to help in the office.'
    else:
        print"Please enter a valid name of 4 characters"#more than 3 characters required to enter a valid name
else:
    print"Invalid Entry" #other input is given rather than Y or N



