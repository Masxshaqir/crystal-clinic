
from landing_page.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('add_comment/', add_comment),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('Logout/', Logout, name='Logout'),
    path('appointments/', appointments, name='appointments'),
    path('delete_book/<int:ID>', delete_book, name='delete_book'),
    path('update_book/', update_book, name='update_book'),
    path('add_appointment/', add_appointment, name='add_appointment'),
]
