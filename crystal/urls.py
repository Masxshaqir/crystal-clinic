
from landing_page.views import add_comment, index
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('add_comment/', add_comment),
]
