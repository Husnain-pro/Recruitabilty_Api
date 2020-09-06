# Recruitabilty_Api
Recruitability API with DRF


1: Make Virtal ENVIRONMENT
2: install django                   ==> pip install django
3: install djangorestframework      ==> pip install djangorestframework
4: run command                      ==> python manage.py makemigrations rec_profile
5: run command                      ==> python manage.py migrate rec_profile
6: run command                      ==> python manage.py createsuperuser
7: run command                      ==> python manage.py runserver
8: First Go to url                  ==> http://127.0.0.1:8000/admin

// enter email password 
// gave some values to database



  urlpatterns = [
    path('api/recruit/overview',views.RecruitOverview.as_view()),                           ==> http://127.0.0.1:8000/api/recruit/overview
    path('api/recruit/overview/<pk>',views.RecruitOverviewViewList.as_view()),              ==> http://127.0.0.1:8000/api/recruit/overview/1
    path('api/recruit/profile',views.ProfileView.as_view()), 
    path('api/recruit/profile/<pk>',views.ProfileViewList.as_view()), 
    path('api/recruit/profile_record/',views.ProfileRecView.as_view()), 
    path('api/recruit/profile_record/<pk>',views.ProfileRecViewList.as_view()), 
    path('api/recruit/factor',views.FactorView.as_view()),
    path('api/recruit/factor/<pk>',views.FactorViewList.as_view()),
    path('api/recruit/skills',views.SkillView.as_view()),

]