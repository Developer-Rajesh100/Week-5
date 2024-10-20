from django.contrib import messages
from django.shortcuts import render
from car.models import Car, Brand
from car.models import Order
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .forms import CommentForm
from datetime import datetime
from car.models import Comment


########## Home Page Function Views ##########
def homepage(request, brand_slug = None):
    car_data = Car.objects.all()
    brands = Brand.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(brand_name = brand_slug)
        data = Car.objects.filter(brand_name = brand)
        return render(request, 'homepage.html', {'data': data, 'brands': brands})
    return render(request, 'homepage.html', {'data': car_data, 'brands': brands})


########## Car Details Class Views ##########
class CarDetailsView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


########## Buy Now Function Views ##########
def buyNow(request, id):
    car = Car.objects.get(id=id)
    if car.car_quantity > 0:
        car.car_quantity -= 1
        car.save()
        Order.objects.create(car_id=car.id, username=request.user.username, orderd_on = datetime.now())
        messages.success(request, 'Order Placed Successfully!')
    else:
        messages.warning(request, 'This car is currently out of stock.....!')
    return render(request, 'car_details.html', {'car': car})


######## Comment Class Views ##########
class CommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'car_details.html'
    success_url = reverse_lazy('car_details')