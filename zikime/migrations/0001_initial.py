# Generated by Django 3.2.9 on 2021-11-20 12:17

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import zikime.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gps_module_info', models.CharField(db_column='GPS_INFO', help_text='This value is automatically entered by device connecting.', max_length=100, verbose_name='GPS 모듈 정보')),
                ('camera_module_info', models.CharField(db_column='CAMERA_INFO', help_text='This value is automatically entered by device connecting.', max_length=100, verbose_name='카메라 모듈 정보')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='CRE_DT', help_text='This value is automatically entered when the table is created.', null=True, verbose_name='기기 등록 날짜')),
            ],
            options={
                'verbose_name': '디바이스 정보',
                'verbose_name_plural': '디바이스 정보',
                'db_table': 'device_info',
            },
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(db_column='SerialID', help_text='This serial number must be unique.', max_length=50, unique=True, verbose_name='시리얼 번호')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='CRE_DT', help_text='This value is entered automatically.', null=True, verbose_name='생성 날짜')),
                ('deleted_at', models.DateTimeField(auto_now=True, db_column='DEL_DT', help_text='If you enter the date here, this device will no longer be available.', null=True, verbose_name='만료 날짜')),
            ],
            options={
                'verbose_name': '시리얼 정보',
                'verbose_name_plural': '시리얼 정보',
                'db_table': 'serial_info',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(db_column='Mode_ST', default='N', help_text='If the state is normal N is if the the state is emergency F is automatically entered.', max_length=1, verbose_name='디바이스 모드')),
                ('latitude', models.FloatField(db_column='Latitude_ST', default=0.0, help_text='This value is automatically entered by receiving the status of the connected device', verbose_name='위도')),
                ('longitude', models.FloatField(db_column='longitude_ST', default=0.0, help_text='This value is automatically entered by receiving the status of the connected device', verbose_name='경도')),
                ('altitude', models.FloatField(db_column='altitude_ST', default=0.0, help_text='This value is automatically entered by receiving the status of the connected device', verbose_name='고도')),
                ('latest_updated_at', models.DateTimeField(auto_now=True, db_column='UDA_DT', help_text='This value is automatically entered when the table is updated.', verbose_name='최근 업데이트한 시간')),
                ('ONF', models.BooleanField(db_column='ONF_ST', default=True, help_text='This vaule is automatically entered by receiving the status of the connected device', verbose_name='디바이스 On/Off')),
                ('IP', models.GenericIPAddressField(db_column='IP_INFO', null=True, verbose_name='IP')),
                ('device', models.OneToOneField(db_column='Device_ID', help_text='This value is automatically entered when the table is created.', on_delete=django.db.models.deletion.CASCADE, to='zikime.device', verbose_name='디바이스 시리얼 번호')),
            ],
            options={
                'verbose_name': '디바이스 상태',
                'verbose_name_plural': '디바이스 상태',
                'db_table': 'status_info',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자 리스트',
                'db_table': 'user',
                'ordering': ('username',),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('status_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='zikime.status')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='CRE_DT', help_text='This value is automatically entered when the table is created.', null=True, verbose_name='생성 날짜')),
            ],
            options={
                'verbose_name': '이전 상태 기록',
                'verbose_name_plural': '이전 상태 기록',
                'db_table': 'history_info',
            },
            bases=('zikime.status',),
        ),
        migrations.CreateModel(
            name='Regist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='CRE_DT', help_text='This value is automatically entered when the table is created.', null=True, verbose_name='관계 등록 날짜')),
                ('device', models.OneToOneField(db_column='Device_ID', help_text="TThis value is automatically entered when the table is created. owner's device id ", on_delete=django.db.models.deletion.CASCADE, to='zikime.device', verbose_name='디바이스 ID')),
                ('protector', models.OneToOneField(db_column='Proector_ID', help_text='This value must be entered by the owner or by the user specified by the owner.', on_delete=django.db.models.deletion.CASCADE, related_name='registered_protector', to='zikime.customuser', verbose_name='보호자')),
                ('protege', models.OneToOneField(db_column='Progete_ID', help_text='This value must be entered by the owner or by the user specified by the owner.', on_delete=django.db.models.deletion.CASCADE, related_name='registered_protege', to='zikime.customuser', verbose_name='피보호자')),
            ],
            options={
                'verbose_name': '등록 정보',
                'verbose_name_plural': '등록정보',
                'db_table': 'regist_info',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('protector', 'Protector'), ('protege', 'Protege'), ('observer', 'Observer'), ('other', 'Other')], db_column='ROLE_CD', help_text='This value is entered as a selected one of ROLE_CHOICES', max_length=10, verbose_name='사용자 권한 코드')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='CRE_DT', help_text='This value is automatically entered when the table is created.', null=True, verbose_name='생성날짜')),
                ('changed_at', models.DateTimeField(auto_now=True, db_column='CHG_DT', help_text='This value is automatically entered when the table is updated.', verbose_name='수정날짜')),
                ('device', models.ForeignKey(db_column='Device_ID', help_text='This value must be owner\\s device ID', on_delete=django.db.models.deletion.CASCADE, related_name='permission_device_id', to='zikime.device', verbose_name='사용자와 연결된 디바이스')),
                ('user', models.ForeignKey(db_column='User_ID', help_text='This value must be entered by the owner or by the user specified by the owner.', on_delete=django.db.models.deletion.CASCADE, related_name='permission_user_id', to='zikime.device', verbose_name='기기에 연결된 사용자')),
            ],
            options={
                'verbose_name': '권한 정보',
                'verbose_name_plural': '권한 정보',
                'db_table': 'permission_list',
            },
        ),
        migrations.AddField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(db_column='User_ID', default='-1', help_text='This value is automatically entered by device connecting.', on_delete=django.db.models.deletion.SET_DEFAULT, to='zikime.customuser', verbose_name='기기 소유주'),
        ),
        migrations.AddField(
            model_name='device',
            name='serial',
            field=models.OneToOneField(db_column='Serial_ID', help_text='This value is automatically entered by reference.', on_delete=django.db.models.deletion.CASCADE, to='zikime.serial', verbose_name='시리얼 번호'),
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('video', 'Video'), ('audio', 'Audio'), ('image', 'Image'), ('other', 'Other')], db_column='TYPE', help_text='This value is entered as a selected one of TYPE_CHOICES', max_length=10, verbose_name='미디어 타입')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='CRE_DT', help_text='This value is automatically entered when the table is created.', null=True, verbose_name='생성 날짜')),
                ('saved_path', models.FileField(db_column='SAVE_PATH', help_text='This value is entered by the file_path_for_db function.', upload_to=zikime.models.Attachment.file_path_for_db, verbose_name='경로')),
                ('device', models.ForeignKey(db_column='Device_ID', help_text='This value is automatically entered when the table is created.', on_delete=django.db.models.deletion.CASCADE, to='zikime.device', verbose_name='디바이스ID')),
                ('user', models.ForeignKey(db_column='Owner_ID', help_text='This value is automatically entered when the table is created.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='소유자 ID')),
            ],
            options={
                'verbose_name': '미디어 정보',
                'verbose_name_plural': '미디어 정보',
                'db_table': 'attachment_list',
            },
        ),
        migrations.AddConstraint(
            model_name='regist',
            constraint=models.UniqueConstraint(fields=('protector', 'protege', 'device'), name='unique regist'),
        ),
        migrations.AddConstraint(
            model_name='permission',
            constraint=models.UniqueConstraint(fields=('user', 'device'), name='unique permissions'),
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(db_column='UID', help_text='This value is automatically entered when the table is created.', on_delete=django.db.models.deletion.CASCADE, to='zikime.customuser', verbose_name='소유자'),
        ),
        migrations.AddConstraint(
            model_name='device',
            constraint=models.UniqueConstraint(fields=('serial', 'owner'), name='unique device'),
        ),
        migrations.AddConstraint(
            model_name='attachment',
            constraint=models.UniqueConstraint(fields=('device', 'user'), name='unique attachments'),
        ),
        migrations.AddConstraint(
            model_name='history',
            constraint=models.UniqueConstraint(fields=('created_at', 'user'), name='unique history'),
        ),
    ]
