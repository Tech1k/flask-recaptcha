# Flask-Turnstile

A Cloudflare Turnstile extension for Flask based on flask-recaptcha.

---

## Install

    pip install flask-turnstile

# Usage

### Implementation view.py

    from flask import Flask
    from flask_turnstile import Turnstile

    app = Flask(__name__)
    turnstile = Turnstile(app=app)
    
    #or 
    
    turnstile = Turnstile()
    turnstile.init_app(app)
    

### In your template: **{{ turnstile }}**

Inside of the form you want to protect, include the tag: **{{ turnstile }}**

It will insert the code automatically


    <form method="post" action="/submit">
        ... your field
        ... your field

        {{ turnstile }}

        [submit button]
    </form>


### Verify the captcha

In the view that's going to validate the captcha

    from flask import Flask
    from flask_turnstile import Turnstile

    app = Flask(__name__)
    turnstile = Turnstile(app=app)

    @route("/submit", methods=["POST"])
    def submit():

        if turnstile.verify():
            # SUCCESS
            pass
        else:
            # FAILED
            pass


## Api

**turnstile.__init__(app, site_key, secret_key, is_enabled=True)**

**turnstile.get_code()**

Returns the HTML code to implement. But you can use
**{{ turnstile }}** directly in your template

**turnstile.verfiy()**

Returns bool

## In Template

Just include **{{ turnstile }}** wherever you want to show the captcha


## Config

Flask-Turnstile is configured through the standard Flask config API.
These are the available options:

**TURNSTILE_ENABLED**: Bool - True by default, when False it will bypass validation

**TURNSTILE_SITE_KEY** : Public key

**TURNSTILE_SECRET_KEY**: Private key

The following are **Optional** arguments.

    TURNSTILE_ENABLED = True
    TURNSTILE_SITE_KEY = ""
    TURNSTILE_SECRET_KEY = ""

---

(c) 2015 Mardix
(c) 2023 Kristian
