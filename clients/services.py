import datetime

from django.conf import settings
from django.core.mail import send_mail

from clients.models import Newsletter, MailingAttempt


def send_email(message_client, message_settings):
    try:
        send_mail(
            subject=message_settings.message.subject,
            message=message_settings.message.letter,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[message_client.email],
            fail_silently=False,
        )

        MailingAttempt.objects.create(
            status=MailingAttempt.STATUS_OK,
            settings=message_settings,
            client=message_client,
        )
    except Exception as e:
        MailingAttempt.objects.create(
            status=MailingAttempt.STATUS_FAILED,
            settings=message_settings,
            client=message_client,
            server_response=str(e),
        )


def send_all_mails():
    datetime_now = datetime.datetime.now(datetime.timezone.utc)

    for mailing_settings in Newsletter.objects.filter(status=Newsletter.STATUS_STARTED):

        if (datetime_now > mailing_settings.start_time) and (datetime_now < mailing_settings.end_time):

            for mailing_client in mailing_settings.clients.all():

                mailing_log = MailingAttempt.objects.filter(client=mailing_client.pk, settings=mailing_settings)

                if mailing_log.exists():
                    last_try_date = mailing_log.order_by('-last_try').first().last_try

                    if mailing_settings.period == Newsletter.PERIOD_DAILY:
                        if (datetime_now - last_try_date).days >= 1:
                            send_email(mailing_client, mailing_settings)
                    elif mailing_settings.period == Newsletter.PERIOD_WEEKLY:
                        if (datetime_now - last_try_date).days >= 7:
                            send_email(mailing_client, mailing_settings)
                    elif mailing_settings.period == Newsletter.PERIOD_MONTHLY:
                        if (datetime_now - last_try_date).days >= 30:
                            send_email(mailing_client, mailing_settings)

                else:
                    send_email(mailing_client, mailing_settings)