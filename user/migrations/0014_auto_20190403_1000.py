

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20190403_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='branch',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='roll_no',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
