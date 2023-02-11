
from django.contrib import admin
from django.urls import path, include
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', main_views.home, name='home'),
    path('register/', main_views.register, name='register'),
    path('add_review/', main_views.add_review, name='add_review'),
    path('recipes/', main_views.recipes, name='recipes'),
    path('recipes/<int:id>', main_views.recipe, name='recipe'),
    path('add/', main_views.add_recipe, name='add'),
    path('notfound/', main_views.notfound, name='notfound'),
    
]


urlpatterns += [path('accounts/', include('django.contrib.auth.urls'))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)