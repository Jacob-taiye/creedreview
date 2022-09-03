from django.urls.conf import path
from django.urls.resolvers import URLPattern
from. import views
urlpatterns=[
    path('home',views.index,name='index'),
    path('hollywood',views.hollywood,name='hollywood'),
    path('nollywood',views.nollywood,name='nollywood'),
    path('bollywood',views.bollywood,name='bollywood'),
    path('korean',views.korean,name='korean'),
    path('movie1',views.movie1,name='movie1'),
    path('movie2',views.movie2,name='movie2'),
    path('movie3',views.movie3,name='movie3'),
    path('movie4',views.movie4,name='movie4'),
    path('hollymovie1',views.movie4,name='hollymovie1'),
    path('hollymovie2',views.movie4,name='hollymovie2'),
    path('hollymovie3',views.movie4,name='hollymovie3'),
    path('hollymovie4',views.movie4,name='hollymovie4'),
    path('bollymovie1',views.movie4,name='bollymovie1'),
    path('bollymovie2',views.movie4,name='bollymovie2'),
    path('bollymovie3',views.movie4,name='bollymovie3'),
    path('bollymovie4',views.movie4,name='bollymovie4'),
    path('korea1',views.movie4,name='korea1'),
    path('korea2',views.movie4,name='korea2'),
    path('korea3',views.movie4,name='korea3'),
    path('korea4',views.movie4,name='korea4'),
]

