

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20190220_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='branch',
            field=models.CharField(default='', max_length=200),
        ),
    ]
