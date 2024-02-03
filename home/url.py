from django.contrib import admin
from django.urls import path,include
from home import views


urlpatterns = [
     path('',views.index,name='index'),
    path('base',views.base,name='base'),
     path('aboutus',views.aboutus,name='aboutus'),
      path('features',views.features,name='features'),
        path('prising',views.prising,name='prising'),
         path('trackorder',views.trackorder,name='trackorder'),
           path('login',views.login,name='login'),
              path('register',views.register,name='register'),
    path('international',views.international,name='international'),
    path('bulk',views.bulk,name='bulk'),
    path('hyperlocal',views.hyperlocal,name='hyperlocal'),
    path('ecommerce',views.ecommerce,name='ecommerce'),
    path('delta',views.delta,name='delta'),
    path('sprint',views.sprint,name='sprint'),
    path('faq',views.faq,name='faq'),
    path('glosary',views.glosary,name='glosary'),
    path('mediafeature',views.mediafeature,name='mediafeature'),
    path('single',views.single,name='single'),
    path('double',views.double,name='double'),
    path('triple',views.triple,name='triple')
]