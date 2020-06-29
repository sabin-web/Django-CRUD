from django.urls import path
from .views import employee_list,employee_detail,employee_delete

urlpatterns = [
path('',employee_list),
path('<id>/',employee_detail),
path('<id>/delete/',employee_delete)

]