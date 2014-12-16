from django.db import models
from mezzanine.forms.signals import form_valid


class Profile(models.Model):
    user = models.OneToOneField("auth.User")
    address = models.TextField(null=True, max_length=200)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contribute_by = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{0} : {1}".format(self.name, self.email)

def save_contact_to_db(sender, **kwargs):
    request = sender
    if request.page.slug not in ["contact-us", "contribute"]:
        return None
    form = kwargs["form"]
    cd = form.cleaned_data
    data = {}
    if request.page.slug == "contact-us":
        contact_fields = {
            "Name": "name",
            "Email": "email",
            "Contributions": "contribute_by",
            "Content": "content"
        }
        for field in request.page.form.fields.all():
            if not contact_fields.get(field.label):
                continue
            data[contact_fields[field.label]] = cd["field_{0}".format(field.id)]
    elif request.page.slug == "contribute":
        contribute_fields = {
            "Name": "name",
            "Email": "email",
            "Contributions": "contribute_by",
            "Message": "content"
        }
        for field in request.page.form.fields.all():
            if not contribute_fields.get(field.label):
                continue
            data[contribute_fields[field.label]] = cd["field_{0}".format(field.id)]
    Contact.objects.create(**data)
form_valid.connect(save_contact_to_db)
