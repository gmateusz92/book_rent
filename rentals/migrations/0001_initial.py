# Generated by Django 4.2.6 on 2023-10-27 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('#0', 'rented'), ('#0', 'returned'), ('#', 'lost'), ('3', 'delayed')], max_length=2)),
                ('rent_start_date', models.DateField(help_text='when the book was rented')),
                ('rent_end_date', models.DateField(blank=True, help_text='deadline')),
                ('return_date', models.DateField(blank=True, help_text='actual return date', null=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
    ]