from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
        path('<int:article_pk>/comment/create/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comment/<int:pk>/delete/', views.comment_delete, name = 'comment_delete'),
    path('<int:article_pk>/comment/<int:pk>/edit', views.comment_edit, name ='comment_edit'),
]
