import yagmail

def sendDetailsToDiscord(name, email, phone, state, course):
    print(name)
    print(email)
    print(phone)
    print(state)
    print(course)
    yag = yagmail.SMTP('deanvains18@gmail.com')
    contents = [name, email, phone, state, course]
    yag.send('dean.vains@outlook.com', 'New Client', contents)
