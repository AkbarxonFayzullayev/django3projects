
from django.contrib import admin
from django.urls import path

from app2_2.views import func1_11, func1_22, func1_33
from app2_1.views import func2_11, func2_22, func2_33
from app2_3.views import func3_11, func3_22, func3_33

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func11/', func1_11),
    path('admin12/', func1_22),
    path('func13/', func1_33),
    path('func13/', func2_11),
    path('func13/', func2_22),
    path('func13/', func2_33),
    path('func13/', func3_11),
    path('func13/', func3_22),
    path('func13/', func3_33),

]
