from .cart import Cart #import Cart Class from cart.py

#Create Context Processor so cart will work on all pages
def cart(request):
    #return default data from our cart
    return {'cart': Cart(request)}