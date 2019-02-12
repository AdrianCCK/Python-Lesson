

username = input("Please enter your name: ")

lastLength = 0
while True:
    f = open('msgbuffer.txt', 'r+')
    messages = f.readlines()
    mailboxSize = len(messages)

    if mailboxSize > 0 and mailboxSize > lastLength:
        print( messages[-1] )
        lastLength = mailboxSize
        message = input("|")

        if message == 'read':
            print( messages[-1] )
    
        f.write( '%s:%s' % (username, message) )
        f.write('\n')

        f.close()
