
from landing_page.views import add_comment, index, login_view, signup_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('add_comment/', add_comment),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]
