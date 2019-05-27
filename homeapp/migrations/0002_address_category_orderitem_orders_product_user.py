# Generated by Django 2.0.6 on 2019-05-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('consignee', models.CharField(blank=True, max_length=50, null=True)),
                ('detailaddress', models.CharField(blank=True, max_length=100, null=True)),
                ('postalcode', models.CharField(blank=True, max_length=10, null=True)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('mobilephone', models.CharField(blank=True, max_length=20, null=True)),
                ('extend', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('parent_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('productname', models.CharField(blank=True, db_column='productName', max_length=100, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('amount', models.BigIntegerField(blank=True, null=True)),
                ('subtotal', models.FloatField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'orderitem',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('ordernumber', models.CharField(blank=True, db_column='orderNumber', max_length=100, null=True)),
                ('dateinproduct', models.DateTimeField(blank=True, db_column='dateInProduct', null=True)),
                ('freight', models.FloatField(blank=True, null=True)),
                ('expenditure', models.FloatField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('face', models.CharField(blank=True, max_length=100, null=True)),
                ('publishing_house', models.CharField(blank=True, max_length=50, null=True)),
                ('edition', models.SmallIntegerField(blank=True, null=True)),
                ('publishing_time', models.DateTimeField(blank=True, null=True)),
                ('print_time', models.SmallIntegerField(blank=True, null=True)),
                ('isbn', models.CharField(blank=True, max_length=30, null=True)),
                ('word', models.CharField(blank=True, max_length=20, null=True)),
                ('number_of_page', models.IntegerField(blank=True, null=True)),
                ('format_of_book', models.CharField(blank=True, max_length=20, null=True)),
                ('paper', models.CharField(blank=True, max_length=20, null=True)),
                ('packagin', models.CharField(blank=True, max_length=20, null=True)),
                ('emboitement', models.CharField(blank=True, max_length=10, null=True)),
                ('sales', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('dangdang_price', models.FloatField(blank=True, null=True)),
                ('review', models.BigIntegerField(blank=True, null=True)),
                ('issue', models.DateTimeField(blank=True, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
                ('sold_out', models.CharField(blank=True, max_length=10, null=True)),
                ('recommand', models.CharField(blank=True, max_length=10, null=True)),
                ('extend', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('nickname', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('extend', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'user',
            },
        ),
    ]