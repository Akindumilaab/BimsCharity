from django.urls import path
from .views import *

urlpatterns = [
    path('create-cause/', addcauseView, name='create-cause'),
    path('all-cause/', allcauses, name= 'all-cause'),
    path('edit-cause/<int:id>/', editcauseView, name='edit-cause' ),
    path('delete-cause/<int:id>/', deletecauseView, name='delete-cause' )
]