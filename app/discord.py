import yagmail

def sendDetailsToDiscord(name, email, phone, state, course, address, browser):

    message = createMessage(name, email, phone, state, course, address, browser)

    yag = yagmail.SMTP('deanvains18@gmail.com')
    contents = [message]
    yag.send('dean.vains@outlook.com', 'New Client', contents)


def createMessage(name, email, phone, state, course, address, browser):
    str = "Hello Tutors, \n \n my name is " + name + " and I would like to apply for tutoring in " + course + " in " + state \
        + ". My email address is: " + email + " and my phone number is: " + phone + ". \n \n" + "Browser: " + browser \
        + "\n IP Address: " + address

    return str
