# Generated by Django 3.1.2 on 2020-10-19 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0006_auto_20201019_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planinclude',
            name='feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='include', to='landing_page.planfeature'),
        ),
    ]
