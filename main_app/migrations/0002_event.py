# Generated by Django 4.0.4 on 2022-04-23 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.TextField(max_length=250)),
                ('contact', models.CharField(max_length=100)),
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.ministry')),
            ],
        ),
    ]