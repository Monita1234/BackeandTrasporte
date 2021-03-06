# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CallDepartamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'call_departamento'


class CallFormapago(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'call_formapago'


class CallMunicipio(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    departamento = models.ForeignKey(CallDepartamento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'call_municipio'


class CallTipoidentificacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'call_tipoidentificacion'


class CallTiposervicio(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'call_tiposervicio'


class CotizacionesDepartamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cotizaciones_departamento'


class CotizacionesMunicipio(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    departamento = models.ForeignKey(CotizacionesDepartamento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cotizaciones_municipio'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class Envioguia(models.Model):
    id = models.BigAutoField(primary_key=True)
    numueroguia = models.CharField(max_length=50)
    identificacionremi = models.CharField(db_column='identificacionRemi', max_length=50)  # Field name made lowercase.
    nombreremi = models.CharField(db_column='nombreRemi', max_length=50)  # Field name made lowercase.
    direccionremi = models.TextField(db_column='direccionRemi')  # Field name made lowercase.
    telefonoremi = models.CharField(db_column='telefonoRemi', max_length=50)  # Field name made lowercase.
    correoremi = models.CharField(db_column='correoRemi', max_length=254)  # Field name made lowercase.
    identificaciondesti = models.CharField(db_column='identificacionDesti', max_length=50)  # Field name made lowercase.
    nombredesti = models.CharField(db_column='nombreDesti', max_length=50)  # Field name made lowercase.
    direcciondesti = models.TextField(db_column='direccionDesti')  # Field name made lowercase.
    telefonodesti = models.CharField(db_column='telefonoDesti', max_length=50)  # Field name made lowercase.
    correodesti = models.CharField(db_column='correoDesti', max_length=254)  # Field name made lowercase.
    peso = models.CharField(max_length=50)
    alto = models.CharField(max_length=50)
    ancho = models.CharField(max_length=50)
    largo = models.CharField(max_length=50)
    contiene = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    ciudaddesti = models.ForeignKey(CallMunicipio, models.DO_NOTHING, db_column='ciudadDesti_id')  # Field name made lowercase.
    ciudadremi = models.ForeignKey(CallMunicipio, models.DO_NOTHING, db_column='ciudadRemi_id')  # Field name made lowercase.
    formapagp = models.ForeignKey(CallFormapago, models.DO_NOTHING)
    tipoiddesti = models.ForeignKey(CallTipoidentificacion, models.DO_NOTHING, db_column='tipoIdDesti_id')  # Field name made lowercase.
    tipoidremitente = models.ForeignKey(CallTipoidentificacion, models.DO_NOTHING, db_column='tipoIdRemitente_id')  # Field name made lowercase.
    tiposervicio = models.ForeignKey(CallTiposervicio, models.DO_NOTHING, db_column='tipoServicio_id')  # Field name made lowercase.
    vehiculos = models.ForeignKey('VehiculosVehiculo', models.DO_NOTHING, blank=True, null=True)
    entregado = models.IntegerField()
    asignado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'envioguia'


class ServiciosDestinatario(models.Model):
    id = models.BigAutoField(primary_key=True)
    identificaciondesti = models.CharField(db_column='identificacionDesti', max_length=50)  # Field name made lowercase.
    nombredesti = models.CharField(db_column='nombreDesti', max_length=50)  # Field name made lowercase.
    direcciondesti = models.TextField(db_column='direccionDesti')  # Field name made lowercase.
    telefonodesti = models.CharField(db_column='telefonoDesti', max_length=50)  # Field name made lowercase.
    correodesti = models.CharField(db_column='correoDesti', max_length=254)  # Field name made lowercase.
    created = models.DateTimeField()
    updated = models.DateTimeField()
    ciudaddesti = models.ForeignKey(CotizacionesMunicipio, models.DO_NOTHING, db_column='ciudadDesti_id')  # Field name made lowercase.
    tipoiddesti = models.ForeignKey('ServiciosTipoidentificacion', models.DO_NOTHING, db_column='tipoIdDesti_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicios_destinatario'


class ServiciosEnvios(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    destinatario = models.ForeignKey(ServiciosDestinatario, models.DO_NOTHING)
    remitente = models.ForeignKey('ServiciosRemitente', models.DO_NOTHING)
    tiposervicio = models.ForeignKey('ServiciosTiposervicio', models.DO_NOTHING, db_column='tipoServicio_id')  # Field name made lowercase.
    unidades = models.ForeignKey('ServiciosUnidades', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'servicios_envios'


class ServiciosFormapago(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'servicios_formapago'


class ServiciosRemitente(models.Model):
    id = models.BigAutoField(primary_key=True)
    identificacionremi = models.CharField(db_column='identificacionRemi', max_length=50)  # Field name made lowercase.
    nombreremi = models.CharField(db_column='nombreRemi', max_length=50)  # Field name made lowercase.
    direccionremi = models.TextField(db_column='direccionRemi')  # Field name made lowercase.
    telefonoremi = models.CharField(db_column='telefonoRemi', max_length=50)  # Field name made lowercase.
    correoremi = models.CharField(db_column='correoRemi', max_length=254)  # Field name made lowercase.
    created = models.DateTimeField()
    updated = models.DateTimeField()
    ciudadremi = models.ForeignKey(CotizacionesMunicipio, models.DO_NOTHING, db_column='ciudadRemi_id')  # Field name made lowercase.
    tipoidremitente = models.ForeignKey('ServiciosTipoidentificacion', models.DO_NOTHING, db_column='tipoIdRemitente_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicios_remitente'


class ServiciosServicio(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    imagen = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'servicios_servicio'


class ServiciosTipoidentificacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'servicios_tipoidentificacion'


class ServiciosTiposervicio(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'servicios_tiposervicio'


class ServiciosUnidades(models.Model):
    id = models.BigAutoField(primary_key=True)
    peso = models.CharField(max_length=50)
    alto = models.CharField(max_length=50)
    ancho = models.CharField(max_length=50)
    largo = models.CharField(max_length=50)
    contiene = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    formapagp = models.ForeignKey(ServiciosFormapago, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'servicios_unidades'


class VehiculosTipovehiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vehiculos_tipovehiculo'


class VehiculosVehiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    placa = models.CharField(max_length=7)
    marca = models.CharField(max_length=50)
    conductor = models.ForeignKey(AuthUser, models.DO_NOTHING)
    tipo = models.ForeignKey(VehiculosTipovehiculo, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vehiculos_vehiculo'
