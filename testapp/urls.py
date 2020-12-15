from django.urls import path, include
from django.contrib import admin
from testapp import views
#from testApp.views import upload, ClubChartView, SectionB, SectionC, It, Civil, Mech, Elect, Average

urlpatterns = [
    path('',views.create,name='create'),
    path('read/',views.read,name='read'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
     path('update/<int:id>',views.update,name='edit'),
    #path("accounts/",include('django.contrib.auth.urls')),
]