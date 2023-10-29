from flask import Flask, render_template

app = Flask(__name__)

# Dummy product data for demonstration
products = [
    {"id": 1, "name": "Product 1", "price": 10.00, "image": "product1.jpg"},
    {"id": 2, "name": "Product 2", "price": 15.00, "image": "product2.jpg"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product.html', product=product)
    return "Product not found"

@app.route('/cart')
def cart():
    return render_template('cart.html', products=products)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
