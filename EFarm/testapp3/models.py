from django.db import models


# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    @staticmethod
    def get_all_categories_by_categoryid(category_id):
        if category_id:
            return Category.objects.filter(category = category_id)
        else:
            return Product.get_all_products();





class Product(models.Model):
    #pro_id = models.AutoField
    pro_name=models.CharField(max_length=25)
    selling_price = models.IntegerField()
    discounted_price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    desc = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='uploads/to')

    # class Meta:
    #     app_label = 'testapp'  # Add this line with your app name

    def __str__(self):
        return self.pro_name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    
    @classmethod
    def get_products_by_categoryid(cls, category_id):
        # Implement logic to retrieve products by category ID
        return cls.objects.filter(category_id=category_id)



class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    mobile_no = models.CharField(max_length=15)
    dob = models.DateField(max_length=8)
    username = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_username(username):
        try:
            return Customer.objects.get(username = username)
        except:
            return False
            

            

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False



 