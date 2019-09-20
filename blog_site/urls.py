from django.urls import path
from .views import home_view, about_view,register_view, login_view, logout_view, contact_view,profile_view, post_edit_view, dashboard_view,delete_view, post_view, usersettings_view



urlpatterns = [
   path('', home_view, name="home-view"),
   path('about/', about_view, name='about-view'),
   path('register/', register_view, name='register-view'),
   path('login/', login_view, name='login-view'),
   path('logout/',logout_view, name='logout-view'),
   path('contact/', contact_view, name="contact-view"),
   path('author/<str:slug>', profile_view, name = 'author-view'),
   path('post-edit/<int:id>/', post_edit_view, name='post-edit'),
   path('dashboard/', dashboard_view, name= 'dashboard-view'),
   path('dashboard/<int:id>', delete_view, name= 'delete-view'),
   path('post/<str:slug>', post_view, name= 'post-view'),
   path('usersettings/', usersettings_view, name='settings')
]
