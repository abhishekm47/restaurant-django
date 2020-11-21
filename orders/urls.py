from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^pay/(?P<product_id>\d+)/$', views.charge, name='charge'),
    url(r'^email/(?P<product_id>\d+)/$', views.email_one, name='email_one'),
    url(r'^emailfive/(?P<product_id>\d+)/$', views.email_five, name='email_five'),
     url(r'^feedback/(?P<pk>\d+)/$', views.email_two, name='email_two'),
     url(r'^status/(?P<pk>\d+)/$', views.email_status, name='email_status'),
      url(r'^reservation_status/(?P<pk>\d+)/$', views.reservation_status, name='reservation_status'),
    url(r'^payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    url(r'^update-order/(?P<pk>\d+)/$',
        views.UpdateOrder.as_view(), name="update_Order"),
    url(r'^ideal/(?P<product_id>\d+)/(?P<amountcost>\d+)/$', views.ideal, name='ideal'),
    url(r'^authback/(?P<product_id>\d+)/(?P<amountcost>\d+)/$', views.authback, name='authback'),
   
]

