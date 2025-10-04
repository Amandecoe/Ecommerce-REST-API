from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
#any function marked with this decorator becomes a celery task that workers can execute asynchronously
# it can be called with .delay() from anywhere in Django
def send_confirmation_email(user_email, order_id):
    subject = "Your Order Confirmation"
    message = f"Thank you for your purchase, Your order ID is {order_id}."
    
    send_mail(
        subject, #email subject
        message, #email body
        settings.DEFAULT_FROM_EMAIL, #from address
        [user_email], #list of recipients
        fail_silently = False, #raise error if sending fails
    )
    #sends the actual email
    return f"Email sent to {user_email} for order {order_id}"