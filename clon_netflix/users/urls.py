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
]
