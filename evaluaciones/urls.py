from django.conf.urls import url
from evaluaciones import views
from django.urls import include
from django.urls import path

urlpatterns = [
    path('', include('users.urls')),
    path('show/',views.show,name='show'),
    path('formulario/',views.formulario,name='formulario'),
    path('update/<int:id>', views.update, name='update'),
    path('edit/<int:id>', views.edit, name='edit'),
]