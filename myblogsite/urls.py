from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("new/", views.create_post, name="create_post"),
    path("edit/<int:pk>/", views.edit_post, name="edit_post"),
    path("delete/<int:pk>/", views.delete_post, name="delete_post"),
    path("students/", include("students.urls")),
    path("accounts/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
