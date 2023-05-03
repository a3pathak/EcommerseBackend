from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from anyio import Path

conf = ConnectionConfig(
    MAIL_FROM="ajitpathak0449@gmail.com",
    MAIL_USERNAME="ajitpathak0449",
    MAIL_PASSWORD="jpgfstnfqpufehsk",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS= True,
    MAIL_SSL_TLS= False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True,
    TEMPLATE_FOLDER=Path(__file__).parent.parent / 'templates',
)

def otp_generator():
    return randint(100000, 1000000)

def sendRegistrationMail(email, mobile, background_tasks):
    message = MessageSchema(
        subject="New Registration",
        recipients = [email],
        body = f"You have new Registration.\n\nEmail Address: {email}\nContact No.: {mobile}",
        subtype=MessageType.plain
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)

def sendOTPemail(otp, email, message, background_tasks):
    message = MessageSchema(
        subject="OTP for email verification",
        recipients = [email],
        body = f"Welcome to STARTUP KHATA.\nOTP for {mess} is {otp}",
        subtype=MessageType.plain
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)

def sendConfirmInfo(password, email, message, background_tasks):
    message = MessageSchema(
        subject="Password Change",
        recipients = [email],
        body = f"{mess} {otp}",
        subtype=MessageType.plain
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)

async def sendInvoice(invoiceNumber,email, file):
    message = MessageSchema(
        subject=f"Invoice-{invoiceNumber} from {email}",
        recipients = [email],
        # body = f"{mess} {otp}",
        subtype=MessageType.plain,
        template_body={
            "client_name" : email, "invoice_number": invoiceNumber, "sender": email
        },
        attachments=[   
            {
                "file": file
            }
        ]
    )
    fm = FastMail(conf)
    # background_tasks.add_task(fm.send_message, message)
    response = await fm.send_message(message, template_name = "invoice.html")
    return True