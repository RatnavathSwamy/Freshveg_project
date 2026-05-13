from django.shortcuts import render

from .models import Product

from .models import Contact

from .models import Product, Contact, Order
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


from django.contrib.auth.models import User

from django.contrib.auth import authenticate

from django.contrib.auth import login

from django.contrib.auth import logout
from django.db.models import Q

from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')





@login_required(login_url='login')
def products(request):

    

    return render(
        request,
        'home/products.html'
    )


def testimonials(request):
    return render(request, 'home/testimonials.html')

def contact(request):
    

    if request.method == "POST":

        name = request.POST.get('name')

        email = request.POST.get('email')

        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

    return render(request, 'home/contact.html')
  

from .models import Product, Contact, Order
from django.shortcuts import render, redirect, get_object_or_404


@login_required(login_url='login')
def buy_product(request, product_name):

    products = {

        'tomato': {
            'name': 'Tomato',
            'price': 40,
            'image': 'https://images.unsplash.com/photo-1546094096-0df4bcaaa337?q=80&w=1200&auto=format&fit=crop',
            'description': 'Fresh organic tomatoes rich in vitamins and antioxidants.'
        },

        'potato': {
            'name': 'Potato',
            'price': 30,
            'image': 'https://images.unsplash.com/photo-1518977676601-b53f82aba655?q=80&w=1200&auto=format&fit=crop',
            'description': 'Farm fresh potatoes perfect for curries and snacks.'
        },

        'onion': {
            'name': 'Onion',
            'price': 45,
            'image': 'https://images.unsplash.com/photo-1508747703725-719777637510?q=80&w=1200&auto=format&fit=crop',
            'description': 'Premium quality onions directly from local farms.'
        },

        'spinach': {
            'name': 'Spinach',
            'price': 25,
            'image': 'https://images.unsplash.com/photo-1576045057995-568f588f82fb?q=80&w=1200&auto=format&fit=crop',
            'description': 'Nutritious spinach full of iron and minerals.'
        },

        'carrot': {
            'name': 'Carrot',
            'price': 50,
            'image': 'https://images.unsplash.com/photo-1567306226416-28f0efdc88ce?q=80&w=1200&auto=format&fit=crop',
            'description': 'Sweet and crunchy carrots for salads and juices.'
        },

        'broccoli': {
            'name': 'Broccoli',
            'price': 90,
            'image': 'https://images.unsplash.com/photo-1563565375-f3fdfdbefa83?q=80&w=1200&auto=format&fit=crop',
            'description': 'Healthy broccoli rich in fiber and vitamins.'
        },

        'cucumber': {
            'name': 'Cucumber',
            'price': 35,
            'image': 'https://images.unsplash.com/photo-1582515073490-dc0c8f76f5d2?q=80&w=1200&auto=format&fit=crop',
            'description': 'Fresh cucumbers with hydration benefits.'
        },

        'capsicum': {
            'name': 'Capsicum',
            'price': 70,
            'image': 'https://images.unsplash.com/photo-1576186726115-4d51596775d1?q=80&w=1200&auto=format&fit=crop',
            'description': 'Colorful capsicum rich in vitamin C.'
        }
    }

    product = products.get(product_name)

    if not product:

        return redirect('products')

    if request.method == "POST":

        customer_name = request.POST.get(
            'customer_name'
        )
        buyer_state = request.POST.get(
        'buyer_state'
    )

        buyer_district = request.POST.get(
        'buyer_district'
    )

        buyer_mandal = request.POST.get(
        'buyer_mandal'
    )

        buyer_village = request.POST.get(
        'buyer_village'
    )


        phone = request.POST.get('phone')

        address = request.POST.get('address')

        quantity = float(
            request.POST.get('quantity')
        )

        payment_method = request.POST.get(
            'payment_method'
        )

        total_price = quantity * product['price']

        Order.objects.create(
            buyer_state=buyer_state,
            buyer_district=buyer_district,
            buyer_mandal=buyer_mandal,
            buyer_village=buyer_village,

            user=request.user,

            customer_name=customer_name,

            phone=phone,

            address=address,

            product_name=product['name'],

            quantity=quantity,

            price_per_kg=product['price'],

            total_price=total_price,

            payment_method=payment_method
        )

        return redirect('success')

    return render(
        request,
        'home/buy.html',
        {'product': product}
    )

    
def order_success(request):

    return render(request, 'home/order_success.html')


# REGISTER
@login_required(login_url='login')
def success(request):

    return render(
        request,
        'home/success.html'
    )

def register(request):

    if request.method == "POST":

        username = request.POST.get('username')

        email = request.POST.get('email')

        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():

            return render(
                request,
                'home/register.html',
                {'error': 'Username already exists'}
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'home/register.html')


