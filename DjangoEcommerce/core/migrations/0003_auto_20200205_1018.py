# Generated by Django 3.0.2 on 2020-02-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200203_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SP', 'Sport Wear'), ('OW', 'Out Wear')], default='S', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('New', 'danger'), ('BestSeller', 'primary')], default='New', max_length=12),
            preserve_default=False,
        ),
    ]
