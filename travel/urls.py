
from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name='index'),
    path('charminar.html',views.charminar,name='charminar'),
    path('sarlarjung.html',views.sarlarjung,name='sarlarjung'),
    path('sanjeevaiahpark.html',views.sanjeevaiah,name='sanjeevaiah'),
    path('tankbund.html',views.tankbund,name='tankbund'),
    path('golkonda.html',views.golkonda,name='golkonda'),
    path('about.html',views.about,name='about'),
    path("index.html",views.index,name="index"),
    path("favicon.ico",views.fav,name="fav"),
    path("/",views.empty,name="empty"),
]
