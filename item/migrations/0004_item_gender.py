# Generated by Django 5.0.7 on 2024-07-19 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='gender',
            field=models.CharField(choices=[('M', 'Man'), ('W', 'Woman')], max_length=1, null=True),
        ),
    ]
