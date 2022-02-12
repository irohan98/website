

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190214_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='branch',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_details',
            name='year',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
