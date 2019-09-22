from django.shortcuts import render, redirect

# Create your views here.
from evaluaciones.forms import EvaluacionForm, DocenteForm
from evaluaciones.models import EvaluacionProf, DocenteProf, AsignaturaProf
from users.views import *


def show(request):
    docente = DocenteProf.objects.all()
    return render(request, "users/buscarDocente.html", {'docentes':  docente})


def edit(request, id):
    docente = DocenteProf.objects.get(id=id)
    return render(request, 'users/edit.html', {'docente': docente})


def formulario(request):
    asignatura = AsignaturaProf.objects.all()
    return render(request, "users/formulario.html", {'asignaturas':  asignatura})


def showEvaluaciones(request):
    evaluaciones = EvaluacionProf.objects.all()
    return render(request, "users/buscarDocente.html", {'evaluaciones':  evaluaciones})


def update(request, id):
    docente = DocenteProf.objects.get(id=id)
    if docente.comentarios(null=True):
        print("WACHOOO ENTRÉ AL IFFF")
    else:
        print("NO ENTRÉ AL IF WACHO, SORRY")
    print("ENTRÉ A LA FUNCION UPDATEEE")
    form = DocenteForm(request.POST, instance=docente)
    if form.is_valid():
        comentario = docente.comentarios + ";" + request.POST['comentarios']
        print("ESTE ES EL COMENTARIO QUE ESTOY INTENTANDO CREAR : " + comentario)
        docente.comentarios = comentario
        form.save()
        docente.save()
        print("Comentario añadido satisfactoriamente")
    return render(request, "users/principalUser.html", {})