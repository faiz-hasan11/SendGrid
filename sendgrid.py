import sendgrid
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key='{ Enter your API Key }')
from_email = Email(input("EMAIL TO SEND FROM"))
to_email = To(input("EMAIL TO SEND TO"))
subject = input("EMAIL SUBJECT")
content = Content("text/plain", input("ENTER YOUR MESSAGE"))
mail = Mail(from_email, to_email, subject, content)
try:
    response = sg.client.mail.send.post(request_body=mail.get())
except:
    print("Connection Error Retry!!")
print(response.status_code)
print(response.body)
print(response.headers)