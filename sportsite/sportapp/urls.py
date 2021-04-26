
from django.urls import path

from sportapp import views


urlpatterns = [
    path('equipments/', views.equipmentsListView.as_view(), name='equipments'),
]
