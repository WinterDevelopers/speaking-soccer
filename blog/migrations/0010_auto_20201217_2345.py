# Generated by Django 3.1.2 on 2020-12-17 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201123_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.IntegerField(choices=[(0, 'EPL'), (1, 'laliga'), (2, 'seria-A'), (3, 'bundesliga'), (4, 'league 1')], default=0),
        ),
    ]
