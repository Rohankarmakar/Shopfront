from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from .models import Product, Review, Order, OrderItem, ShippingAddress


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ["user", "created_at", "updated_at"]
        read_only_fields = ["_id"]
        extra_kwargs = {
            "name": {"required": True},
            "image": {"required": False},
            "brand": {"required": True},
            "category": {"required": True},
            "description": {"required": False},
            "rating": {"required": False, "validators": [MinValueValidator(0)]},
            "numReviews": {"required": False, "validators": [MinValueValidator(0)]},
            "price": {"required": True, "validators": [MinValueValidator(0.0)]},
            "countInStock": {"required": True, "validators": [MinValueValidator(0)]},
        }


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "product", "user", "name", "rating", "comment", "created_at"]
        read_only_fields = ["id", "created_at"]
        extra_kwargs = {
            "product": {"required": True},
            "user": {"required": True},
            "name": {"required": True},
            "rating": {"required": True, "validators": [MinValueValidator(0)]},
            "comment": {"required": False},
        }

        def create(self, validated_data):
            return Review.objects.create(**validated_data)


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "product", "order", "name", "qty", "price"]
        read_only_fields = ["id", "order"]
        extra_kwargs = {
            "product": {"required": True},
            "order": {"required": False},
            "name": {"required": True},
            "qty": {"required": True, "validators": [MinValueValidator(0)]},
            "price": {"required": True, "validators": [MinValueValidator(0.0)]},
        }


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "paymentMethod",
            "taxPrice",
            "shippingPrice",
            "totalPrice",
            "isPaid",
            "paidAt",
            "isDelivered",
            "deliveredAt",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "user": {"required": True},
            "paymentMethod": {"required": True},
            "taxPrice": {"required": True, "validators": [MinValueValidator(0.0)]},
            "shippingPrice": {"required": True, "validators": [MinValueValidator(0.0)]},
            "totalPrice": {"required": True, "validators": [MinValueValidator(0.0)]},
            "isPaid": {"required": False},
            "paidAt": {"required": False},
            "isDelivered": {"required": False},
            "deliveredAt": {"required": False},
        }


class ShippingAddressSerializer(ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = [
            "id",
            "order",
            "address",
            "city",
            "postalCode",
            "country",
            "shippingPrice",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
        extra_kwargs = {
            "order": {"required": False},
            "address": {"required": True},
            "city": {"required": True},
            "postalCode": {"required": True},
            "country": {"required": True},
            "shippingPrice": {"required": True, "validators": [MinValueValidator(0.0)]},
        }


class OrderItemDetailSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product", "order", "name", "qty", "price"]
        read_only_fields = ["id", "order"]
        extra_kwargs = {
            "product": {"required": True},
            "order": {"required": False},
            "name": {"required": True},
            "qty": {"required": True, "validators": [MinValueValidator(0)]},
            "price": {"required": True, "validators": [MinValueValidator(0.0)]},
        }


class OrderDetailSerializer(ModelSerializer):
    order_items = OrderItemDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "paymentMethod",
            "taxPrice",
            "shippingPrice",
            "totalPrice",
            "isPaid",
            "paidAt",
            "isDelivered",
            "deliveredAt",
            "created_at",
            "updated_at",
            "order_items",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "user": {"required": True},
            "paymentMethod": {"required": True},
            "taxPrice": {"required": True, "validators": [MinValueValidator(0.0)]},
            "shippingPrice": {"required": True, "validators": [MinValueValidator(0.0)]},
            "totalPrice": {"required": True, "validators": [MinValueValidator(0.0)]},
            "isPaid": {"required": False},
            "paidAt": {"required": False},
            "isDelivered": {"required": False},
            "deliveredAt": {"required": False},
        }


class ShippingAddressDetailSerializer(ModelSerializer):
    order = OrderDetailSerializer(read_only=True)

    class Meta:
        model = ShippingAddress
        fields = [
            "id",
            "order",
            "address",
            "city",
            "postalCode",
            "country",
            "shippingPrice",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
        extra_kwargs = {
            "order": {"required": False},
            "address": {"required": True},
            "city": {"required": True},
            "postalCode": {"required": True},
            "country": {"required": True},
            "shippingPrice": {"required": True, "validators": [MinValueValidator(0.0)]},
        }


class ReviewDetailSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "product", "user", "name", "rating", "comment", "created_at"]
        read_only_fields = ["id", "created_at"]
        extra_kwargs = {
            "product": {"required": True},
            "user": {"required": True},
            "name": {"required": True},
            "rating": {"required": True, "validators": [MinValueValidator(0)]},
            "comment": {"required": False},
        }

        def create(self, validated_data):
            return Review.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.rating = validated_data.get("rating", instance.rating)
            instance.comment = validated_data.get("comment", instance.comment)
            instance.save()
            return instance


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "_id",
            "name",
            "image",
            "brand",
            "category",
            "description",
            "rating",
            "numReviews",
            "price",
            "countInStock",
            "created_at",
            "updated_at",
            "user",
        ]
        read_only_fields = ["_id", "created_at", "updated_at"]
        extra_kwargs = {
            "name": {"required": True},
            "image": {"required": False},
            "brand": {"required": True},
            "category": {"required": True},
            "description": {"required": False},
            "rating": {"required": False, "validators": [MinValueValidator(0)]},
            "numReviews": {"required": False, "validators": [MinValueValidator(0)]},
            "price": {"required": True, "validators": [MinValueValidator(0.0)]},
            "countInStock": {"required": True, "validators": [MinValueValidator(0)]},
        }

        def create(self, validated_data):
            return Product.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get("name", instance.name)
            instance.image = validated_data.get("image", instance.image)
            instance.brand = validated_data.get("brand", instance.brand)
            instance.category = validated_data.get("category", instance.category)
            instance.description = validated_data.get(
                "description", instance.description
            )
            instance.rating = validated_data.get("rating", instance.rating)
            instance.numReviews = validated_data.get("numReviews", instance.numReviews)
            instance.price = validated_data.get("price", instance.price)
            instance.countInStock = validated_data.get(
                "countInStock", instance.countInStock
            )
            instance.save()
            return instance


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "image"]
        read_only_fields = ["id"]
        extra_kwargs = {
            "image": {"required": True},
        }

        def create(self, validated_data):
            return Product.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.image = validated_data.get("image", instance.image)
            instance.save()
            return instance


class ProductReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "product", "user", "name", "rating", "comment", "created_at"]
        read_only_fields = ["id", "created_at"]
        extra_kwargs = {
            "product": {"required": True},
            "user": {"required": True},
            "name": {"required": True},
            "rating": {"required": True, "validators": [MinValueValidator(0)]},
            "comment": {"required": False},
        }

        def create(self, validated_data):
            return Review.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.rating = validated_data.get("rating", instance.rating)
            instance.comment = validated_data.get("comment", instance.comment)
            instance.save()
            return instance
