# python -m flask --app easymed run
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('easymed.html')


@app.route('/medicine')
def medicine():
    return render_template('medicine.html')


@app.route('/cognitive')
def cognitive():
    # This serves cognative.html (uploaded file)
    return render_template('cognative.html')


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.png')


@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    email = request.form.get('email')
    print(f"Appointment booked with email: {email}")
    return "Appointment successfully booked! We will contact you soon."


@app.route('/submit_purchase', methods=['POST'])
def submit_purchase():
    medicine = request.form.get('medicine')
    quantity = request.form.get('quantity')
    payment_method = request.form.get('payment')
    delivery_address = request.form.get('address')

    print(f"Medicine: {medicine}")
    print(f"Quantity: {quantity}")
    print(f"Payment Method: {payment_method}")
    print(f"Delivery Address: {delivery_address}")

    return f"Your order for {quantity} of {medicine} has been placed successfully! We will deliver it to {delivery_address}."


if __name__ == '__main__':
    app.run(debug=True)
