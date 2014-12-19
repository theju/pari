from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage

from mezzanine.conf import settings
from mezzanine.pages.models import Page

from pari.user.models import Contact

import datetime
import csv


class Command(BaseCommand):
    help = "Send a list of contacts created daily"

    def handle(self, *args, **kwargs):
        today = datetime.date.today()
        yday = today - datetime.timedelta(days=1)
        contacts = list(Contact.objects.filter(created_on__gte=yday,
                                               created_on__lt=today).values('name', 'email'))
        filename = "/tmp/contacts.csv"
        output_file = csv.DictWriter(open(filename, "w"),
                                     fieldnames=["name", "email"])
        output_file.writeheader()
        rows = []
        for contact in contacts:
            rows.append(contact)
        if not rows:
            return None
        output_file.writerows(rows)
        page = Page.objects.get(slug="contact-us")
        form = page.form
        msg = EmailMessage(**{
            "subject": "Contacts created on {0}".format(yday.strftime("%d-%m-%Y")),
            "body": "Please check attachment",
            "from_email": settings.DEFAULT_FROM_EMAIL,
            "to": [form.email_from],
            "attachments": [(filename, open(filename, "r").read(), "text/csv")]
        })
        msg.send()
