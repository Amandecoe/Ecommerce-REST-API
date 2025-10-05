from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
@shared_task
#any function marked with this decorator becomes a celery task that workers can execute asynchronously
# it can be called with .delay() from anywhere in Django
def send_order_confirmation_email(user_email, order_id):
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

@shared_task
def send_weekly_newsletter():
    users = User.objects.filter(is_active = True) #for all active users

    for user in users:
        subject = "Your Weekly Deals & Recommendations"
        message = f"Hi {user.username}, Don't miss out on the new products and special deals this week! " 
        send_mail (
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently = False #raises an error if it fails
        )  