# Generated by Django 3.0.5 on 2020-05-08 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0010_auto_20200503_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommodityTaifex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_id', models.CharField(max_length=100, verbose_name='商品代號')),
                ('spot_id', models.CharField(max_length=100, null=True, verbose_name='現貨代號')),
                ('stock_name', models.CharField(max_length=100, verbose_name='商品名稱')),
                ('check_fc', models.BooleanField(default=False, verbose_name='期貨商品')),
                ('check_opt', models.BooleanField(default=False, verbose_name='選擇權商品')),
                ('check_sii', models.BooleanField(default=False, verbose_name='上市商品')),
                ('check_otc', models.BooleanField(default=False, verbose_name='上櫃商品')),
                ('check_etf', models.BooleanField(default=False, verbose_name='ETF商品')),
                ('spot_unit', models.FloatField(blank=True, null=True, verbose_name='契約現貨單位')),
            ],
        ),
        migrations.CreateModel(
            name='Stock3PRatioTW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_id', models.CharField(max_length=100, verbose_name='證券代號')),
                ('date', models.DateField(verbose_name='資料日期')),
                ('stock_name', models.CharField(max_length=100, null=True, verbose_name='證券名稱')),
                ('dividend_yield', models.FloatField(blank=True, null=True, verbose_name='殖利率')),
                ('pe', models.FloatField(blank=True, null=True, verbose_name='本益比')),
                ('pb', models.FloatField(blank=True, null=True, verbose_name='本淨比')),
            ],
        ),
        migrations.AlterField(
            model_name='brokerinfotw',
            name='address',
            field=models.CharField(max_length=500, verbose_name='券商地址'),
        ),
        migrations.AlterField(
            model_name='companybasicinfotw',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='公司總部地址'),
        ),
        migrations.AlterField(
            model_name='companybasicinfotw',
            name='dividend_frequency',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='普通股盈餘分派或虧損撥補頻率'),
        ),
        migrations.AlterField(
            model_name='companybasicinfotw',
            name='english_abbreviation',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='英文簡稱'),
        ),
        migrations.AlterField(
            model_name='companybasicinfotw',
            name='market',
            field=models.CharField(default=None, max_length=100, verbose_name='市場別'),
        ),
        migrations.AlterField(
            model_name='companybasicinfotw',
            name='registered_country',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='企業註冊地國'),
        ),
        migrations.AlterField(
            model_name='companybasicinfotw',
            name='stock_transfer_institution',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='股票過戶機構'),
        ),
        migrations.AlterField(
            model_name='companybasicinfotw',
            name='visa_accounting_firm',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='簽證會計師事務所'),
        ),
        migrations.AlterField(
            model_name='stockmargintransactionstw',
            name='note',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='官方註記'),
        ),
        migrations.AlterField(
            model_name='stocktiimarketreporttw',
            name='market',
            field=models.CharField(default=None, max_length=100, verbose_name='市場別'),
        ),
        migrations.CreateModel(
            name='FuturePriceTW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_id', models.CharField(max_length=100, verbose_name='商品代號')),
                ('date', models.DateField(verbose_name='資料日期')),
                ('contract_date', models.CharField(max_length=100, null=True, verbose_name='契約日期')),
                ('open', models.FloatField(blank=True, null=True, verbose_name='開盤價')),
                ('high', models.FloatField(blank=True, null=True, verbose_name='最高價')),
                ('low', models.FloatField(blank=True, null=True, verbose_name='最低價')),
                ('close', models.FloatField(blank=True, null=True, verbose_name='收盤價')),
                ('quote_change', models.FloatField(blank=True, null=True, verbose_name='漲跌幅')),
                ('turnover_vol', models.FloatField(blank=True, null=True, verbose_name='成交量')),
                ('settlement_price', models.FloatField(blank=True, null=True, verbose_name='結算價')),
                ('open_interest', models.FloatField(blank=True, null=True, verbose_name='未沖銷契約數')),
                ('best_bid', models.FloatField(blank=True, null=True, verbose_name='最後最佳買價')),
                ('best_ask', models.FloatField(blank=True, null=True, verbose_name='最後最佳賣價')),
                ('trading_halt', models.CharField(max_length=100, null=True, verbose_name='暫停交易')),
                ('trading_session', models.CharField(max_length=100, null=True, verbose_name='交易時段')),
                ('cross_contract_vol', models.FloatField(blank=True, null=True, verbose_name='價差對單式委託成交量')),
                ('commodity_info', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crawlers.CommodityTaifex', verbose_name='公司資訊')),
            ],
        ),
        migrations.AddField(
            model_name='commoditytaifex',
            name='company_info',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crawlers.CompanyBasicInfoTW', verbose_name='公司資訊'),
        ),
    ]