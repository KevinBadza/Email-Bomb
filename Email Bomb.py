import os
import sys
import getpass
import smtplib

print('This is a program that sends any number of emails automatically to an email address')

email = input(' Enter Your Email Address : ')
password = getpass.getpass(' Enter Your Password : ')
victim_email = input(' Enter Destination Email Address : ')
subject = input(' Enter The Subject : ')
message = input(' Enter Your Message Here : ')
count = int(input(' How Many Time You Want To Send :'))
try:

    print('[✓] All done')
    smtp_server = 'smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
        server.starttls()
    server.login(email, password)
    i = 0
    print(' Sending is in Progress \n')
    while i < count:
        i += 1
        server.sendmail(email, victim_email, subject, message)
        if i == 1:
            print('[✓]  %dst Email has been sent successfully ' % i)
        elif i == 2:
            print('[✓]  %dnd Email has been sent successfully ' % i)
        elif i == 3:
            print('[✓]  %drd Email has been sent successfully ' % i)
        else:
            print('[✓]  %dth Email has been sent successfully ' % i)
        sys.stdout.flush()
    server.quit()
except KeyboardInterrupt:
    print(" ")
    print('[x]  Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print('[x]  The username or password you entered is incorrect.')
    print('[x] Check if the Options of Applications are less secure is enabled ')
    sys.exit()
