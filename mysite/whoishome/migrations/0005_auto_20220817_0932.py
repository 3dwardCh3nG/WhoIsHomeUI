# Generated by Django 3.2.15 on 2022-08-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoishome', '0004_create_discord_config_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='discordnotificationsconfig',
            name='new_connection_message',
            field=models.CharField(default='At time {arrival_time} a new device connected to the network\nMAC: {mac}\nIP: {ip}\nName: {name}', max_length=500),
        ),
        migrations.AddField(
            model_name='discordnotificationsconfig',
            name='new_connection_notification_switch',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='emailconfig',
            name='new_connection_mail_body',
            field=models.CharField(default='At time {arrival_time} a device connected to the network\nMAC: {host.mac}\nIP: {host.ip}\nName: {host.name}', max_length=500),
        ),
        migrations.AddField(
            model_name='emailconfig',
            name='new_connection_mail_subject',
            field=models.CharField(default='New device detected.', max_length=500),
        ),
        migrations.AddField(
            model_name='emailconfig',
            name='new_connection_notification_switch',
            field=models.BooleanField(default=False),
        ),
    ]
