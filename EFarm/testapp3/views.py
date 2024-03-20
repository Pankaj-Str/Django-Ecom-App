from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
#from .models import Product
# from .models import Product, ContactMessage
# # from .models import Product, CartItem
from django.core.exceptions import ValidationError
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import Category as CategoryModel  # Assuming CategoryModel is your Django model for categories
from django.contrib.auth.hashers import check_password
from django.views import View
from . models import Product
from . models import Category
# from . models import SignupPage
# from . models import Cart
from . models import Customer
from django.db import IntegrityError
from datetime import datetime







def index(request):
    products = Product.get_all_products();
    print(products)
    return render(request, 'testapp/index.html')

class Category(View):
    @staticmethod
    def get_all_categories():
        # Retrieve all categories from the database using Django models
        return CategoryModel.objects.all()

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart', {})
        quantity = cart.get(product)
        cart[product] = quantity + 1 if quantity else 1
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('index')

    def get(self, request):
       categories = Category.get_all_categories()
       category_id = request.GET.get('category')
       products = Product.get_products_by_category_id(category_id) if category_id else Product.get_all_products()

       # Clear the 'cart' session key
       request.session.pop('cart', None)

       # Pass 'cart' to the template context
       data = {'products': products, 'categories': categories, 'cart': request.session.get('cart', {})}
       print('you are : ', request.session.get('username'))
       return render(request, 'testapp/category.html', data)





# def category(request):
#     products = None
#     categories = Category.get_all_categories()
#     categoryid = request.GET.get('category')
#     if categoryid:
#         products = Product.get_products_by_categoryid(categoryid)
#     else:
#         products = Product.get_all_products()

#     data = {}
#     data['products'] = products
#     data['categories'] = categories
#     print('you are : ',request.session.get('username'))
#     return render(request,'testapp/category.html',data)





def signup(request):
    if request.method == 'GET':
        return render(request, 'testapp/signup.html') 
    elif request.method == 'POST':
        postData = request.POST
        first_name = postData.get('fname')
        middle_name = postData.get('mname')
        last_name = postData.get('lname')
        age = postData.get('age')
        mob_no = postData.get('mob_no')
        dob = postData.get('dob')
        username = postData.get('username')
        email = postData.get('email')
        password1 = postData.get('password1')

        # Form validation
        value = {'first_name' : first_name,'middle_name' :middle_name,'last_name':last_name,'age':age,'mobile_no':mob_no,'dob':dob,'username':username,'email':email}
        error_message = None
        if not first_name:
            error_message = 'First Name Required!!'
        elif len(first_name) < 4:
            error_message = 'First Name must be 4 characters'
        elif not middle_name:
            error_message = 'Middle Name Required'
        elif len(middle_name) < 4:
            error_message = 'Middle Name must be 4 characters'
        elif not last_name:
            error_message = 'Last Name Required'
        elif len(last_name) < 4:
            error_message = 'Last Name must be 10 characters'
        elif not mob_no :
            error_message = 'Mobile no. Required'
        elif len(mob_no) < 10:
            error_message = 'Mobile no. must be 10 numbers'
        elif not username :
            error_message = 'Username Required'
        elif len(username) <= 10:
            error_message = 'Username must be 10 characters'
        elif len(email) < 5:
            error_message = "email must be 5 character "
        elif len(password1) < 8:
            error_message = "password must be 8 character"
        elif Customer.objects.filter(email=email).exists():  # Check if customer with email already exists
            error_message = 'Email already exists'
        

        if not dob:
            error_message = 'Date of birth is required.'
        else:
            try:
                # Validate the format of the date
                datetime.strptime(dob, '%Y-%m-%d')
            except ValueError:
                error_message = 'Date of birth must be in YYYY-MM-DD format.'

        if age and not age.isdigit():
            error_message = 'Age must be a valid number.'

        if error_message:
            return render(request, 'testapp/signup.html', {'error_message': error_message})

        try:
            # Data processing - create Customer instance and save
            customer = Customer(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                age=int(age),
                mobile_no=mob_no,
                dob=dob,
                username=username,
                email=email,
                password=password1
            )
            customer.password = make_password(customer.password)
            customer.register()
            data = {
                'values' : value
            }
        except ValidationError as e:
            return render(request, 'testapp/signup.html', {'error_message': e.message},data)
        except IntegrityError:
            return render(request, 'testapp/signup.html', {'error_message': 'Failed to save customer. Please try again.'},data)
        
        # If everything goes well, redirect to success page
        return redirect('index')  # Corrected redirect usage




class Login(View):
    def get(self, request):
        return render(request, 'testapp/login.html')

    def post(self, request):
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        customer = Customer.objects.filter(username=username).first()

        error_message = None
        if customer:
            flag = check_password(pass1,customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['username'] = customer.username

                return redirect('index')
            else:
                error_message = 'Username or password invalid'
        else:
            error_message = 'Username or password invalid'
        print(username,pass1)
        return render(request,'testapp/login.html',{'error':error_message})
        
# def login(request):
#     if request.method == 'GET':
#         return render(request,'testapp/login.html')
#     else:
#         uname = request.POST.get('username')
#         pass1 = request.POST.get('password1')
#         customer = Customer.get_customer_by_username(uname)
#         error_message = None
#         if customer:
#             flag = check_username(uname)
#             if flag:
#                 return redirect('index')
#             else:
#                 error_message = 'Username or Password Invalid!!'

#         else:
#             error_message = 'Username or Password Invalid!!'

#         print(username,password)
#         return render(request,'testapp/login.html',{'error':error_message})


















# from django.core.exceptions import ObjectDoesNotExist

# def login(request):
#     error_message = None  # Initialize error_message variable
    
#     if request.method == 'GET':
#         return render(request, 'testapp/login.html', {'error_message': error_message})
#     elif request.method == 'POST':
#         username = request.POST.get('uname')
#         password = request.POST.get('pass1')
        
#         try:
#             customer = Customer.get_customer_by_username(username)
        
#         except ObjectDoesNotExist:
#             error_message = 'Invalid username or password.'  # Set error message
#             return render(request, 'testapp/login.html', {'error_message': error_message})

#         print(customer)
#         print(username, password)
        
#         # Assuming you want to render index.html after successful login
#         return redirect('index')





def contact(request):
    return render(request,'testapp/contact.html')

def payment(request):
    return render(request,'testapp/payment.html')



def LogoutPage(request):
    logout(request)
    return redirect('login')