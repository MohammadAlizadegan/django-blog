from django.urls import path
from . import views
#from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    #registration
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login'),
    #ChangePassword
    #ResetPassword
    #LoginToken
    #Login JWT
]