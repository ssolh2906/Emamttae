from django.urls import path, re_path
from .views import BoardLV, Board_POSTLV
from . import views

app_name = 'board'

urlpatterns = [
    # example : /board/
    path('', BoardLV.as_view(), name='index'),

    # example : /board/slug-example/
    re_path(r'^(?P<slug>[-\w]+)/$', views.Board_POSTLV.as_view(), name='board_detail'),

    # example : /board/slug-example/add
    re_path(r'^/add/$', views.PostCreatedView.as_view(), name='add'),

    re_path(r'^(?P<slug>[-\w]+)/(?P<week>\d{2})/$', views.Board_POSTLV_otherweeks.as_view(), name='otherweeks'),

    # example : /board/slug-example/24
    re_path(r'^(?P<slug>[-\w]+)/add/<int:week>/', views.PostCreatedView.as_view(), name='by_week'),
]