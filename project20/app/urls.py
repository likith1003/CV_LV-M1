from django.urls import path
from .views import *
urlpatterns = [
    path('insert_school_by_FBV', insert_school_by_FBV, name='insert_school_by_FBV'),
    path('insert_school_by_cbv', insert_school_by_CBV.as_view(), name='insert_school_by_CBV'),
    path('School_list', school_list.as_view(), name='school_list')

]
