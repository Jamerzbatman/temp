from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('', include('pages.urls')),
    path('', include('base.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
