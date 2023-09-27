from django.urls import path
from . import views

urlpatterns = [
    # path('prueba/<int:pk>', views.leer_id_y_retornar_json),
    path('', views.SnippetList.as_view()),
    path('<int:pk>', views.SnippetDetails.as_view())
]