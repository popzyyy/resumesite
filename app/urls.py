from django.conf.urls.static import static
from django.urls import path, include

from resumesite import settings
from . import views
from .views import *

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('webtools/', views.tools_home, name='tools_home'),
    path('gpacalculator/', GPACalc.as_view(), name='gpacalc'),
    path('gpacalculator/<int:pk>/', GPACalc.as_view(), name='gpacalc'),
    path('refresh/', views.refresh, name='refresh'),
    path('tools/', views.tools, name='tools'),
    path('inflationcalculator/', views.inflation, name='inflation'),
    path('calculators/', views.calculators, name='calculators'),
    path('onelinemaker/', views.line, name='line'),
    path('datecalculation/', views.date, name='date'),
    path('timecalculation/', views.time_view, name='time'),
    path('between_dates/', views.between_dates, name='between_dates'),
    path('ipaddress/', views.ipaddress, name='ipaddress'),
    path('memento_mori/', views.grim_reaper, name='grim'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
