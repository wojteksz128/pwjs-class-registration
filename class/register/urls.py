from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('lectures/', views.lectures),
    path('subjects/', views.subjects),
    url(r'^subject/(?P<subject_id>\d+)$', views.getSubjectInfo, name='subject_info'),
    url(r'^lecture/(?P<lecture_id>\d+)$', views.getLectureInfo, name='lecture_info'),
    path('', views.main_window),
]