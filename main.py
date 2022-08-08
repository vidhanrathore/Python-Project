import random
import smtplib
OTP = str(random.randint(100000, 999999))
msg = OTP + ' is <strong>your</strong> OTP.\n Enter this to verify your account '
msg = 'Subject: OTP Verification \n' + msg
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your Mail", "Your key")
email_id = input("Enter your email: ")
s.sendmail("Vidhan", email_id, msg)


while 1:
    a = input("Enter Your OTP >>: ")
    if a == OTP:
        print("Verified")
        break
    else:
        print("Please Check your OTP again")

print("Thanks for your Verification.\nPLease Visit again")
