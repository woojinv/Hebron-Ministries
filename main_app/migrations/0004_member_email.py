# Generated by Django 4.0.4 on 2022-04-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_event_options_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default='foo@example.com', max_length=50),
            preserve_default=False,
        ),
    ]
