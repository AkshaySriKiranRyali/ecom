from store.models import Product
class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('ses_key', {})

        if 'ses_key' not in request.session:
            cart = self.session['ses_key'] = {}

        self.cart = cart

    def add(self, product, quantity ):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)
        self.session.modified = True
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
   
    def get_quants(self):
         quantities = self.cart
         return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        ourcart = self.cart
        ourcart[product_id] = product_qty
        self.session.modified = True
        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]   

        self.session.modified = True
    
    def deleteAll(self):
        self.cart.clear()
        self.session.modified = True
            

    def cart_total(self):
        property_ids = self.cart.keys()
        products = Product.objects.filter(id__in=property_ids)
        quantity = self.cart
        total = 0
        for key, value in quantity.items():
            key = int(key)      
            for product in products:
                if product.id == key:
                    total = total + (product.price * value)
        return total

        
