# Generated by Django 2.1.5 on 2019-01-26 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190126_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='addcomment',
        ),
    ]
