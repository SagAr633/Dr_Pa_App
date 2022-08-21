from django.urls import path
from Doctors import views

urlpatterns = [

    path('dr_dash', views.DoctorDashView.as_view(), name='dr_dash'),
    path('signout', views.signout, name='signout'),
    path('post_blog', views.DoctorBlogView.as_view(), name='post_blog'),
    path('user_blogs', views.DoctorBlogsListView.as_view(), name='user_blogs'),
    path('doc_details', views.DoctorDetailsView.as_view(), name='doc-details')

]
