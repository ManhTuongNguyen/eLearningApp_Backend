# Generated by Django 4.1 on 2022-11-15 16:02

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCustom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('email_verified', models.BooleanField(default=False)),
                ('account_verified', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=300, null=True, verbose_name='Địa chỉ')),
                ('gender', models.PositiveSmallIntegerField(choices=[(0, 'Nam'), (1, 'Nữ'), (2, 'Khác')], default=0, verbose_name='Giới tính')),
                ('introduce', models.CharField(blank=True, max_length=300, null=True, verbose_name='Giới thiệu')),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('birth', models.DateField(blank=True, null=True)),
                ('previous_permission', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Chỉ định xem người dùng này phải được coi là đang hoạt động. Bạn nên bỏ chọn này thay vì xóa tài khoản.', verbose_name='Hoạt động')),
                ('is_staff', models.BooleanField(default=False, help_text='Chỉ định người dùng nào được phép truy cập vào trang admin.', verbose_name='Nhân viên')),
                ('is_superuser', models.BooleanField(default=False, help_text='Chỉ định rằng người dùng này có tất cả các quyền mà không gán cho họ một cách cụ thể.', verbose_name='Superuser')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Người dùng',
                'verbose_name_plural': 'Tất cả người dùng',
                'db_table': 'auth_user',
                'ordering': ['id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
