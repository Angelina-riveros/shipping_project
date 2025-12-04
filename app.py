from flask import Flask, render_template, request

app = Flask(__name__)



#Homepage
@app.route('/')
def home():
    return render_template('index.html')


#Price calculator
@app.route('/price', methods=['GET', 'POST'])
def price():
    total = None

    if request.method == 'POST':
        weight = float(request.form['weight'])
        speed = request.form['speed']

        base = weight * 0.5

        if speed == "ground":
            total = base + 5
        elif speed == "two_day":
            total = base + 10
        else:
            total = base + 2
    return render_template('price.html', total=total)



#Package tracking
@app.route('/tracking', methods=['GET', 'POST'])
def tracking():
    package = None

    if request.method == 'POST':
        tracking = request.form['tracking']

        #Placeholder to replace with SQL SELECT later
        package = {
            "tracking_number": tracking,
            "status": "In Transit",
            "delivery_date": "2025-12-8"
        }
    return render_template('tracking.html', package=package)


#Reschedule delivery

@app.route('/reschedule', methods=['GET', 'POST'])
def reschedule():
    message = None

    if request.method == 'POST':
        tracking = request.form['tracking']
        new_date = request.form['date']
        # Placeholder to replace with SQL update later
        message = f"Delivery for {tracking} rescheduled to {new_date}."
    return render_template('reschedule.html', message=message)


#Customer dashboard

@app.route('/customers')
def customers():
    fake_customers = [
        {"id": 1, "name": "Alice Smith", "email": "alice@example.com"},
        {"id": 2, "name": "Bob Johnson", "email": "bob@example.com"},
    ]
    return render_template('customer_dashboard.html', customers=fake_customers)


#Employee dashboard

@app.route('/employees')
def employees():
    fake_employees = [
        {"id": 1, "name": "John Worker", "role": "Driver"},
        {"id": 2, "name": "Sara Manager", "role": "Manager"},
    ]
    return render_template('employee_dashboard.html', employees=fake_employees)


#Inquiries

@app.route('/inquiries')
def inquiries():
    fake_inquiries = [
        {"id": 1, "message": "Where is my package?", "status": "Open"},
        {"id": 2, "message": "Billing question", "status": "Closed"},
    ]
    return render_template('inquiries.html', inquiries=fake_inquiries)


#Shipments

@app.route('/shipments')
def shipments():
    fake_shipments = [
        {"shipment_id": 101, "tracking": "ABC123", "status": "In Transit"},
        {"shipment_id": 102, "tracking": "XYZ789", "status": "Delivered"},
    ]
    return render_template('shipments.html', shipments=fake_shipments)


#Packages

@app.route('/packages')
def packages():
    fake_packages = [
        {"package_id": 1, "weight": 12, "type": "Box"},
        {"package_id": 2, "weight": 5, "type": "Envelope"},
    ]
    return render_template('packages.html', packages=fake_packages)


#Payments

@app.route('/payments')
def payments():
    fake_payments = [
        {"payment_id": 1, "customer": "Alice", "amount": 22.50, "status": "Paid"},
        {"payment_id": 2, "customer": "Bob", "amount": 15.00, "status": "Pending"},
    ]
    return render_template('payments.html', payments=fake_payments)


#Vehicles

@app.route('/vehicles')
def vehicles():
    fake_vehicles = [
        {"vehicle_id": 1, "model": "Ford Transit", "status": "Active"},
        {"vehicle_id": 2, "model": "Mercedes Van", "status": "In Repair"},
    ]
    return render_template('vehicles.html', vehicles=fake_vehicles)

if __name__ == '__main__':
    app.run(debug=True)