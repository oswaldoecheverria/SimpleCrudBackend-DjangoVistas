
from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name="home"),
    # A la vista se llama a la funcion as_view() por que 
    #  despues sale un error 

    path('blog/', include('blog.urls', namespace='blog'))

    
]
