from django.contrib import admin
from django.urls import path
from todo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("agregar/",views.agregar,name="agregar"),


    

]
