from flask import Flask
from flask_turnstile import Turnstile

app = Flask(__name__)
app.config.update({
    "debug": True,
    "TURNSTILE_SITE_KEY": "SITE_KEY",
    "TURNSTILE_SITE_SECRET": "SECRET",
    "TURNSTILE_ENABLED": True
})

def test_turnstile_enabled():
    turnstile = Turnstile(site_key="SITE_KEY", secret_key="SECRET_KEY")
    assert isinstance(turnstile, Turnstile)
    assert turnstile.is_enabled == True
    assert "script" in turnstile.get_code()
    assert turnstile.verify(response="None", remote_ip="0.0.0.0") == False

def test_turnstile_enabled_flask():
    turnstile = Turnstile(app=app)
    assert isinstance(turnstile, Turnstile)
    assert turnstile.is_enabled == True
    assert "script" in turnstile.get_code()
    assert turnstile.verify(response="None", remote_ip="0.0.0.0") == False

def test_turnstile_disabled():
    turnstile = Turnstile(site_key="SITE_KEY", secret_key="SECRET_KEY", is_enabled=False)
    assert turnstile.is_enabled == False
    assert turnstile.get_code() == ""
    assert turnstile.verify(response="None", remote_ip="0.0.0.0") == True

def test_turnstile_disabled_flask():
    app.config.update({
        "TURNSTILE_ENABLED": False
    })
    turnstile = Turnstile(app=app)
    assert turnstile.is_enabled == False
    assert turnstile.get_code() == ""
    assert turnstile.verify(response="None", remote_ip="0.0.0.0") == True
