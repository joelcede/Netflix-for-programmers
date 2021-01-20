from django.urls import path
from users import views

urlpatterns = [
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

    path(
        route='',
        view=views.InitNetflix.as_view(),
        name='init'
    ),

    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    )
    path(
        "update/",
        view=views.UpdateProfileView.as_view()
        name="update"
    )
    
]
