
from django.urls import path
from .views import auth, index,contact_us,dashboard,contact_message,Site_Maintenance,project,service,about

urlpatterns = [
    path("",index.home,name = "home"),
    path("contact_us",contact_us.contact_us,name = "contact_us"),
    path("about",about.about,name = "about"),
    path("signin",auth.signin,name = "signin"),
    path("signout",auth.signout,name = "signout"),
    path("dashboard",dashboard.dashboard,name = "dashboard"),
    path("message",contact_message.new_message,name = "message"),
    path("history",contact_message.history,name = "history"),
    path("site504",Site_Maintenance.site504,name = "site504"),
    path('project', project.project, name='project'),
    path('project_list', project.project_list, name='project_list'),
    path('project_create',project.project_create, name='project_create'),
    path('service', service.service, name='service'),
    path('service_list', service.service_list, name='service_list'),
    path('service_create',service.service_create, name='service_create'),
 
]