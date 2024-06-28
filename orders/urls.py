from django.urls import path
from views import place_order

app_name=[
    path('billing/', place_order, name='place_order'),
    path('payment/',payments,name='paymwnts')
    path('order/',views.place_order),
    path('payment_page/',views.makepayment),
    path('sendmail/<uemail>/',views.sendusermail)
]