"""new_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from studentapp import views

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'course', views.CourseViewSet)
router.register(r'checkpoint', views.CheckpointViewSet)

urlpatterns = [
    path('', views.index),
    path('api/', include(router.urls)),
    path('vue', views.index_vue),
    path('api/student/', views.student_json),
    path('api/student/<int:pk>', views.student_json),
    path('api/course/', views.course_json),
    path('api/post_mark/', views.post_mark),
    #path('course/<int:pk>/', views.CourseDetail.as_view(),name="course-detail2"),
    path('course/', views.CourseList.as_view(),name="course-list2",),
    path('student/<int:pk>/', views.StudentDetail.as_view(),name="student-detail2"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
