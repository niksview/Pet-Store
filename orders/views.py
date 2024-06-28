from django.shortcuts import render,HttpResponse,redirect
from cart.models import cart 
from datetime import date
from .forms import OrdersForm
from .models import Orders
import random
import razorpay
from django.core.mail import send_mail

# Create your views here.
def place_order(request):
    #pass
    form=OrdersForm()
    current_user=request.user
    cart_item=cart.objects.filter(user=current_user)
    cart_item_count=cart_item.count()
    total_amount=request.GET.get('totalamount')
    print(totalamount)
    if cart_item_count<=0:
        render redirect('pets:petlist')
    if request.method=='POST':
        form=OrdersForm(request.POST)
        if form.is_valid():
            data.user=request.user
            data.first_name=form.cleaned_data.get('first_name')
            data.last_name=form.cleaned_data.get('last_name')
            data.phone=form.cleaned_data.get('phone')
            data.email=form.cleaned_data.get('email')
            data.address=form.cleaned_data.get('address')
            data.country=form.cleaned_data.get('country')
            data.state=form.cleaned_data.get('state')
            data.city=form.cleaned_data.get('city')
            data.total=total_amount
            data.ip=request.META.get('REMOTE_ADDR')
            todaydate=date.today()
            data.save()
            today=str(todaydate).replace('-','')
            orderNumber=today+ str(data.id)
            data.order_number=orderNumber

            data.save()
            order_object=orders.objects.get(user=request.user,order_number=orderNumber)

            context={'orders':Orders.order_object,'cart_item':cart_item,'total':total_amount}
            return render(request.'orders/payment_page',context)

            
        return render(request,'orders/billing_page.html',{'form':form,'total':total_amount})


def makepayment(request):
    orders=Order.objects.filter(uid=request.user.id)
    s=0
    for x in orders:
        s= s + x.pid.price * x.qty
        oid=x.order_id
    client = razorpay.Client(auth=("rzp_test_10OBDkwWTbBzdQ", "NxP46jxjJOPC09CmcNggVsga"))
    data = { "amount": s*100, "currency": "INR", "receipt": oid }
    payment = client.order.create(data=data)
    print(payment)
    context={}
    context['data']=payment
    uemail=request.user.email
    print(uemail)
    context['uemail']=uemail
    return render(request,'payment_page.html',context)

def sendusermail(request,uemail):
    msg="Order details of petstore are as follows:"
    send_mail(
        "Pet-Order is placed successfully",
        msg,
        "nikhilsurtekar88@gmail.com",  
        [uemail],  
        fail_silently=False,
        )
    return HttpResponse("Mail has sent successfully to the customer")
    
    