from django.db import models


# Create your models here.
class EvaluacionProf(models.Model):
    docente = models.CharField(max_length=255, default='')
    periodo = models.CharField(max_length=255, default='')
    asignatura = models.CharField(max_length=255, default='')
    matriculados = models.IntegerField(default=0)
    evaluaron = models.IntegerField(default=0)
    p9 = models.CharField(max_length=255, default='')
    p10 = models.CharField(max_length=255, default='')
    p11 = models.CharField(max_length=255, default='')
    p12 = models.CharField(max_length=255, default='')
    p13 = models.CharField(max_length=255, default='')
    p14 = models.CharField(max_length=255, default='')
    p15 = models.CharField(max_length=255, default='')
    p16 = models.CharField(max_length=255, default='')
    p17 = models.CharField(max_length=255, default='')
    p18 = models.CharField(max_length=255, default='')
    p19 = models.CharField(max_length=255, default='')
    p20 = models.CharField(max_length=255, default='')
    promedio = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 'evaluaciones'

    def get_full_name(self):
        # usado para obtener el nombre completo
        return self.docente

    def get_short_name(self):
        # usado para obtener el nombre corto
        return self.docente

    def get_id(self):
        return self.id

    def __str__(self):
        # Djando usa esto cuando necesita convertir objecs a string
        return self.docente


class DocenteProf(models.Model):
    nombre = models.CharField(max_length=255, default='')
    asignatura = models.CharField(max_length=255, default='')
    comentarios = models.CharField(max_length=500, default='')

    class Meta:
        db_table = 'docentes'

    def __str__(self):
        # Djando usa esto cuando necesita convertir objecs a string
        return self.nombre

    def get_comentario(self):
        return self.comentarios


class AsignaturaProf(models.Model):
    nombre = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 'asignaturas'

    def __str__(self):
        # Djando usa esto cuando necesita convertir objecs a string
        return self.nombre