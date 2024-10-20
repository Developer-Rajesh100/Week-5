from django.db import models


########## Brand Model ##########
class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand_name}"


########## Car Model ##########
class Car(models.Model):
    car_img = models.ImageField(upload_to='upload/')
    car_name = models.CharField(max_length=50)
    car_description = models.TextField()
    car_quantity = models.IntegerField()
    car_price = models.IntegerField()
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.car_name} | Quantity: {self.car_quantity} | Price: {self.car_price} | Brand: {self.brand_name}"


########## Order Model ##########
class Order(models.Model):
    car_id = models.IntegerField()
    username = models.CharField(max_length=50)
    orderd_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} | {self.car_id} | {self.orderd_on}"


########## Comment Model ##########
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.comment[0:30]}....."