# LOGIN

def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('products')

        else:

            return render(
                request,
                'home/login.html',
                {'error': 'Invalid Username or Password'}
            )

    return render(request, 'home/login.html')


# LOGOUT

def user_logout(request):

    logout(request)

    return redirect('login')
# Create your views here.



@login_required(login_url='login')
def my_orders(request):

    orders = None

    error = None

    if request.method == "POST":

        username = request.POST.get('username')

        phone = request.POST.get('phone')

        try:

            orders = Order.objects.filter(

                

                user__username=username,

                #phone=phone
                
                ##############
                user=request.user,
                is_received=False

                #################

            ).order_by('-ordered_at')

            if not orders.exists():

                error = "Invalid Username or Phone Number"

        except:

            error = "Something went wrong"

    return render(

        request,

        'home/my_orders.html',

        {

            'orders': orders,

            'error': error

        }
    )

from .models import Seller


@login_required(login_url='login')
def seller_register(request):

    if request.method == 'POST':

        seller_name = request.POST.get(
            'seller_name'
        )

        age = request.POST.get('age')

        photo = request.FILES.get('photo')

        aadhaar_number = request.POST.get(
            'aadhaar_number'
        )

        phone_number = request.POST.get(
            'phone_number'
        )

        state = request.POST.get('state')

        district = request.POST.get(
            'district'
        )
        mandal = request.POST.get('mandal')

        village = request.POST.get('village')

        market_name = request.POST.get(
            'market_name'
        )

        vegetables_selling = request.POST.get(
            'vegetables_selling'
        )

        experience = request.POST.get(
            'experience'
        )

        Seller.objects.create(

            user=request.user,

            seller_name=seller_name,

            age=age,

            photo=photo,

            aadhaar_number=aadhaar_number,

            phone_number=phone_number,

            state=state,

            district=district,

            mandal=mandal,

            village=village,
            market_name=market_name,

            vegetables_selling=vegetables_selling,

            experience=experience
        )

        return redirect('seller_profile')

    return render(
        request,
        'home/seller_register.html'
    )
@login_required(login_url='login')
def seller_profile(request):

    seller = Seller.objects.get(
        user=request.user
    )

    return render(
        request,
        'home/seller_profile.html',
        {'seller': seller}
    )


def seller_login(request):

    error = None

    if request.method == 'POST':

        seller_name = request.POST.get(
            'seller_name'
        )

        phone_number = request.POST.get(
            'phone_number'
        )

        try:

            seller = Seller.objects.get(
                seller_name=seller_name,
                phone_number=phone_number
            )

            request.session['seller_id'] = (
                seller.id
            )

            return redirect(
                'seller_dashboard'
            )

        except Seller.DoesNotExist:

            error = (
                'Invalid Seller Name or '
                'Phone Number'
            )

    return render(
        request,
        'home/seller_login.html',
        {'error': error}
    )

def seller_dashboard(request):

    seller_id = request.session.get(
        'seller_id'
    )

    if not seller_id:

        return redirect(
            'seller_login'
        )

    seller = Seller.objects.get(
        id=seller_id
    )

    # FILTER ORDERS BY SELLER AREA

    orders = Order.objects.filter(

        

        buyer_state=seller.state,

        buyer_district=seller.district,

        buyer_mandal=seller.mandal,

        buyer_village=seller.village,

        status='Pending',
        ############
        #status='Accepted',
        is_received=False
        #############

    ).order_by('-ordered_at')

    total_orders = orders.count()

    total_revenue = sum(

        order.total_price

        for order in orders

    )

    return render(

        request,

        'home/seller_dashboard.html',

        {

            'seller': seller,

            'orders': orders,

            'total_orders': total_orders,

            'total_revenue': total_revenue

        }

    )

def accept_order(request, order_id):


    ##############3
    order = Order.objects.get(id=order_id)

    seller_profile = Seller.objects.get(
        user=request.user
    )
###################33333


    seller_id = request.session.get(
        'seller_id'
    )

    if not seller_id:

        return redirect('seller_login')

    seller = Seller.objects.get(
        id=seller_id
    )

    order = Order.objects.get(
        id=order_id
    )

    if order.status == 'Pending':

        order.status = 'Accepted'

        order.accepted_by = (
            seller.seller_name
        )

        order.seller_id = (
            seller.seller_id
        )

        order.seller_name = (
            seller.seller_name
        )

        order.seller_phone = (
            seller.phone_number
        )

        order.save()

    messages.success(
        request,
        'Order Accepted Successfully'
    )

    return redirect(
        'seller_dashboard'
    )


