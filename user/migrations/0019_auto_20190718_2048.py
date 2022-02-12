

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_auto_20190607_0533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='User_details',
        ),
    ]
