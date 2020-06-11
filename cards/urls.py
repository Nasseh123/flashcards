from django.urls import path
from . import views
from django.conf import settings
from  django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path(r'newsubject/',views.newsubject,name='newsubject'),
    path('new/card', views.new_card, name='new_card'),
    path(r'subject/<subject>',views.subject,name='subject')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)