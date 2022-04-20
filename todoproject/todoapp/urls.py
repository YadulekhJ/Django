
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cvhome/',views.todolistview.as_view(),name='cvhome'),
    path('cvdetail/<int:pk>/',views.tododetailview.as_view(),name='cvdetail'),
    path('cvupdate/<int:pk>/',views.todoupdateview.as_view(),name='cvupdate'),
    path('cvdelete/<int:pk>/',views.tododeleteview.as_view(),name='cvdelete')

]