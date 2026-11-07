from django.contrib import admin
from django.urls import path
from detector import views
urlpatterns=[
 path('admin/',admin.site.urls),
 path('',views.home,name='home'),
 path('register/',views.register_view,name='register'),
 path('login/',views.login_view,name='login'),
 path('logout/',views.logout_view,name='logout'),
 path('detect/',views.detect_view,name='detect'),
 path('result/<int:pk>/',views.result_view,name='result'),
 path('dashboard/',views.dashboard,name='dashboard'),
 path('history/',views.history,name='history'),
]
