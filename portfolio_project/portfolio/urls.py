from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "portfolio"   # 🔥 THIS LINE IS CRITICAL

urlpatterns = [
    # Portfolio routes
    path("", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    path("skills/", views.skills, name="skills"),
    path("experience/", views.experience, name="experience"),
    path("contact/", views.contact, name="contact"),
   
    # Favicon route
    path("favicon.ico", RedirectView.as_view(
        url="/static/images/favicon.ico", permanent=True)),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)