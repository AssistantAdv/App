import smtplib

def sender(email, otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('assistantadv00@gmail.com', 'phojnfsaitavngpw')
    subject = "Verify your email"
    content = f"""Hello,

Thank you for signing up to Artificial Assistant. We will be sending an email to the email address you provided. Please verify your email and we'll send instructions on how to proceed.

To verify your account,

OTP :- {otp}

Please do not share this OTP with anyone to avoid fraudulent activities. If you're not receiving any emails from us, please check your spam folder and add us as a contact in your email account settings.

Best regards,

The Artificial Assistant Team"""
    msg = f"Subject: {subject}\n\n{content}"
    server.sendmail('assistantadv00@gmail.com', email, msg)
    print("Sent successfully")
    server.quit()

def user_sender(email, user):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('assistantadv00@gmail.com', 'phojnfsaitavngpw')
    subject = "Please reset your username"
    content = f"""Hi sir,

We noticed you've been inactive for a while. We would like to help you with that. To ensure your account is secure, please reset your username and password.

You can do this by clicking on the "Sign in" button on our homepage, then follow the instructions.

Username :- {user}

If you can't remember your username or password, please refer to this article for help. We're happy to talk with you at any time, just reply to this email if you need anything!

Hope we get to see you again soon!

All the best, Artificial Assistant"""
    msg = f"Subject: {subject}\n\n{content}"
    server.sendmail('aiassistant00@gmail.com', email, msg)
    print("Sent successfully")
    server.quit()

def pass_sender(email, user, passwd):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('assistantadv00@gmail.com', 'phojnfsaitavngpw')
    subject = "Forget Password on Artificial Assistant"
    content = f"""Hi,

We noticed you requested a password reset for your Ai Assistant account.

Please use the following information to log in:

Username: {user}
Password: {passwd}

Please do not share your Username or Password with anyone to avoid fraudulent activities.

If you have any questions, please contact us at aiassistant002@gmail.com."""
    msg = f"Subject: {subject}\n\n{content}"
    server.sendmail('aiassistant00@gmail.com', email, msg)
    print("Sent successfully")
    server.quit()

def login_sender(email, name):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('assistantadv00@gmail.com', 'phojnfsaitavngpw')
    subject = f"Security Alert for Artificial Assistant"
    content = f"""Hi {name},

We've seen that you're just signed up for our service!

To keep your account secure, we need to verify that the device you are signing in from belongs to you. To do this, please click on the link below and sign in with your username and password. If everything is correct, we will show a green check mark and "Verified" will appear below the link.

Don't forget to sign out of any other devices when you've finished using them so we can confirm they're yours too! We appreciate your help with keeping your account safe.

Best, Artificial Assistant"""
    msg = f"Subject: {subject}\n\n{content}"
    server.sendmail('aiassistant00@gmail.com', email, msg)
    print("Sent successfully")
    server.quit()

def register_sender(email, name):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('assistantadv00@gmail.com', 'phojnfsaitavngpw')
    subject = f"Registration Successful"
    content = f"""Hi {name},

We are so very happy to hear that you have successfully registered. We know how important it is for our clients to be able to get started quickly, and we've here to help you do just that.

Please take a moment to go through our getting-started guides and tutorials, as well as any other resources we may have in the sidebar of your account dashboard.

We are available by email if you need any help or support.

Thank you for choosing Assistant! We look forward to supporting your business growth in the days, weeks and months ahead.

Best regards, Artificial Assistant team"""
    msg = f"Subject: {subject}\n\n{content}"
    server.sendmail('aiassistant00@gmail.com', email, msg)
    print("Sent successfully")
    server.quit()

# email = "aiassistant002@gmail.com"
# passwd = "yodsuxghzhyxtxeo"