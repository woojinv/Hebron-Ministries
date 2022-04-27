# Generated by Django 4.0.4 on 2022-04-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date']},
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('verse', models.TextField(max_length=250)),
                ('ministry', models.ManyToManyField(to='main_app.ministry')),
            ],
        ),
    ]