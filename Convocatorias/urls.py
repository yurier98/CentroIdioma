from django.urls import path

from Convocatorias import views

app_name = "convocatorias"

urlpatterns = [
    # path(r'',views.IndexView.as_view(),
    #     name='convocatorias_index'),
    # path('', views.index, name='convocatorias'),

    path('', views.ConvocatoriasView.as_view(), name='convocatorias'),
    path('detail/<int:pk>/', views.DetailConvocatoria, name='convocatoria_detail'),
    # path('detail/<int:pk>/', views.ConvocatoriaDetailView.as_view(), name='convocatoria_detail'),
    # path('detail/<uuid:id_convocatoria>/', views.ConvocatoriaDetailView.as_view(), name='convocatoria_detail'),
    # path('detail/(?P<id_convocatoria>[\w\d-]+)/$', views.ConvocatoriaDetailView.as_view(), name='convocatoria_detail'),

    path('inscripciones/', views.inscripciones, name='inscripciones_index'),
    # esto no se hace   path('inscripciones/<int:id>/edit/', views.inscripcion_edit, name='inscripcion_edit'),
    path('inscripciones/<int:id>/delete/', views.inscripcion_delete, name='inscripcion_delete'),

]
