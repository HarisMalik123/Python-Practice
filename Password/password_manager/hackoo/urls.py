


from django.contrib import admin
from django.urls import path
from hackoo import views

urlpatterns = [
    path('signup',views.toggle,name="signup"),
    path('login',views.index,name='index'),
    path('login_submit',views.login_submit,name='login_submit'),
    path('signup_submit',views.signup_submit,name='signup_submit'),
    path('admin/', admin.site.urls),
]