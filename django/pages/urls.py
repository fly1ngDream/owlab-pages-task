from django.urls import path

# from rest_framework.authtoken import views

from .apiviews import (
    PageListView,
    PageDetailView,
    PageVersionListView,
    PageVersionDetailView,
    PageVersionCurrentDetailView,
)


app_name = 'pages'

urlpatterns = [
    # path('login/', views.obtain_auth_token, name='login'),
    path('', PageListView.as_view(), name='page_list'),
    path('<int:pk>/', PageDetailView.as_view(), name='post_detail'),
    path(
        '<int:pk>/versions/current/',
        PageVersionCurrentDetailView.as_view(),
        name='page_version_current',
    ),
    path(
        '<int:pk>/versions/<path:version>/',
        PageVersionDetailView.as_view(),
        name='page_version',
    ),
    path(
        '<int:pk>/versions/',
        PageVersionListView.as_view(),
        name='page_versions_list',
    ),
]
