from django.urls import path
from .views import TodoappCreateView, TodoappListView, TodoappDetailView, TodoappUpdateView,TodoappDeleteView


urlpatterns =[
    path('', TodoappCreateView.as_view(), name='home'),
    path('list/', TodoappListView.as_view()),
    path('detail/<pk>/', TodoappDetailView.as_view()),
    path('update/<pk>/', TodoappUpdateView.as_view()),
    path('delete/<pk>', TodoappDeleteView.as_view()),
]