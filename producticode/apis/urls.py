from django.urls import path
from apis import views 

urlpatterns = [
    path('',views.say_hello)
    
]
