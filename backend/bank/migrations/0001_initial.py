# Generated by Django 3.0 on 2020-01-13 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'branches',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_options', models.CharField(choices=[('savings', 'SAVINGS'), ('checkings', 'CHECKINGS'), ('business', 'BUSINESS')], default=('savings', 'SAVINGS'), max_length=20)),
                ('account_type', models.CharField(choices=[('business', 'BUSINESS'), ('personal', 'PERSONAL'), ('charity', 'CHARITY')], default=('business', 'BUSINESS'), max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank', to='bank.Branch')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposite', models.DecimalField(decimal_places=1, max_digits=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Customer')),
            ],
        ),
    ]
