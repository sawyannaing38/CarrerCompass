import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def validPassword(password):

    if 6 <= len(password) <= 8 and containUpper(password) and containNumber(password) and containSpecial(password):
        return True 
    
    return False 

def containUpper(password):
    for char in password:
        if char.isupper():
            return True 
    return False 

def containNumber(password):
    for char in password:
        if char.isdigit():
            return True 
    return False

def containSpecial(password):
    specials = ["@", "!", "#", "$", "*"]

    for char in password:
        if char in specials:
            return True 
    return False 

# For Seding Email
def sendEmail(subject, body, to_email):

        from_email = "nsaw460@gmail.com"
        from_password = "ixsh jeni lcxq vlab"

        # Creatng the email
        msg = MIMEMultipart()
        msg["From"] = from_email 
        msg["To"] = to_email
        msg["Subject"] = subject

        # Attach the email body
        msg.attach(MIMEText(body, "plain"))

        # Connecting to server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login the email
        server.login(from_email, from_password)

        server.send_message(msg)

        server.quit()

