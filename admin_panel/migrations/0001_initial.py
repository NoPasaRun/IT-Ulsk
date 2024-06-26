# Generated by Django 5.0.6 on 2024-05-29 06:15

import datetime
import django.contrib.auth.models
import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Company name')),
                ('image_link', models.CharField(max_length=64, verbose_name='Image link')),
                ('income', models.BigIntegerField(default=0, verbose_name='Income')),
                ('quantity', models.SmallIntegerField(default=0, verbose_name='Quantity')),
                ('creation_date', models.DateField(default=datetime.date.today, verbose_name='Creation date')),
                ('growth', models.DecimalField(decimal_places=3, default=0, max_digits=4, verbose_name='Growth rate')),
                ('offers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, null=True), default=list, size=None, verbose_name='Offers')),
                ('technologies', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, null=True), default=list, size=None, verbose_name='Technologies')),
                ('business_number', models.CharField(max_length=16, verbose_name='Business number')),
                ('address', models.CharField(max_length=128, verbose_name='Address')),
                ('leader_info', models.CharField(max_length=64, verbose_name='Leader info')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Description')),
                ('contact_info', models.CharField(max_length=64, verbose_name='Contact info')),
                ('web_site_link', models.CharField(max_length=64, verbose_name='Website link')),
                ('vk_link', models.CharField(blank=True, max_length=64, null=True, verbose_name='VK link')),
                ('tg_link', models.CharField(blank=True, max_length=64, null=True, verbose_name='TG link')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Event title')),
                ('caption', models.CharField(blank=True, max_length=128, null=True, verbose_name='Caption')),
                ('short_description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Short description')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Description')),
                ('facts', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, null=True), default=list, size=None, verbose_name='Facts')),
                ('tg_link', models.CharField(blank=True, max_length=128, null=True, verbose_name='TG link')),
                ('vk_link', models.CharField(blank=True, max_length=128, null=True, verbose_name='VK link')),
                ('site_link', models.CharField(blank=True, max_length=128, null=True, verbose_name='Website link')),
                ('image_dir', models.CharField(max_length=128, verbose_name='Image dir')),
                ('image_link', models.CharField(max_length=128, verbose_name='Image link')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Company name')),
                ('income', models.CharField(blank=True, max_length=16, null=True, verbose_name='Income')),
                ('growth', models.CharField(blank=True, max_length=8, null=True, verbose_name='Growth rate')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
                'db_table': 'ratings',
            },
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='admin_panel.company')),
            ],
            options={
                'verbose_name': 'Учетка компании',
                'verbose_name_plural': 'Учетки компании',
                'db_table': 'company_user',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
