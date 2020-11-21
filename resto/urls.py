from django.conf.urls import url
from resto import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^reservation/$', views.NewReservation.as_view(), name="reservation"),
    url(r'^contact/$', views.Contact.as_view(), name="contact"),
    url(r'^payments/$', views.payment, name="payment"),
    url(r'^thanks/$', views.thanks, name="thanks"),
    url(r'^thankyou/$', views.thankyou, name="thankyou"),
    url(r'^sorry/$', views.sorry, name="sorry"),
    url(r'^soon/$', views.soon, name="soon"),
    url(r'^HomeDelivery/$', views.menu1, name="HomeDelivery"),
    url(r'^Menu/$', views.menu3, name="Menu"),
    url(r'^Takeaway/$', views.menu2, name="Takeaway"),
]
