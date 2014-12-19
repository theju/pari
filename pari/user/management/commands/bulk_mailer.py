from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage, get_connection
from django.template import Template, Context

from mezzanine.pages.models import Page

import csv


class Command(BaseCommand):
    args = "<csv_file_path>"
    help = "Send mails on the CSV file"

    def handle(self, *args, **options):
        csv_file = args[0]
        dr = csv.DictReader(open(csv_file, "r"))
        conn = get_connection()
        contact_page = Page.objects.get(slug="contact-us")
        from_email = contact_page.form.email_from
        for row in dr:
            body = Template(row["message"]).render(Context(row))
            subject = Template(row["subject"]).render(Context(row))
            kwargs = {
                "subject": subject,
                "body": body,
                "from_email": from_email,
                "to": [row["to"]],
                "connection": conn
            }
            msg = EmailMessage(**kwargs)
            msg.send()
