from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('GestionBibliotheque.urls')),
    path('', RedirectView.as_view(url='/gestion/tableau_de_bord/', permanent=True)),  # Rediriger vers le tableau de bord
]
