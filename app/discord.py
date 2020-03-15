import yagmail

def sendDetailsToDiscord(name, email, phone, state, course, address, browser):

    yag = yagmail.SMTP('deanvains18@gmail.com')
    contents = [name, email, phone, state, course, address, browser]
    yag.send('dean.vains@outlook.com', 'New Client', contents)
