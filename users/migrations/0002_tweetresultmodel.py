# Generated by Django 2.0.13 on 2020-10-07 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetResultModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usrname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('tweetmsg', models.IntegerField()),
                ('prediction', models.IntegerField()),
                ('accuracy', models.IntegerField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'TweetResultTable',
            },
        ),
    ]