from django.conf.urls import url

from project import views

urlpatterns = [
    url(r'^profile/$', views.Profile.as_view(), name="profile"),
    url(r'^add-reservation/$', views.AddReservation.as_view(), name="add"),
    url(r'^add-item/$', views.AddItem.as_view(), name="new"),
    url(r'^add-feedback/$', views.AddFeedback.as_view(), name="feedback"),
    url(r'^login/$', views.Login.as_view(), name="login"),
    url(r'^register/$', views.Register.as_view(), name="register"),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),    
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    url(r'^view-menuitems/$',
        views.view_menuitems, name="view_menuitems"),
    url(r'^view-reservations/$',
        views.view_reservations, name="view_reservations"),
    url(r'^update-reservation/(?P<pk>\d+)/$',
        views.UpdateReservation.as_view(), name="update_reservation"),
    url(r'^update-menuitem/(?P<pk>\d+)/$',
        views.UpdateMenuItem.as_view(), name="update_menuitem"),
    url(r'^order-delete/(?P<pk>\d+)$', views.order_delete, name='order_delete'),
    url(r'^del_reserve/(?P<pk>\d+)$', views.reservation_delete, name='reservation_delete'),
    url(r'^show-order/(?P<order_id>\d+)$', views.show, name='show'),
]
