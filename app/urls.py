
from django.urls import path
from .views import auth, index,contact_us,dashboard,contact_message,Site_Maintenance

urlpatterns = [
    path("",index.home,name = "home"),
    path("contact_us",contact_us.contact_us,name = "contact_us"),
    path("signin",auth.signin,name = "signin"),
    path("signout",auth.signout,name = "signout"),
    path("dashboard",dashboard.dashboard,name = "dashboard"),
    path("message",contact_message.new_message,name = "message"),
    path("history",contact_message.history,name = "history"),
    path("site504",Site_Maintenance.site504,name = "site504"),
 
]