# Generated by Django 4.0.5 on 2022-10-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_shop_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200, verbose_name='Kullanıcı adı')),
                ('password', models.CharField(max_length=200, verbose_name='Kullanıcı Şifre')),
            ],
        ),
    ]
