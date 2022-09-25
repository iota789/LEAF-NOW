from atexit import register
from multiprocessing.spawn import import_main_path
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('donate/',views.donate,name='donate'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('buy/',views.buy,name='buy'),
    path('discussion/',views.disc,name='disc'),
    path('plants/',views.plants,name='plants'),
    path('seeds/',views.seeds,name='seeds'),
    path('sell/',views.sell,name='sell'),
    path('cart/',views.cart,name='cart'),
    path("signup/",views.signup, name="signup"),
    path('login/',views.login1,name='login1'),
    path('fm1/',views.fm1,name='fm1'),
    path('fm2/',views.fm2,name='fm2'),
    path('logout/',views.logout1,name='logout1'),
    path('yay/',views.yay,name='yay'),

    ]
