from django.db import migrations, models

from ..settings import PUSH_NOTIFICATIONS_SETTINGS as SETTINGS


class Migration(migrations.Migration):
	dependencies = [
		('push_notifications', '0007_uniquesetting'),
	]

	operations = [
		migrations.AlterField(
			model_name='gcmdevice',
			name='device_id',
			field=models.CharField(max_length=100, verbose_name="Device ID", blank=True, null=True, db_index=True),
		),
	]
