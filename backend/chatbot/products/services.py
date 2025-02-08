from products.models import Product
from features.models import Feature

class ProductService:
    @staticmethod
    def find_all():
        return Product.objects.all()
    
    @staticmethod
    def create_product(data):
        features_data = data.pop("features", [])
        product = Product.objects.create(**data)
        
        # Agregar features al producto
        for feature_id in features_data:
            feature = Feature.objects.get(id=feature_id)
            product.features.add(feature)
        return product
    


    @staticmethod
    def find_by_id(product_id):
        return Product.objects.filter(id=product_id).first()
    
    @staticmethod
    def update_product(product:Product, data):
        features_data = data.pop("features", [])
        
        # Actualizar datos del producto
        for key, value in data.items():
            setattr(product, key, value)
        product.save()

        # Actualizar features
        if features_data:
            product.features.clear()
            for feature_id in features_data:
                feature = Feature.objects.get(id=feature_id)
                product.features.add(feature)

        return product

    @staticmethod
    def delete_product(product:Product):
        product.delete()