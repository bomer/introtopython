answer=raw_input('Enter the Secret: ')
attempts=1
maxAttempts=2
secret='pink'
while answer!=secret and attempts<maxAttempts:
    print "Attempt number " + str(attempts) + " is WRONG"
    answer=raw_input('Enter the Secret: ')
    attempts=attempts+1
if answer==secret:
    print "Correct a mondo!"
else:
    print "Locked out after " + str(attempts) + " attempts"
