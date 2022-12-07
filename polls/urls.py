from django.urls import path, include

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResutlsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('owner/', views.owner, name='owner'),
]
