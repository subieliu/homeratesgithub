from flask import Flask, render_template, url_for, request, redirect, jsonify, flash
import json
app = Flask(__name__)

li = ["info@homeratesonline.com", "1712omnifundmichaeltonwebleads@robot.zapier.com"]

app.secret_key = b'testtest'
@app.route("/", methods=['GET'])
def index():
    #if 'success' in list(request.args):
        #flash('Thank you for your inquiry, a licensed mortgage professional will contact you shortly to go over your Loan Approval options')
    return render_template('index.html')

@app.route("/refinance", methods=['GET', 'POST'])
def refinance():
    if request.method == 'POST':
        email_body = 'Subject: Home Rate Loan Website Customer \n\n'
        email_body += 'Customer from HomeRateLoan\n'
        submitted = json.loads(list(request.form)[0])
        email_body += 'Name: {}\n'.format(submitted['name'])
        email_body += 'State: {}\n'.format(submitted['state'])
        email_body += 'Property Use: {}\n'.format(submitted['typer'])
        email_body += 'Property Type: {}\n'.format(submitted['propertyType'])
        email_body += 'Current Loan Balance: {}\n'.format(submitted['currentLoanBalance'])
        email_body += 'Current Property Value: {}\n'.format(submitted['currentPropertyValue'])
        email_body += 'Cash Request: {}\n'.format(submitted['howMuchCash'])
        email_body += 'Zip Code: {}\n'.format(submitted['zip'])
        email_body += 'Credit: {}\n'.format(submitted['credit'])
        email_body += 'Email: {}\n'.format(submitted['email'])
        email_body += 'Phone Number: {}\n'.format(submitted['tel'])
        print(submitted)
        print(email_body)
        send_mail(email_body)
        # return redirect(url_for('index'))
        flash('Thank you for your request, a licensed loan agent for your area will contact you shortly OR call now (800)996-8196.')
        return jsonify({"emailSent": True})
    return render_template('refinance.html')

@app.route("/purchase", methods=['GET', 'POST'])
def purchase():
    if request.method == 'POST':
        email_body = 'Subject: Home Rate Loan Website Customer \n\n'
        email_body += 'Customer from HomeRateLoan\n'
        submitted = json.loads(list(request.form)[0])
        email_body += 'Name: {}\n'.format(submitted['name'])
        email_body += 'State: {}\n'.format(submitted['state'])
        email_body += 'Property Use: {}\n'.format(submitted['typer'])
        email_body += 'Property Type: {}\n'.format(submitted['propertyType'])
        email_body += 'Cash Out: {}\n'.format(submitted['approxPurchasePrice'])
        email_body += 'Current Property Value: {}\n'.format(submitted['currentPropertyValue'])
        email_body += 'Credit: {}\n'.format(submitted['credit'])
        email_body += 'Email: {}\n'.format(submitted['email'])
        email_body += 'Phone Number: {}\n'.format(submitted['tel'])
        print(submitted)
        print(email_body)
        send_mail(email_body)
        flash('Thank you for your request, a licensed loan agent for your area will contact you shortly OR call now (800)996-8196.')
        return jsonify({"emailSent": True})
    return render_template('purchase.html')


def send_mail(body):
    import smtplib
    # list of email_id to send the mail

    for i in range(len(li)):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("testbaokhoa@gmail.com", "dbojbhjjtjzqwede")
        message = body
        s.sendmail("sender_email_id", li[i], message)
        s.quit()
app.run(host='0.0.0.0', port=8080, debug=True)
