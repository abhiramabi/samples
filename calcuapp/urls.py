from . import views
from django.urls import path


urlpatterns = [
    path('',views.loadcalculatorpage,name='loadcalculatorpage'),
    path('calc',views.calc,name='calc')
]