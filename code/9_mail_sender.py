import smtplib, ssl, time, pandas
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

gmail_user = ''
gmail_password = ''


def send_mail(recipient, mail_body):

    sender_email = ''
    receiver_email = recipient
    password = ''

    message = MIMEMultipart("alternative")
    message["Subject"] = "Request for feedback on architectural technical debt research"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = mail_body

    # Turn mail_body into html MIMEText objects
    html_mail_content = MIMEText(mail_body, "html")

    # Add mail_body to MIMEMultipart message
    message.attach(html_mail_content)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 25) as server:
        server.starttls()
        server.login(sender_email, password)
        server.ehlo()
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
        print(recipient)
        server.quit()

users = pandas.read_csv('./data/contributors.csv')

for index, user in users.iterrows():

    repos = user['repo']
    repos = ", ".join(repos.split(",")[:9])
    uID = user['uID']
    recipient = user['email']


    mail_body = """\
<html>
<body>
<pre style="font-family: Helvetica, sans-serif; font-size: 12px">Dear OSS contributor,<br />I am a Software Engineering researcher of the Vrije Universiteit Amsterdam.<br />
Jointly with other researchers we created a new method for measuring architectural technical debt, called ATDx.<br />
We are contacting you because you appear as a contributor of the following GitHub repos:
""" + str(repos) + """ 

We analyzed such repos with our method, and would kindly ask your support by:<br />
1. Having a look at the analysis results of your projects, and some background material, available at:
    <a href="https://github.com/S2-group/ATDx_reports/blob/master/reports/"""+ str(uID) + """_report.md">https://github.com/S2-group/ATDx_reports/blob/master/reports/"""+ str(uID) + """_report.md</a>
2. Filling in the on-line survey available at: <a href="https://forms.gle/3kUyLENhZwzgnvPd9">https://forms.gle/3kUyLENhZwzgnvPd9</a><br />
Filling the survey will take no more than 10-15 minutes to complete. 
All responses are anonymous and there are no questions with personally identifiable information. <br />
Your contributions will help us greatly in validating our method.<br />
This research is carried out jointly by the Vrije Universiteit Amsterdam (The Netherlands), and the Software Engineering Institute at Carnegie Mellon University (USA).<br />
Thanks in advance for your help!

Roberto
---
Roberto Verdecchia | Research Associate | Vrije Universiteit Amsterdam, The Netherlands | <a href="http://robertoverdecchia.github.io/">robertoverdecchia.github.io</a><br />
Co-investigators:
Patricia Lago (Vrije Universiteit Amsterdam)
Ivano Malavolta (Vrije Universiteit Amsterdam)
Ipek Ozkaya (Software Engineering Institute, Carnegie Mellon University)
</body>
</html>
"""

    send_mail(recipient, mail_body)
    time.sleep(4)