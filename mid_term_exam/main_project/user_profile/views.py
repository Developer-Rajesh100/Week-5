from django.shortcuts import render, redirect
from car.models import Order, Car


def userProfile(request):
    if request.user.is_authenticated:
        user_orders = Order.objects.filter(username=request.user.username)
        if user_orders.exists():
            car = Car.objects.all()
            orders = [car for car in car if car.id in user_orders.values_list('car_id', flat=True)]
            return render(request, 'profile.html', {'data': orders})
        else:
            return render(request, 'profile.html')
    else:
        return redirect('login')