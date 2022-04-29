from django.urls import path,include
from users import views

urlpatterns = [
  

    path('',views.dashboard, name="dashboard"),
    path('addshipment/',views.addshipment, name="addshipment"),
    path('listshipment/',views.listshipment, name="listshipment"),
    path('viewshipment/<str:pk>/',views.viewshipment, name="viewshipment"),
    path('updateshipment/<str:pk>/',views.updateshipment, name="updateshipment"),
    path('deleteshipment/<str:pk>/',views.deleteshipment, name="deleteshipment"),
    path('searchshipment/',views.searchshipment, name="searchshipment"),
    path('queryshipment/',views.queryshipment, name="queryshipment"),
    path('inbox/', views.inbox, name= "inbox")
]
