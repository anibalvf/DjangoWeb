from django.conf.urls import url
from django.urls import path, include
from hookah.views import hookah_list_view, hookah_details_view, HookahListView, HookahListViewSecond, HookahDetailsView, \
    edit_company, CompanyUpdatedView, CompanyDetailView, CompanyCreateView, CompanylistView, HookahCreateView

urlpatterns = [
    # con funcion
    # path('list',hookah_list_view, name='hookah_list_view'),
    # Con clases
    # url(r'^list-alt/$',HookahListView.as_view(), name='hookah_list_view_alt'),
    url(r'^list/$',HookahListViewSecond.as_view(), name='hookah_list_view'),
    # con funcion
    # url(r'^details/(?P<pk>\d+)$',hookah_details_view, name='hookah_details_view'),
    # con clases
    url(r'^details/(?P<pk>\d+)$',HookahDetailsView.as_view(), name='hookah_details_view'),
    url(r'^create/$',HookahCreateView.as_view(), name='hookah_create_view'),


    url(r'^company/list/',CompanylistView.as_view(), name='company_list_view'),
    url(r'^company/detail/(?P<pk>\d+)$',CompanyDetailView.as_view(), name='company_detail_view'),


    url(r'^company/edit/(?P<pk>\d+)$',CompanyUpdatedView.as_view(), name='company_edit_view'),
    url(r'^company/create/$',CompanyCreateView.as_view(), name='company_create_view'),
]
