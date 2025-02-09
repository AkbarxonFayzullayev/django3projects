
from django.contrib import admin
from django.urls import path

from app1.views import func1_1, func1_2, func1_3
from app2.views import func2_1, func2_2, func2_3
from app3.views import func3_1, func3_2, func3_3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func11/', func1_1),
    path('admin12/', func1_2),
    path('func13/', func1_3),
    path('func13/', func2_1),
    path('func13/', func2_2),
    path('func13/', func2_3),
    path('func13/', func3_1),
    path('func13/', func3_2),
    path('func13/', func3_3),

]
