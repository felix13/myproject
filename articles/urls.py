from django.urls import path

from articles import views


urlpatterns = [
    path('', views.articles, name='articles'),
    path('write/', views.write, name='write'),
    path('drafts/', views.drafts, name='drafts'),
    path('search/', views.search, name='search'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('article/<int:id>/', views.article, name='article'),
]
