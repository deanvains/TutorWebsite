import yagmail

def sendDetailsToDiscord(name, email, phone, state, course):
    print(name)
    print(email)
    print(phone)
    print(state)
    print(course)
    yag = yagmail.SMTP()
    contents = [name, email, phone, state, course]
    yag.send('russell.error.reporting@gmail.com', 'New Client', contents)
