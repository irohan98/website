

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20190606_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
