from django.urls import path

from .views import Register, ListUsers

# urlpatterns = [
#     path('login/', login_view),
#     path('logout/', logout_view)
# ]

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', Register.as_view()),
    path('listUsers/', ListUsers.as_view())
]