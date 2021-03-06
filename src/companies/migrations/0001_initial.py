# Generated by Django 3.1.7 on 2021-03-22 07:42

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('unverified', 'Non vérifiée'), ('verified', 'Vérifiée')], default='unverified', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('td_id', models.CharField(max_length=64, verbose_name='Identifiant Trackdechets')),
                ('siret', models.CharField(max_length=10, verbose_name='Siret')),
                ('name', models.CharField(max_length=256, verbose_name='Nom')),
                ('info', models.TextField(blank=True, verbose_name='Info')),
            ],
            options={
                'verbose_name': 'Entreprise',
                'verbose_name_plural': 'Entreprises',
                'ordering': ('created',),
            },
        ),
    ]
