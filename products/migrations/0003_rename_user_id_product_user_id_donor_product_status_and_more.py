# Generated by Django 4.0.5 on 2022-06-06 00:18

from django.db import migrations, models
import django.db.models.deletion
import products.status


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user_id',
            new_name='user_id_donor',
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('IN_PROGRESS', 'IN_PROGRESS'), ('FINISHED', 'FINISHED')], default=products.status.Status['OPEN'], max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='user_id_recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
