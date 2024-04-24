from django.urls import path
from apis import views 

urlpatterns = [
    path('register',views.register,name="register"),
    path('login',views.login_page ,name="login"),
    path('logout',views.logout,name="logout")
    
]
