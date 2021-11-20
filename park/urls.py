from django.urls import path
from . import views
urlpatterns = [
    path('<str:pk>',views.home,name='park_home'),
    path('updateslot1/<str:pk>/<int:status>',views.update_slot_1,name='slot1update'),
    path('updateslot2/<str:pk>/<int:status>',views.update_slot_2,name='slot2update'),
]
