# Generated by Django 4.0.5 on 2022-07-05 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_meetup_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='joiners',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
    ]
