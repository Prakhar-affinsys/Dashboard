from django.urls import path, include
from django.conf.urls import url
from .views import *

from django.views.generic import TemplateView
from demo.views import testview


urlpatterns =[
path('click/', NameViews.as_view(),name='nameviews'),
#url('^dash_plot$', TemplateView.as_view(template_name='index.html'), name="dash_plot"),
#url('^django_plotly_dash/', include('django_plotly_dash.urls')),
path('plot/',Analytics.as_view(),name='analyticsview'),
path('plot1/',Dashboard.as_view(),name='dashboardview'),
path('plot2/',Dashboard_canny.as_view(),name='dashboardcannyview'),
path('test', testview)
]