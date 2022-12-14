from django.urls import path , include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('category-list',views.category_list,name='category-list'),
    path('branch-list',views.branch_list,name='branch-list'),
    path('competition-list',views.competition_list,name='competition-list'),
]
  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)