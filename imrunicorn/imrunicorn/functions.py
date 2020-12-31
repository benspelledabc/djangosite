# import json
# from datetime import datetime
# from django.conf import settings
# from django.contrib.auth.models import User
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from .models import PageCounter
import logging

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


# create an entry or step it up if there is one.
def step_hit_count_by_page(input_page_name='/'):
    result = PageCounter.objects.filter(
        Q(page_name=input_page_name)
    )[0:1]
    if not result:
        result = PageCounter.objects.create(page_name=input_page_name, page_hit_count=1)
    else:
        result[0].page_hit_count = result[0].page_hit_count + 1
        result[0].page_name = input_page_name
        result[0].save()

    return result


def email_user(email_name, email_subject, email_body):
    try:
        subject = 'testing email in django'
        message = ""
        # for x in range(5):
        #     message = "%s                            %s\n\r" % (message, "spam")

        message = "%s\n\r -- %s" % (message, email_body)
        email_from = settings.EMAIL_HOST_USER
        # recipient_list = ['svendavison@gmail.com', 'svenisa@live.com']
        recipient_list = ['svendavison@gmail.com']

        logger.error("Sent email to {0} as {1} with password {2}"
                     .format(email_name, settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD))
        result = send_mail(subject, message, email_from, recipient_list)
        print("Email sent....")
    except Exception as e:
        print("Exception: {0}".format(e))
        print("Email failed to send.")
        logger.error("Failed to send email to {0} as {1} with password {2}"
                     .format(email_name, settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD))
        return False

    return True
