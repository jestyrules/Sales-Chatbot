# Import libraries
import random

# Product database
products = [
    {"name": "NIKE", "description": "A high-quality product.", "price": 50.0, "availability": True},
    {"name": "ADIDAS", "description": "An affordable option.", "price": 25.0, "availability": True},
    {"name": "PUMA", "description": "A premium choice.", "price": 100.0, "availability": False},
    {"name": "GUCCI", "description": "Great for daily use.", "price": 30.0, "availability": True},
    {"name": "FILA", "description": "Limited edition.", "price": 75.0, "availability": True},
]

# user's cart
user_cart = []


# Greeting message
def greeting():
    return "Hello! How can I help you today?"


# Show available products
def display_products():
    available_products = [product['name'] for product in products if product['availability']]
    if available_products:
        return f"Available products: {', '.join(available_products)}"
    else:
        return "Sorry, all products are currently out of stock."


# Specific product information
def product_details(product_name):
    for product in products:
        if product['name'].lower() == product_name.lower():
            if product['availability']:
                return f"{product['name']}: {product['description']} | Price: ${product['price']}"
            else:
                return f"Sorry, {product['name']} is currently out of stock."
    return "I couldn't find information about that product. Please try another name."


# Recommending a product
def recommend_product(user_preference):
    available_products = [product for product in products if product['availability']]
    if not available_products:
        return "I'm sorry, but we don't have any products in stock at the moment."

    if user_preference.lower() == "affordable":
        product = min(available_products, key=lambda x: x['price'])
    elif user_preference.lower() == "premium":
        product = max(available_products, key=lambda x: x['price'])
    else:
        product = random.choice(available_products)

    return f"I recommend {product['name']} - {product['description']} | Price: ${product['price']}"


# Add a product to the user's cart
def add_to_cart(product_name):
    for product in products:
        if product['name'].lower() == product_name.lower():
            if product['availability']:
                user_cart.append(product)
                return f"{product['name']} has been added to your cart."
            else:
                return f"Sorry, {product['name']} is currently out of stock and cannot be added to your cart."
    return "I couldn't find that product. Please try another name."


# Showing the user's cart
def show_cart():
    if not user_cart:
        return "Your cart is empty."

    cart_items = [product['name'] for product in user_cart]
    total_price = sum(product['price'] for product in user_cart)

    return f"Your cart contains: {', '.join(cart_items)} | Total Price: ${total_price}"


# Function to do purchase
def complete_purchase():
    if not user_cart:
        return "Your cart is empty. There's nothing to purchase."

    total_price = sum(product['price'] for product in user_cart)
    user_cart.clear()

    return f"Thank you for your purchase! You've been charged ${total_price}. Your cart is now empty."


# User Interface Function
def sales_chatbot():
    print(greeting())

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break
        elif "products" in user_input:
            print(display_products())
        elif "tell me about" in user_input:
            product_name = user_input.split("tell me about")[1].strip()
            print(product_details(product_name))
        elif "recommend a product" in user_input:
            user_preference = input("You: What type of product are you looking for (affordable/premium/any)? ").strip()
            print(recommend_product(user_preference))
        elif "add to cart" in user_input:
            product_name = user_input.split("add to cart")[1].strip()
            print(add_to_cart(product_name))
        elif "show me my cart" in user_input:
            print(show_cart())
        elif "complete purchase" in user_input:
            print(complete_purchase())
        else:
            print(
                "I'm not sure how to assist with that. You can ask about products, add to cart, complete purchase, "
                "or ask for recommendations.")


# Run the chatbot
if __name__ == "__main__":
    sales_chatbot()
