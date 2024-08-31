# Generated by Django 5.0.7 on 2024-08-05 07:16

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_authordetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(error_messages={'max_value': 'Please less!!!!!!!', 'min_value': 'Please more'}, validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(120)]),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('books', models.ManyToManyField(related_name='events', to='library.book')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='library.library')),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='library.event')),
                ('member', models.ManyToManyField(related_name='event_participations', to='library.member')),
            ],
        ),
    ]
