from django.contrib import admin
from django.urls import path,re_path
from booking.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'date/(?P<number>\d{1,2})$', home)
    path('date/<int:number>',home)
]