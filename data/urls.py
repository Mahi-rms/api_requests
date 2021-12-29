from django.urls import include, path
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("new",views.AddData,name="task/new"),
    path("all",views.ShowData,name="task/all"),
]