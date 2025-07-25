# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MappageDistrict(models.Model):
    code = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    province_code = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'MapPage_district'


class MappageProvince(models.Model):
    code = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'MapPage_province'


class MappageSubdistrict(models.Model):
    code = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    district_code = models.PositiveSmallIntegerField()
    is_island = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'MapPage_subdistrict'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class District(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.TextField()
    province_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'district'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Factory(models.Model):
    name = models.TextField(blank=True, null=True)
    registration_num = models.TextField(primary_key=True)
    type = models.TextField(blank=True, null=True)
    standard = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    subdistrict = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    province = models.TextField(blank=True, null=True)
    factory_phone_number = models.TextField(blank=True, null=True)
    owner_name = models.TextField(blank=True, null=True)
    owner_address = models.TextField(blank=True, null=True)
    owner_phone_number = models.TextField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    hp = models.FloatField(blank=True, null=True)
    capital = models.FloatField(blank=True, null=True)
    worker = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory'


class Factory2(models.Model):
    name = models.TextField(blank=True, null=True)
    registration_num = models.TextField(primary_key=True)
    type = models.TextField(blank=True, null=True)
    standard = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    subdistrict = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    province = models.TextField(blank=True, null=True)
    factory_phone_number = models.TextField(blank=True, null=True)
    owner_name = models.TextField(blank=True, null=True)
    owner_address = models.TextField(blank=True, null=True)
    owner_phone_number = models.TextField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    capital = models.FloatField(blank=True, null=True)
    worker = models.IntegerField(blank=True, null=True)
    lat = models.IntegerField(blank=True, null=True)
    lng = models.IntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory2'


class FactoryCoordinates(models.Model):
    registration_num = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    type = models.FloatField(blank=True, null=True)
    standard = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    subdistrict = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    province = models.TextField(blank=True, null=True)
    factory_phone_number = models.TextField(blank=True, null=True)
    owner_name = models.TextField(blank=True, null=True)
    owner_address = models.TextField(blank=True, null=True)
    owner_phone_number = models.TextField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    hp = models.FloatField(blank=True, null=True)
    capital = models.FloatField(blank=True, null=True)
    worker = models.IntegerField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory_coordinates'


class FactoryType(models.Model):
    code = models.TextField(primary_key=True)
    num = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    class1 = models.TextField(blank=True, null=True)
    class2 = models.TextField(blank=True, null=True)
    class3 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory_type'


class Province(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'province'


class Subdistrict(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.TextField()
    district_code = models.IntegerField()
    is_island = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subdistrict'

class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    franchise = models.TextField(blank=True, null=True)
    branch_name = models.TextField(blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    branch_type = models.TextField(blank=True, null=True)
    format = models.TextField(blank=True, null=True)
    owner = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    province = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    subdistrict = models.TextField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store'
