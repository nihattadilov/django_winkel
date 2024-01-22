from celery import shared_task
from .models import Subscriber
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

# code for run celery:
#celery -A Wellern worker --beat -S django -l info
# for development
#celery -A  Wellern worker --beat --scheduler django --loglevel=info

@shared_task
def send_mail_to_subscribers():
    email_list = Subscriber.objects.all().values_list('email',flat=True)
    mail_text = f"<h1>Nihad Adilov,Mushviq </h1> Salam, <br> Bu test maildir. zəhmət olmasa oxuduqdan sonra silin <br> Təşəkkürlər oxuduğunuz üçün, <br>"

    msg = EmailMultiAlternatives(subject='Test subject', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    msg.attach_alternative(mail_text, "text/html")
    msg.send()


send_mail_to_subscribers.delay()
