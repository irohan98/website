

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190214_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='branch',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 13, 42, 26, 4000)),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='phone_no',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='roll_no',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='year',
            field=models.CharField(default='', max_length=20),
        ),
    ]
