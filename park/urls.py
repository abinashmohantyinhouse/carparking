from django.urls import path
from . import views
urlpatterns = [
    path('<str:pk>',views.home,name='park_home'),
    path('updateslot1/<str:pk>/<int:status>',views.update_slot_1,name='slot1update'),
    path('updateslot2/<str:pk>/<int:status>',views.update_slot_2,name='slot2update'),
    path('getslot1/<str:pk>',views.get_slot_1,name='slot1get'),
    path('getslot2/<str:pk>',views.get_slot_2,name='slot2get'),
]
