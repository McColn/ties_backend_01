from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Mine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
    	return self.name

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, null=True,blank=True, default="null")
    role = models.CharField(max_length=50, null=True,blank=True, default="user")
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    is_premium = models.BooleanField(default=False)

class PremiumModel(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.is_premium}"

class Investments(models.Model):
    projectName = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    resources = models.CharField(max_length=200)
    resourcesSummary = models.CharField(max_length=200)
    areaCovered = models.CharField(max_length=200)
    licenceType = models.CharField(max_length=200)
    licenceNumber = models.CharField(max_length=200)
    physicalLocation = models.CharField(max_length=200)
    mapLocation = models.CharField(max_length=200)
    levelInvestment= models.CharField(max_length=200) #type of Ownership / management
    image = models.ImageField(upload_to='images/', null=True,blank=True)

    projectStatus = models.CharField(max_length=200, null=True,blank=True) #CURRENT DVL STAGE
    studiesDone = models.CharField(max_length=200, null=True,blank=True)
    modeOfInvestment = models.CharField(max_length=200, null=True,blank=True)
    contact = models.CharField(max_length=200, default="info@ties.co.tz") #button contact
    attachments = models.FileField(upload_to='pdfs/', null=True, blank=True) #studies done

    def __str__(self):
        return self.projectName


class FrontPageInfo(models.Model):
    image = models.ImageField(upload_to='images/')
    body = models.CharField(max_length=200)


class InvestmentCompliance(models.Model):
    title = models.CharField(max_length=100)
    paragraph1 = models.TextField(db_index=True, default='null', blank=True)
    paragraph2 = models.TextField(db_index=True, default='null', blank=True)
    paragraph3 = models.TextField(db_index=True, default='null', blank=True)
    paragraph4 = models.TextField(db_index=True, default='null', blank=True)
    paragraph5 = models.TextField(db_index=True, default='null', blank=True)
    paragraph6 = models.TextField(db_index=True, default='null', blank=True)
    paragraph7 = models.TextField(db_index=True, default='null', blank=True)
    paragraph8 = models.TextField(db_index=True, default='null', blank=True)
    paragraph9 = models.TextField(db_index=True, default='null', blank=True)
    paragraph10 = models.TextField(db_index=True, default='null', blank=True)
    paragraph11 = models.TextField(db_index=True, default='null', blank=True)
    paragraph12 = models.TextField(db_index=True, default='null', blank=True)
    paragraph13 = models.TextField(db_index=True, default='null', blank=True)
    paragraph14 = models.TextField(db_index=True, default='null', blank=True)
    paragraph15 = models.TextField(db_index=True, default='null', blank=True)
    paragraph16 = models.TextField(db_index=True, default='null', blank=True)
    paragraph17 = models.TextField(db_index=True, default='null', blank=True)
    paragraph18 = models.TextField(db_index=True, default='null', blank=True)
    paragraph19 = models.TextField(db_index=True, default='null', blank=True)
    paragraph20 = models.TextField(db_index=True, default='null', blank=True)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)

class ConsultationCompliance(models.Model):
    title = models.CharField(max_length=100)
    paragraph1 = models.TextField(db_index=True, default='null')
    paragraph2 = models.TextField(db_index=True, default='null')
    paragraph3 = models.TextField(db_index=True, default='null')
    paragraph4 = models.TextField(db_index=True, default='null')
    paragraph5 = models.TextField(db_index=True, default='null')
    paragraph6 = models.TextField(db_index=True, default='null')
    paragraph7 = models.TextField(db_index=True, default='null')
    paragraph8 = models.TextField(db_index=True, default='null')
    paragraph9 = models.TextField(db_index=True, default='null')
    paragraph10 = models.TextField(db_index=True, default='null')
    paragraph11 = models.TextField(db_index=True, default='null')
    paragraph12 = models.TextField(db_index=True, default='null')
    paragraph13 = models.TextField(db_index=True, default='null')
    paragraph14 = models.TextField(db_index=True, default='null')
    paragraph15 = models.TextField(db_index=True, default='null')
    paragraph16 = models.TextField(db_index=True, default='null')
    paragraph17 = models.TextField(db_index=True, default='null')
    paragraph18 = models.TextField(db_index=True, default='null')
    paragraph19 = models.TextField(db_index=True, default='null')
    paragraph20 = models.TextField(db_index=True, default='null')
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)



