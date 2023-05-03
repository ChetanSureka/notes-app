from django.urls import path
import api.views as views

urlpatterns = [
    path('notes/', views.getNotes, name='getNotes'),
    path('notes/<str:pk>', views.getNote, name='getNote'),
]
