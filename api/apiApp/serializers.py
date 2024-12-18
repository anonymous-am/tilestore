# serializers.py in your app

from rest_framework import serializers
from .models import Category, Product, Orders
from .validation import Validation

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'category_id','category_image']



class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'size', 'product_id', 'category', 'product_details', 'product_image']

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'order_id', 'product_id', 'merchant_name', 'merchant_mobile_no','seller_id', 'price', 'quantity', 'user_comment','order_date', 'mail_status', 'order_processed']

#     # apply custom validation ......................
#     # validate product id ..........
    def validate_product_id(self, value):
        if Validation.is_idValid(value):
            return value
        raise serializers.ValidationError('Invalid product id.')
    
    # validate merchant name.......
    def validate_merchant_name(self, value):
        if Validation.is_nameValid(value):
            return value
        raise serializers.ValidationError('Please enter a valid customer name (at least 3 characters only).')
    
    # validate merchant mobile number ..............
    def validate_merchant_mobile_no(self, value):
        if Validation.is_contactValid(value):
            return value
        raise serializers.ValidationError('Please enter a valid mobile number.')
    
    # validate seller id ..............
    def validate_seller_id(self, value):
        if Validation.is_idValid(value):
            return value
        raise serializers.ValidationError('Please enter a valid seller Id (at least 3 characters, letters, numbers, and underscores only).')
    
    # validate price ......
    # def validate_price(self, value):
    #     if Validation.is_priceValid(value):
    #         return value
    #     raise serializers.ValidationError('Please enter a valid price.')

    # # validate quantity ......
    # def validate_quantity(self, value):
    #     if Validation.is_quantityValid(value):
    #         return value
    #     raise serializers.ValidationError('Please enter a valid quantity value.')