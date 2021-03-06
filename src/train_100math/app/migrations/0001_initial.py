# Generated by Django 2.2 on 2019-06-11 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('q_count', models.PositiveIntegerField(verbose_name='問題数')),
                ('sucess_count', models.PositiveIntegerField(verbose_name='正解数')),
                ('score', models.PositiveIntegerField(verbose_name='点数')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
