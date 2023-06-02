from django.urls import path
from .views import *


urlpatterns = [
    path('map/', stocker_polygone, name='stocker_polygone'),
    path('superviser/', superviser , name='superviser'  ),
    path('get_polygone/<str:id>', get_polygone , name='get_polygone'  ),
    path('consult/', all_project , name='all_project'  ),
    path('delete/<str:id>', delete , name='delete'  ),
    path('preject/', création_project , name='création_project'  ),
    path('node/<str:id>', node , name='node'  ),
    
    path('',compte,name='compte'),
]