#####################3333
    order.status = 'Accepted'

    order.seller_name = request.user.seller

    order.seller_phone = seller_profile.phone_number

    #order.seller_address = seller_profile.address

    order.seller_latitude = seller_profile.latitude

    order.seller_longitude = seller_profile.longitude

    order.save()

    messages.success(
        request,
        'Order Accepted Successfully'
    )

    return redirect('seller_dashboard')


    #######

    #order = Order.objects.get(id=order_id)

    #order.status = 'Accepted'

    # SELLER DETAILS

    #order.seller_name = request.user.username

    #order.seller_phone = "9876543210"

    #order.seller_address = "Hyderabad"

    #order.seller_latitude = "17.3850"

    #order.seller_longitude = "78.4867"

   # order.save()

   # messages.success(
       # request,
        #'Order Accepted Successfully'
   # )

   # return redirect('seller_dashboard')


    #############

    seller_id = request.session.get(
        'seller_id'
    )

    seller = Seller.objects.get(
        id=seller_id
    )

    order = Order.objects.get(
        id=order_id
    )

    if order.status == 'Pending':

        order.status = 'Accepted'

        order.accepted_by = (
            seller.seller_name
        )

        order.seller_id = (
            seller.seller_id
        )

        order.seller_name = (
            seller.seller_name
        )

        order.save()

    return redirect(
        'seller_dashboard'
    )


def reject_order(request, order_id):

    seller_id = request.session.get(
        'seller_id'
    )

    if not seller_id:

        return redirect('seller_login')

    order = Order.objects.get(
        id=order_id
    )

    order.status = 'Rejected'

    order.save()

    return redirect(
        'seller_dashboard'
    )




from django.db.models import Q


def accepted_orders(request):



    #################
    

    error = None

    orders = None

    seller = None

    if request.method == 'POST':

        seller_name = request.POST.get(
            'seller_name'
        )

        phone_number = request.POST.get(
            'phone_number'
        )

        try:

            seller = Seller.objects.get(

                seller_name=seller_name,

                phone_number=phone_number

            )

            orders = Order.objects.filter(

                seller_id=seller.seller_id,

                status='Accepted',

                is_received=False

            ).order_by('-ordered_at')

            if not orders.exists():

                error = "No Accepted Orders Found"

        except Seller.DoesNotExist:

            error = (
                'Invalid Seller Name or Phone Number'
            )

    return render(

        request,

        'home/accepted_orders.html',

        {

            'orders': orders,

            'error': error,

            'seller': seller

        }

    )
    ################

    error = None

    orders = None

    seller = None

    if request.method == 'POST':

        seller_name = request.POST.get(
            'seller_name'
        )

        phone_number = request.POST.get(
            'phone_number'
        )

        try:

            seller = Seller.objects.get(

                seller_name=seller_name,

                phone_number=phone_number

            )

            orders = Order.objects.filter(

                seller_id=seller.seller_id,

                status='Accepted'

            ).order_by('-ordered_at')

        except Seller.DoesNotExist:

            error = (
                'Invalid Seller Credentials'
            )

    return render(

        request,

        'home/accepted_orders.html',

        {

            'orders': orders,

            'error': error,

            'seller': seller

        }

    )

########################
from django.shortcuts import get_object_or_404

def track_order(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(
        request,
        'home/track_order.html',
        {'order': order}
    )




def received_order(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )


###############
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    order.status = 'Delivered'

    order.is_received = True

    order.save()

    return render(
        request,
        'home/order_received.html',
        {'order': order}
    )


############
    order.status = 'Delivered'

    order.is_received = True

    order.save()

    messages.success(
        request,
        'Order Successfully Received'
    )

    return redirect('my_orders')

#########################

####################333
from django.http import JsonResponse

def update_live_location(request):

    if request.method == 'POST':

        seller_profile = Seller.objects.get(   ######insteadof seller profile we will keep seller
            user=request.user
        )

        latitude = request.POST.get('latitude')

        longitude = request.POST.get('longitude')

        seller_profile.latitude = latitude

        seller_profile.longitude = longitude

        seller_profile.save()

        return JsonResponse({
            'status': 'success'
        })
    
    #################3

from .models import ContactMessage
from django.contrib import messages

def contact_page(request):

    if request.method == "POST":

        name = request.POST.get("name")

        phone = request.POST.get("phone")

        email = request.POST.get("email")

        #issue = request.POST.get("issue")
        message = request.POST.get("issue")

        ContactMessage.objects.create(
            name=name,
            phone=phone,
            email=email,
           # issue=issue
           message=message
        )

        messages.success(
    request,
    f"Hello {name} 👋 Your issue has been sent successfully. Our FreshVeg support team will contact you shortly!"
)

    return render(request, "contact.html")