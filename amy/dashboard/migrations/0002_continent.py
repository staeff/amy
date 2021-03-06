# Generated by Django 2.1.2 on 2019-02-15 21:03

from django.db import migrations, models
import django_countries.fields


def add_initial_continents(apps, schema_editor):
    """Add initial continents."""

    Continent = apps.get_model('dashboard', 'Continent')
    data = [
        ('Africa',
         'DZ,AO,BJ,BW,BF,BI,CM,CV,CF,TD,KM,CD,DJ,EG,GQ,ER,ET,GA,GM,GH,GN,GW,'
         'CI,KE,LS,LR,LY,MG,MW,ML,MR,MU,YT,MA,MZ,NA,NE,NG,CG,RE,RW,SH,ST,SN,'
         'SC,SL,SO,ZA,SS,SD,SZ,TZ,TG,TN,UG,EH,ZM,ZW,TF'),
        ('Asia',
         'AF,AM,AZ,BH,BD,BT,BN,KH,CN,EG,GE,IN,ID,IR,IQ,IL,JP,JO,KZ,KP,KR,KW,'
         'KG,LA,LB,MY,MV,MN,MM,NP,OM,PK,PH,QA,RU,SA,SG,LK,SY,TJ,TH,TL,TR,TM,'
         'AE,UZ,VN,YE,IO,HK,MO,PS,TW,CX,CC'),
        ('Europe',
         'AL,AD,AM,AT,AZ,BY,BE,BA,BG,HR,CY,CZ,DK,EE,FI,FR,GE,DE,GR,HU,IS,IE,'
         'IT,KZ,LV,LI,LT,LU,MT,MD,MC,ME,NL,MK,NO,PL,PT,RO,RU,SM,RS,SK,SI,ES,'
         'SE,CH,TR,UA,GB,VA,AX,EU,FO,GI,GG,JE,SJ,IM'),
        ('North America',
         'AG,BS,BB,BZ,CA,CR,CU,DM,DO,SV,GD,GT,HT,HN,JM,MX,NI,PA,KN,LC,VC,TT,'
         'US,AI,BM,VG,KY,MS,PR,TC,VI,AW,BQ,CW,GL,GP,MQ,BL,MF,PM,SX'),
        ('South America', 'AR,BO,BR,CL,CO,EC,GY,PY,PE,SR,UY,VE,BV,FK,GS,GF'),
        ('Antarctica', 'AQ,HM'),
        ('Australia / Oceania',
         'AU,FM,FJ,KI,MH,NR,NZ,PW,PG,WS,SB,TO,TV,VU,CK,NU,AS,PF,GU,NC,NF,MP,'
         'PN,TK,WF,UM'),
    ]
    for datum in data:
        name, countries = datum
        Continent.objects.create(name=name, countries=countries)


def remove_initial_continents(apps, schema_editor):
    """Remove initial continents."""

    Continent = apps.get_model('dashboard', 'Continent')
    names = ['Africa', 'Asia', 'Europe', 'North America', 'South America',
             'Antarctica', 'Australia/Oceania']
    for name in names:
        Continent.filter(name=name).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('countries', django_countries.fields.CountryField(max_length=752, multiple=True, verbose_name='Countries in this continent')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Continents',
                'verbose_name': 'Continent',
            },
        ),
        migrations.RunPython(add_initial_continents,  # forward
                             remove_initial_continents),  # backward
    ]
