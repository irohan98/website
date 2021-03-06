

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20190403_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='branch',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='phone_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='roll_no',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='year',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
