**Python installation**:
```
sudo apt-get install python
```
***
**Usage**:
```
1. Prepare your source email and destination email in >.env
2. Execute main.py file with command line parameters:

Example: help - send you all information about app.
Example: 10 - send 10 mails to destination email.
```
***
**And, of course you can use this application for just sending mails to specific emails**

**Just refactor code in this places:**

1. Domain and port in `smtp_obj = smtplib.SMTP("smpt.mail.ru", 465)`
2. Implement message and subject attributes in your function:
    ```
   def bomber(message, subject):
   msg['Subject'] = subject
   msg = MIMEText(message)
    ```
3. In main section add this line: `args = sys.argv[2:]`
and pass them into your function `bomber(*args)`