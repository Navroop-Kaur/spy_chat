print "Hello!"
print "What's Up?"
print 'Let\'s get started.'
spy_name = raw_input("What is your name?")
if len(spy_name)>3:
    print 'Welcome ' + spy_name +' Glad to have you back with us.'
    spy_salutation = raw_input("What should i call you? Mr. or Ms.")
    spy_name = spy_salutation +" " + spy_name
    print spy_name
    print "Alright" + " " + spy_name + " " + "i would like to know more about you before we proceed..."
else:
    print"Please enter a valid name of 4 characters"
spy_age = 0
spy_rating = 0.0
spy_is_online = False

spy_age = input("What is your age?")
if spy_age > 12 and spy_age < 50:
    spy_rating = input("What is your spy rating?")
else:
    print 'Sorry you are not of the correct age to be a spy'
if spy_rating > 4.5:
    print 'best spy...!'
elif spy_rating > 3.5 and spy_rating <= 4.5:
    print 'good spy...you can do much better'
elif spy_rating >= 2.5 and spy_rating <= 3.5:
    print 'fine spy..need to do better'
else:
    print 'We can always use somebody to help in the office.'
spy_is_online = True



