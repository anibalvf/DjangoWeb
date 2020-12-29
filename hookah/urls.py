from django.conf.urls import url
from django.urls import path, include
from hookah.views import hookah_list_view, hookah_details_view, HookahListView, HookahListViewSecond, HookahDetailsView, \
    edit_company, CompanyUpdatedView, CompanyDetailView, CompanyCreateView

urlpatterns = [
    path('list',hookah_list_view, name='hookah_list_view'),
    url(r'^list-alt/$',HookahListView.as_view(), name='hookah_list_view_alt'),
    url(r'^list-alt-second/$',HookahListViewSecond.as_view(), name='hookah_list_view_alt_second'),

    url(r'^details/(?P<pk>\d+)$',hookah_details_view, name='hookah_details_view'),
    url(r'^details-alt/(?P<pk>\d+)$',HookahDetailsView.as_view(), name='hookah_details_view_alt'),


    url(r'^company/edit/(?P<pk>\d+)$',CompanyUpdatedView.as_view(), name='company_edit_view'),

    url(r'^company/detail/(?P<pk>\d+)$',CompanyDetailView.as_view(), name='company-detail-view'),
    url(r'^company/create/$',CompanyCreateView.as_view(), name='company-create-view'),
]