# Generated by Django 3.1.4 on 2020-12-10 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiceManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('created', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('dice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dice.dice')),
            ],
        ),
    ]
