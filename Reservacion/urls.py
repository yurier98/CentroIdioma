from django.urls import path

from Reservacion import views

app_name = "reservaciones"

urlpatterns = [
    # path(r'',views.IndexView.as_view(),
    #     name='convocatorias_index'),
    # path('', views.index, name='reservaciones'),
    # path('', views.ReservacionesView.as_view(), name='reservaciones'),
    path('', views.ReservacionesView.as_view(), name='reservaciones'),
    path('new/', views.ReservacionCreate.as_view(), name='reservar'),
    # path('new/', views.Create, name='reservar'),

    path('detail/<uuid:pk>', views.DetailReservacion.as_view(), name='detail'),
    path('edit/<uuid:pk>', views.ReservacionUpdate.as_view(), name='update'),
    path('delete/<uuid:pk>', views.ReservacionDelete.as_view(), name='delete'),
]
