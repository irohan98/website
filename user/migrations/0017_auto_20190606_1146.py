

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20190606_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
