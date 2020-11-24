from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('driver/',include('driver.urls')),
    path('owner/',include('owner.urls')),
    path('passenger/', include('passenger.urls'))
]
