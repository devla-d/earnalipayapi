# Generated by Django 4.0.6 on 2022-07-28 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0002_transactions_paymethod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='trans_type',
            new_name='mode',
        ),
    ]
