from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.get_total()
    return render(request, 'cart_summary.html', {'cart_products': cart_products, 'quantities': quantities, 'total': total})

# def cart_add(request):
#     cart = Cart(request)

#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('product_id'))
#         product_qty = int(request.POST.get('product_qty'))
#         product = get_object_or_404(Product, id=product_id)
#         cart.add(product=product, quantity = product_qty)

#         cart_quantity = cart.__len__()

#         # response = JsonResponse({'Product name': product.name})
#         response = JsonResponse({'qty': cart_quantity})
#         return response

def cart_add(request):  
    cart = Cart(request)  

    if request.POST.get('action') == 'post':  
        product_id_str = request.POST.get('product_id')  
        product_qty_str = request.POST.get('product_qty')  
        
        # Validate product ID  
        if not product_id_str or not product_qty_str:  
            return JsonResponse({'error': 'Product ID and quantity are required.'}, status=400)  

        try:  
            product_id = int(product_id_str)  
            product_qty = int(product_qty_str)  
        except ValueError:  
            return JsonResponse({'error': 'Invalid product ID or quantity.'}, status=400)  

        product = get_object_or_404(Product, id=product_id)  
        cart.add(product=product, quantity=product_qty)  

        cart_quantity = cart.__len__()  

        messages.success(request, 'به سبد خرید اضافه شد')
        return JsonResponse({'qty': cart_quantity})
        # return response
        


def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)


        response = JsonResponse({'product': product_id})
        messages.error(request, 'محصول از سبد خرید حذف شد')
        return response


def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
       
        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty': product_qty})
        messages.success(request, 'سبد خرید ویرایش شد')
        return response
