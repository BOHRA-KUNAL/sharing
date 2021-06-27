from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('courses/',views.course),
    path('blog/',views.blog),
    path('register/',views.register),
    path('contact',views.contact),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)