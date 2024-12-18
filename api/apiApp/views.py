from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import ProductSerializer, CategorySerializer, OrdersSerializer
from .models import Category,Product,Orders
from datetime import datetime,date
from . import utils
import json
from django.template.loader import render_to_string

@csrf_exempt
def addProduct(request):
    if request.method == 'POST':
        try:
            # Handling file upload
            product_image = request.FILES.get('product_image')
            data = request.POST.copy()
            data['product_image'] = product_image
            print("data ",data)

            serializer = ProductSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()

                res = {
                    'status': 'Successful',
                    'data': serializer.data,
                    'message': 'Product added successfully'
                }
                return JsonResponse(res)
            else:
                print("Validation error:", serializer.errors)
                return JsonResponse({'error': 'Validation error'}, status=400)

        except Exception as e:
            print("Exception:", str(e))
            return JsonResponse({'error': 'Internal Server Error'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

# API to fetch product ..........................................
@csrf_exempt
def getProduct(request):
    if request.method == 'GET':
        try:
            category_id = request.GET.get('category_id')
            size = request.GET.get('size')
            print("category_id value : ",category_id)
            print("size value : ",size)

            if category_id and size:
                # return the tiles detail with particular size and category............
                result = Product.objects.filter(category=category_id,size=size)
                serializer = ProductSerializer(result, many=True)
                resp = {
                            'status': 'Successful',
                            'data': serializer.data,
                            'message': 'Product details fetched successfully'
                        }
                return JsonResponse(resp)
            
            if category_id:
                # return the list of all sizes of give category.
                values =  Product.objects.filter(category=category_id)  #.values('size').distinct()
                serializer = ProductSerializer(values, many=True)
                print("Result only category id :",serializer.data)
                resp = {
                            'status': 'Successful',
                            'data': serializer.data,
                            'message': 'subcategory details fetched successfully'
                        }
                return JsonResponse(resp)
        except Exception as e:
            print("Exception:", str(e))
            return JsonResponse({'error': 'Internal Server Error'}, status=500)
        
# Api to fetch specific product with product id ..
@csrf_exempt
def getProductdetail(request):
    product_id = request.GET.get('product_id')
    print("produt_id value : ",product_id)
    try:
        # return the tiles detail with particular size and category............
        result = Product.objects.filter(product_id=product_id)
        serializer = ProductSerializer(result, many=True)
        resp = {
                    'status': 'Successful',
                    'data': serializer.data,
                    'message': 'Product details fetched successfully'
                }
        return JsonResponse(resp,status=200)
    except Exception as e:
            print("Exception:", str(e))
            return JsonResponse({'error': 'Internal Server Error'}, status=500) 
        





# API to add category ...................................................
@csrf_exempt
def addCategory(request):
    # print("View is called.")
    if request.method == 'POST':
        # print("Api hitted")
        try:
            category_image = request.FILES.get('category_image')
            data = request.POST.copy()
            data['category_image'] = category_image
            # data = json.loads(request.body)
            serializer = CategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                res = {
                        'status': 'Successful',
                        'data': data,
                        'message': 'Category added successfully'
                    }
                return JsonResponse(res)
            else: 
                print("Validation error:", serializer.errors)
                return JsonResponse({'error': 'Validation error'}, status=400)
            
        except Exception as e:
            print("Exception:", str(e))
            return JsonResponse({'error': 'Internal Server Error'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

# API to fetch category category ...................................................
@csrf_exempt
def getTilesCategory(request):
    if request.method == 'GET':
        try:
            categories = Category.objects.filter(product__isnull=False).distinct()
            # categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            resp = {
                        'status': 'Successful',
                        'data': serializer.data,
                        'message': 'Category details fetched successfully'
                    }
            print("tiles categories : ",serializer.data)
            return JsonResponse(resp)
        except Exception as e:
            print("Exception:", str(e))
            return JsonResponse({'error': 'Internal Server Error'}, status=500)





# API to place order ................................................................................
@csrf_exempt
def placeOrder(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            date = datetime.now().strftime('%Y-%m-%d')
            data['order_date']=date
            data['order_processed']='0'
            random_sequence = utils.generate_random_sequence(10)
            data['order_id']= random_sequence
            print("random sequence ",random_sequence)
            print("data posted : ---------------- ",data)
            serializer = OrdersSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                # send email for order information ...................
                to_email = 's0000011111am@gmail.com'
                subject=data['order_id']
                # Subject with dynamic order ID
                # subject = 'New Order Received - Order ID: {}'.format(data['order_id'])

                
                # body = f'Please click below link to verify your email address.{data}'
                # Render the HTML template with order data
                html_message = render_to_string('email_template.html',data)
                body = html_message
                is_mail_send = utils.send_email(to_email, subject, body)
                if is_mail_send:
                    Orders.objects.filter(order_id=data['order_id']).update(mail_status=True)
                    print("Order placed. mail status updated successfully")
                else:
                    print("Mail not sended.............")
                res = {
                        'success': True,
                        'data':    data['order_id'],
                        'message': 'Order placed successfully'
                    }
                return JsonResponse(res, status=200)
            else: 
                res = {
                    'success':False,
                    'error':serializer.errors
                }
                print("Validation error:", serializer.errors)
                return JsonResponse(res, status=400)
                # return JsonResponse({'error': serializer.errors}, status=400)
            
        except Exception as e:
            print("Exception:", str(e))
            res = {
                    'status':'500',
                    'error':'Internal Server Error'
            }
            return JsonResponse(res, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

    
