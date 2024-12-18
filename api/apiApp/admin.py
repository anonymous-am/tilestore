from django.contrib import admin
from .models import Category, Product, Orders

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category_id','category_image']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'size', 'product_id', 'category', 'product_details', 'product_image']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            kwargs['queryset'] = Category.objects.only('category_id')  # Use only the 'category_id' field
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['id', 'product_name', 'size', 'product_id', 'category', 'product_details', 'product_image']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'product_id', 'merchant_name', 'merchant_mobile_no','seller_id' ,'price', 'quantity', 'user_comment','order_date', 'mail_status', 'order_processed']

