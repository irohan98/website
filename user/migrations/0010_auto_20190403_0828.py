

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20190403_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='date_of_birth',
            field=models.DateField(default=''),
        ),
    ]