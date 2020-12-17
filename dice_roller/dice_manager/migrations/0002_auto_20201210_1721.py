# Generated by Django 3.1.4 on 2020-12-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dice', '0001_initial'),
        ('dice_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dicemanager',
            name='dice',
        ),
        migrations.AddField(
            model_name='dicemanager',
            name='dice',
            field=models.ManyToManyField(to='dice.Dice'),
        ),
    ]