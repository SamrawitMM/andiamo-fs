# Generated by Django 3.1.2 on 2020-11-21 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('passenger', '0001_initial'),
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='triphistory',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passenger.passenger'),
        ),
    ]
