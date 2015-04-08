# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.managers
import mezzanine.core.fields
import pari.article.mixins.admin_thumb


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords_string', models.CharField(max_length=500, editable=False, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('_meta_title', models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', blank=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('district', models.CharField(unique=True, max_length=100, verbose_name='District')),
                ('district_description', models.CharField(max_length=255, null=True, verbose_name='Description(Optional)', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('district',),
                'verbose_name': 'District',
                'verbose_name_plural': 'Districts',
            },
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords_string', models.CharField(max_length=500, editable=False, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('_meta_title', models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', blank=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('zip_import', models.FileField(help_text="Upload a zip file containing images, and they'll be imported into this gallery.", upload_to=b'faces', verbose_name='Zip import', blank=True)),
                ('is_pinned', models.BooleanField(default=False, verbose_name=b'Pin To Top')),
                ('district', models.ForeignKey(to='faces.District', null=True)),
                ('image_collection', models.ForeignKey(to='album.ImageCollection')),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('district',),
                'verbose_name': 'Face',
                'verbose_name_plural': 'Faces',
            },
            bases=(models.Model, pari.article.mixins.admin_thumb.AdminThumbMixin),
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
        migrations.CreateModel(
            name='FaceImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords_string', models.CharField(max_length=500, editable=False, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('_meta_title', models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', blank=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('is_pinned', models.BooleanField(default=False, verbose_name=b'Pin To Top')),
                ('image_file', mezzanine.core.fields.FileField(max_length=200, null=True, verbose_name='File')),
                ('face', models.ForeignKey(related_name='images', to='faces.Face')),
                ('image_collection_image', models.ForeignKey(related_name='face_image', to='album.ImageCollectionImage')),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'FaceImage',
                'verbose_name_plural': 'FaceImages',
            },
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
    ]