# ecommerce.py

class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(unique=True)
    description = models.TextField()
    is_latest=models.BooleanField(default=False)

    def __str__(self):
        return self.name

    #HII NI KWA AJILI YA KUPATA PRODUCT ZILIZOPO KWENYE CATEGORY HUSIKA
    def get_absolute_url(self):
        return reverse('product_by_category', args=[self.slug])

from django.utils.text import slugify

class Item(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField()
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    is_latest=models.BooleanField(default=False)

    location = models.CharField(max_length=200,db_index=True, default='null')
    quality = models.CharField(max_length=200,db_index=True, default='null')
    sellOrRent = models.CharField(max_length=200,db_index=True, default='null')
    quantity = models.CharField(max_length=200,db_index=True, default='null')

    manufacturer = models.CharField(max_length=200,db_index=True, default='null')
    technicalDetails = models.CharField(max_length=1000,db_index=True, default='null')
    dimension = models.CharField(max_length=200,db_index=True, default='null')
    weight = models.CharField(max_length=200,db_index=True, default='null')
    capacity = models.CharField(max_length=200,db_index=True, default='null')
    horsepower = models.CharField(max_length=200,db_index=True, default='null')


    grade = models.CharField(max_length=200,db_index=True, default='null')
    groundedArea = models.CharField(max_length=200,db_index=True, default='null')
    physicalProperties = models.CharField(max_length=200,db_index=True, default='null')
    qualityAssurance = models.FileField(upload_to='pdfs/', null=True, blank=True)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    #HII NI KWA AJILI YA KUADI ITEM TO A CART
    def get_add_to_cart_url(self):
        return reverse('add_to_cart', kwargs={'id': self.id})

    #HII NI KWA AJILI YA KUREMOVE ITEM FROMA CART
    def get_remove_from_cart_url(self):
        return reverse('remove_from_cart', kwargs={'id': self.id})
    #HII NI KWA AJILI YA KUREMOVE ITEM MOJAMOJA FROM A CART ENDAPO UTACLICK MINUS SIGN
    def get_remove_single_from_cart_url(self):
        return reverse('remove_single_from_cart', kwargs={'id': self.id})


class OrderItem(models.Model):
    user = models.CharField(max_length=100,null=True, blank=True)
    # item = models.CharField(max_length=100,null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_item_discount_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_final_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_item_discount_price()
        return self.get_total_item_price()


class Order(models.Model):
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.CharField(max_length=100,null=True, blank=True)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
    	return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()

        return total


# mining trends
class MiningTrends(models.Model):
    mine_name = models.ForeignKey(Mine, on_delete=models.CASCADE)
    local_cost = models.FloatField()
    international_cost = models.FloatField()
    period = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.mine_name} - {self.period}"

# chatting
class Message(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.text}"





class Post(models.Model):
    content = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=100,null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ConsultancyTiesCategory(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
    	return self.title

class ConsultancyTiesDetails(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    category = models.ForeignKey(ConsultancyTiesCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)

    def __str__(self):
    	return self.title



# Chat App Model

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name == None:
            self.full_name = self.user.username
        super(Profile, self).save(*args, **kwargs)


class ChatMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="user")
    # user = models.CharField(max_length=100,null=True, blank=True)
    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="sender")
    # sender = models.CharField(max_length=100,null=True, blank=True)
    reciever = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    message = models.CharField(max_length=10000000000)

    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
        verbose_name_plural = "Message"

    def __str__(self):
        return f"{self.sender} - {self.reciever}"

    @property
    def sender_profile(self):
        sender_profile = Profile.objects.get(user=self.sender)
        return sender_profile
    @property
    def reciever_profile(self):
        reciever_profile = Profile.objects.get(user=self.reciever)
        return reciever_profile