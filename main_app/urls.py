from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Naming routes is best practice 
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name="finches"),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
]   