
from django.urls import path
from Convocatorias import views




app_name = "convocatorias"

urlpatterns = [
    # path(r'',views.IndexView.as_view(),
    #     name='convocatorias_index'),
    path('', views.index, name='convocatoria_index'),
    path('<int:id>/detail/', views.convocatoria_detail, name='convocatoria_detail'),
    ]