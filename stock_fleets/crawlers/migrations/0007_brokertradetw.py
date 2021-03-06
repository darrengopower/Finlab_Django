# Generated by Django 2.2.8 on 2020-04-26 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0006_auto_20200426_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrokerTradeTW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_id', models.CharField(max_length=100, verbose_name='分點進出代號')),
                ('date', models.DateTimeField(verbose_name='資料日期')),
                ('buy_num', models.FloatField(blank=True, null=True, verbose_name='買進')),
                ('sell_num', models.FloatField(blank=True, null=True, verbose_name='賣出')),
                ('net_bs', models.FloatField(blank=True, null=True, verbose_name='買賣超')),
                ('transactions_pt', models.FloatField(blank=True, null=True, verbose_name='成交占比')),
                ('broker_info', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crawlers.BrokerInfoTW', verbose_name='券商資訊')),
            ],
        ),
    ]
