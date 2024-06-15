from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'computacao'

urlpatterns = [
                  path('', views.index, name='index'),
                  path('index/', views.index, name='index'),
                  path('afd0/', views.afd0, name='afd0'),
                  path('automatos/', views.automatos, name='automatos'),
                  path('novo_automato/', views.novo_automato, name='novo_automato'),
                  path('edita_automato/<int:automato_id>/', views.edita_automato, name='edita_automato'),
                  path('apaga_automato/<int:automato_id>/', views.apaga_automato, name='apaga_automato'),
                  path('<int:automato_id>/automato/', views.automato, name='automato')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)