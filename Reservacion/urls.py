
from django.urls import path
from Reservacion import views




app_name = "reservaciones"

urlpatterns = [
    # path(r'',views.IndexView.as_view(),
    #     name='convocatorias_index'),
    path('', views.index, name='reservaciones'),
    path('reservar/', views.reservar, name='reservar'),
    path('<int:id>/', views.reservacion_detail, name='detail'),
    path('<int:id>/edit/', views.reservacion_edit, name='edit'),
     path('<int:id>/delete/', views.reservacion_delete, name='delete'),
    ]