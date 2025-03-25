import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("**************************************")

num_users = int(input("How many users do you want to send OPTs to? "))
for _ in range(num_users):

    print("**************************************")

    name = input("Enter your Name: ")
    otp = random.randint(1111,9999)
    body = f"OTP for verification is {otp}"

    msg = MIMEMultipart()
    msg["From"] = "balasowmya434@gmail.com"
    msg["To"] = input("Enter Email Id: ")
    msg["Subject"] = "OTP for validation"
    msg.attach(MIMEText(body,"plain"))

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("balasowmya434@gmail.com","diyb vffw fljf opsw")
    server.send_message(msg)
    server.quit()
    attempts=3
    while attempts > 0:
        cotp = int(input("Enter OTP Received: "))
        if otp == cotp:
            print("OTP Verification Success")
            break
        else:
            attempts -= 1
            print(f"Invalid OTP. You have {attempts} attemp(s) left.")
    if attempts == 0:
        print(f"OTP Verification failed for {name}.Please try again later.")
    print("\n---End of Verification ---\n")
               
