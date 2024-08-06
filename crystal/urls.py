
from landing_page.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index),
    path('add_comment/', add_comment),
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
    path('Logout/', Logout, name='Logout'),
    path('appointments/', appointments, name='appointments'),
    path('delete_book/<int:ID>', delete_book, name='delete_book'),
    path('update_book/', update_book, name='update_book')
]
