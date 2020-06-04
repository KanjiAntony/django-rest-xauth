# Generated by Django 3.0.6 on 2020-05-29 22:20

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import xauth.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(db_index=True, max_length=150, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=150, unique=True)),
                ('surname', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('provider', models.CharField(
                    choices=[('EMAIL', 'EMAIL'), ('GOOGLE', 'GOOGLE'), ('FACEBOOK', 'FACEBOOK'), ('TWITTER', 'TWITTER'),
                             ('GITHUB', 'GITHUB'), ('APPLE', 'APPLE'), ('PHONE', 'PHONE')], default='EMAIL',
                    max_length=20)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all '
                                                            'permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user',
                                                            to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('created_at', 'updated_at', 'username'),
            },
        ),
        migrations.CreateModel(
            name='SecurityQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, unique=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('usable', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('added_on',),
            },
        ),
        migrations.CreateModel(
            name='PasswordResetLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type',
                 models.CharField(choices=[('CHANGE', 'CHANGE'), ('RESET', 'RESET')], default='RESET', max_length=10)),
                ('request_ip', models.GenericIPAddressField(blank=True, db_index=True, null=True, unpack_ipv4=True)),
                ('change_ip', models.GenericIPAddressField(blank=True, db_index=True, null=True, unpack_ipv4=True)),
                ('request_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('change_time', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-request_time', '-change_time', '-request_ip', '-change_ip'),
            },
        ),
        migrations.CreateModel(
            name='FailedSignInAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_ip', models.GenericIPAddressField(blank=True, db_index=True, null=True, unpack_ipv4=True)),
                ('attempt_date', models.DateField(default=django.utils.timezone.now)),
                ('attempt_count', models.IntegerField(default=1)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-attempt_date',),
            },
        ),
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_in_ip', models.GenericIPAddressField(blank=True, db_index=True, null=True, unpack_ipv4=True)),
                ('sign_out_ip', models.GenericIPAddressField(blank=True, db_index=True, null=True, unpack_ipv4=True)),
                ('sign_in_time', models.DateTimeField(blank=True, null=True)),
                ('sign_out_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-sign_in_ip', '-sign_out_ip', '-sign_in_time', '-sign_out_time'),
            },
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('user',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to=settings.AUTH_USER_MODEL)),
                ('security_question_answer', models.CharField(max_length=128, null=True)),
                ('temporary_password', models.CharField(max_length=128, null=True)),
                ('verification_code', models.CharField(max_length=128, null=True)),
                ('tp_gen_time',
                 models.DateTimeField(blank=True, null=True, verbose_name='temporary password generation time')),
                ('vc_gen_time',
                 models.DateTimeField(blank=True, null=True, verbose_name='verification code generation time')),
                ('deactivation_time',
                 models.DateTimeField(blank=True, null=True, verbose_name="user account's deactivation time")),
                ('security_question', models.ForeignKey(default=xauth.models.default_security_question,
                                                        on_delete=django.db.models.deletion.SET_DEFAULT,
                                                        to='xauth.SecurityQuestion')),
            ],
        ),
    ]
