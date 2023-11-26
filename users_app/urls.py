from django.urls import path, include

from users_app.views import RegistrationView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('', include('rest_framework.urls'))
]