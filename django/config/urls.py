from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views


schema_view = get_swagger_view(title='WiKi Pages API')

urlpatterns = [
    path('login/', views.obtain_auth_token, name='login'),
    path('admin/', admin.site.urls),
    path('docs/', schema_view),
    path('', include('pages.urls', namespace='pages')),
]
