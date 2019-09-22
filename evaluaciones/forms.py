from django import forms
from evaluaciones.models import EvaluacionProf, DocenteProf, AsignaturaProf


class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = EvaluacionProf
        fields = ['docente', 'periodo', 'asignatura', 'matriculados', 'evaluaron', 'p9', 'p10', 'p11', 'p12', 'p13',
                  'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'promedio']


class DocenteForm(forms.ModelForm):
    class Meta:
        model = DocenteProf
        fields = ['nombre', 'asignatura', 'comentarios']


class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = AsignaturaProf
        fields = ['nombre']
