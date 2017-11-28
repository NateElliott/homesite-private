from django.conf.urls import url
from django.contrib import admin
from core.views import Root

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', Root.as_view()),
]
