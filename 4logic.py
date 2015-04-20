print "Welcome to the unbreakable security robot system"
age=input("How old are you?: ")
sex=raw_input("Sex? Enter male or female:")
drinks=input("How many drinks have you had tonight sir?: ")

if sex!='male' and sex!='female':
    sex='other'
print 'sex detector has deteced you as ' + sex

if (sex=='female' and age>=18) or (sex=='female' and drinks>4):
    print "You will get access to the club"
    if drinks>10:
        print "Come right this way to the VIP section"
    else:
        print "You look like you could use a drink"
        
elif sex=='male' and drinks >2:
    print 'Sorry you are too drunk to come in'



##
##number=input("How old are you?: ")
##if number>=18:
##    print "Old to enough to drink!"
##if number>0:
##    print "WELL DAMN TOOTEN YOURE ALIVE"
##elif number==17:
##    print "I guess you're still in school."
##elif number>=16:
##    print "You're Old enough to... well not old enough to drink"
##else:
##    print "You were born before " + str(2014-16)
##    print "... that means you probably don't know what Jurassic Park is"


#oven=raw_input('Do you have a fan forced oven, enter y or n: ')
#if oven=='y':
#    print "Set the oven to 180 degrees"
#    print "Oh and totally remember to turn the fan on"
#elif oven=='n':
#    print "Sethe oven to 200 degrees"
#else:
#    print "You are bad at following directions, GOOD DAY SIR!"
#
#print "Bye!"


