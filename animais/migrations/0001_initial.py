# Generated by Django 4.0.2 on 2022-02-03 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('predador', models.BooleanField()),
                ('venenoso', models.BooleanField()),
                ('domestico', models.BooleanField()),
            ],
        ),
    ]
