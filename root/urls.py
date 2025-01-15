from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from root.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT
from root.swagger import schema_view, swagger_urls

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^rosetta/', include('rosetta.urls')),

    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/v1/', include('app.urls')),


] + swagger_urls + static(MEDIA_URL, document_root=MEDIA_ROOT) + static(STATIC_URL,document_root=STATIC_ROOT)

