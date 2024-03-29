

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

# for admin text change
admin.site.site_header = "Abhi Admin"
admin.site.site_title = "Abhi Admin Portal"
admin.site.index_title = "Welcome to Abhi website"



urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include("home.url")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)