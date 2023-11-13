from django.db import migrations, models

class Migration(migrations.Migration):
	dependencies = [
		('push_notifications', '0009_alter_apnsdevice_device_id'),
	]

	operations = [
		migrations.AlterField(
			model_name='gcmdevice',
			name='device_id',
			field=models.CharField(max_length=100, verbose_name="Device ID", blank=True, null=True, db_index=True),
		),
	]
