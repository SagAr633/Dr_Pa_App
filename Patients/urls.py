from django.urls import path
from Patients import views

urlpatterns = [

    path('pat_dash', views.Patient_Detail_View.as_view(), name='pat_dash'),
    path('signout2', views.signout, name='signout2'),
    path('all-blogs', views.AllBlogsListView.as_view(), name='all-blogs'),
    path('mental', views.MentalHealthView.as_view(), name='mental'),
    path('heart', views.HeartDiseaseView.as_view(), name='heart'),
    path('covid', views.Covid19View.as_view(), name='covid'),
    path('immune', views.ImmunizationView.as_view(), name='immune'),
    path('pat_details',views.PatientDetailsView.as_view(), name='pat-details'),
]
