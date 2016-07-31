from django.conf.urls import url

from dashboard import views
from dashboard.forms import ProgressSearchForm
from dashboard.views import ProgressSearchView

urls = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^profile$', views.profile, name='my_profile'),
    url(r'^profile/(?P<user_id>\d+)$', views.profile, name='profile'),
    url(r'^year\/(?P<year>\d+)\/week\/(?P<week_label>\d+)\/summary$', views.week_summary, name='week_summary'),
    url(r'^chartsjs/week_chart.js$', views.time_comparison_bar_chart_data, name='week_chart_js'),
    url(r'^chartsjs/projects_chart.js$', views.projects_bar_chart_data, name='projects_chart_js'),
    url(r'^search/$', ProgressSearchView(form_class=ProgressSearchForm), name='search_progresses'),
]