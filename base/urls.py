from django.urls import path
from .views import (bar, line, bubble, doughnut,
                    scatter, radar)

urlpatterns = [
    path('bar/',bar, name='bar-chart'),
    path('line/',line, name='line-chart'),
    path('bubble/',bubble, name='bubble-chart'),
    path('doughnut/',doughnut, name='doughnut-chart'),
    path('scatter/',scatter, name='scatter-chart'),
    path('radar/',radar, name='radar-chart')
]