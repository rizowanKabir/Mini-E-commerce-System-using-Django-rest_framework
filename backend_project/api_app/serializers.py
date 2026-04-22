from rest_framework import serializers
from .models import ProductModel,OrderModel,OrderItem

# Serializer create here: 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id','name','description','price','stock']

    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return value
    
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(source='product.price',max_digits=10,decimal_places=2)
    class Meta:
        model = OrderItem
        fields = ['product_name','product_price','quantity','item_subtotal']    


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)
    total_price = serializers.SerializerMethodField(method_name='total')

    def total(self, obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)


    class Meta:
        model = OrderModel
        fields = ['order_id','user','created_at','status','items','total_price']     



