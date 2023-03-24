from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("contact/",views.contact,name="contact"),
    path("booking/",views.booking,name="booking"),
    path("doctors/",views.doctors,name="doctors"),
    path("department/",views.department,name="department"),
    path('signup/',views.signup,name='signup'),
    path('user_login/',views.user_login,name='user_login'),
]
