from unicodedata import name
from django.urls import URLPattern, path

from studyapp import settings
from . import views

urlpatterns = [
    
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('register/',views.registerPage, name="register"),
    path('',views.home,name="home"),
    path('mentor/',views.home_mentor,name="home_mentor"),
    path('room/<str:pk>/',views.room,name="room"),
    path('room_mentor/<str:pk>/',views.room2,name="room2"),
    path('profile/<str:pk>',views.userProfile,name="user-profile"),
    path('mentorprofile/<str:pk>',views.mentorProfile,name="mentor-profile"),
    path('create-room/' , views.createRoom , name="create-room"),
    path('update-room/<str:pk>/' , views.updateRoom , name="update-room"),
    path('delete-room/<str:pk>/' , views.deleteRoom , name="delete-room"),
    path('delete-message/<str:pk>/' , views.deleteMessage , name="delete-message"),
    path('update-user/' , views.updateUser , name="update-user"),
     path('update-mentor/' , views.updateMentor , name="update-mentor"),
     path('topics/' , views.topicsPage , name="topics"),
      path('activity/' , views.activityPage , name="activity"),
       path('courses/' , views.video , name="courses"),
        path('subscription/' , views.subscription , name="subscription"),
    path('dashboard/<str:pk>/',views.analysisDashboard,name='analysis-dashboard') ,
    path('user_interests/<int:user_id>/', views.user_interests, name='user_interests'),   
    path('upload/', views.upload_video, name='upload_video'),
    path('list/', views.video_list, name='video_list'),
    path('list_student/', views.video_list_student, name='video_list_student'),
    path('upload_document/', views.upload_document, name='upload_document'),
    path('document_list/', views.document_list, name='document_list'),
    path('user_rooms_timeline/', views.user_rooms_timeline_graph, name='user_rooms_timeline_graph'),
     path('public_documents/', views.document_list_public, name='public_documents'),
      path('edit-document/<int:document_id>/', views.edit_document, name='edit_document'),
        

]
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)