from django.db import models

# Create your models here.

class seguimiento(models.Model):
    NUMERO_DOCUMENTO=models.CharField(max_length=30)
    ID_ACTIVIDAD=models.CharField(max_length=30)
    ID_CURSO_DE_VIDA=models.CharField(max_length=30)
    EDAD=models.CharField(max_length=30)

class SeguimientoNominalNinio(models.Model):
    ID = models.BigIntegerField(primary_key=True)
    numero_documento = models.CharField(db_column='NUMERO_DOCUMENTO', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_actividad = models.IntegerField(db_column='id_ACTIVIDAD')  # Field name made lowercase.
    id_curso_de_vida = models.IntegerField(db_column='id_CURSO_DE_VIDA')  # Field name made lowercase.
    edad = models.IntegerField(db_column='EDAD', blank=True, null=True)  # Field name made lowercase.
    tipo_edad = models.CharField(db_column='TIPO_EDAD', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    renipress = models.CharField(max_length=12, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    cumple = models.CharField(db_column='CUMPLE', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mes = models.IntegerField(db_column='MES', blank=True, null=True)  # Field name made lowercase.
    anio = models.IntegerField(blank=True, null=True)
    id_indicador = models.IntegerField(db_column='id_INDICADOR', blank=True, null=True)  # Field name made lowercase.
    fecha_atencion = models.DateField(db_column='Fecha_Atencion', blank=True, null=True)  # Field name made lowercase.
    id_cita = models.CharField(db_column='Id_cita', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEGUIMIENTO_NOMINAL_VIEW'