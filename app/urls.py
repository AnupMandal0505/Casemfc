
from django.urls import path
from .views import index,contact_us

urlpatterns = [
    path("",index.home,name = "home"),
    path("contact_us",contact_us.contact_us,name = "contact_us"),
 
]