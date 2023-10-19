import random
import re
# from twilio.rest import Client
import smtplib

account_sid = 'ACe36a9078b44bf3323e6af8453b615f97'
auth_token = '0a1a20005a5b51a2e091066370743198'

twilio_number = '+12675280928'
target_number = '+918149980220'

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_via_sms(phone_number, otp):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Your OTP is: {otp}",
        from_=twilio_number,
        to=phone_number
    )
    print("OTP sent successfully.")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

password = 'hnch blyy pkxx ralo'
server.login('pranjalatil1214@gmail.com', password)

receiver_email = input("Enter E-mail ID: ")

otp = generate_otp()

def send_otp_via_email():
    sender_email = 'pranjalatil1214@gmail.com'
    message = f'Subject: Your OTP\n\nYour OTP is: {otp}'
    server.sendmail(sender_email, receiver_email, message)
    server.quit()

    print('OTP Sent successfully on your Email.')

# validating email address
def is_valid_email(receiver_email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, receiver_email):
        return True
    else:
        return False

if is_valid_email(receiver_email):
    send_otp_via_email()
else:
    print(f"{receiver_email} is not a valid email address.")


if __name__ == "_main_":
    otp = generate_otp()
    send_otp_via_sms(target_number, otp)