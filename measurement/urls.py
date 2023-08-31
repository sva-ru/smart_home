from django.urls import path

from measurement.views import SensorView, MeasurementView, SingleSensorView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SingleSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),

]
