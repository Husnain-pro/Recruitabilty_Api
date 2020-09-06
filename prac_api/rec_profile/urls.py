from django.urls import include, path

from rec_profile import views

urlpatterns = [
    path('api/recruit/overview',views.RecruitOverview.as_view()), 
    path('api/recruit/overview/<pk>',views.RecruitOverviewViewList.as_view()), 
    path('api/recruit/profile',views.ProfileView.as_view()), 
    path('api/recruit/profile/<pk>',views.ProfileViewList.as_view()), 
    path('api/recruit/profile_record/',views.ProfileRecView.as_view()), 
    path('api/recruit/profile_record/<pk>',views.ProfileRecViewList.as_view()), 
    path('api/recruit/factor',views.FactorView.as_view()),
    path('api/recruit/factor/<pk>',views.FactorViewList.as_view()),
    path('api/recruit/skills',views.SkillView.as_view()),

]
