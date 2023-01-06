from setuptools import setup, find_packages
import flask_turnstile

PACKAGE = flask_turnstile

setup(
    name=PACKAGE.__NAME__,
    version=PACKAGE.__version__,
    license=PACKAGE.__license__,
    author=PACKAGE.__author__,
    author_email='kristian@kk.dev',
    description="A Cloudflare Turnstile extension for Flask based on flask-recaptcha",
    long_description=PACKAGE.__doc__,
    url='http://github.com/tech1k/flask-turnstile/',
    download_url='http://github.com/tech1k/flask-turnstile/tarball/master',
    py_modules=['flask_turnstile'],
    include_package_data=True,
    install_requires=[
        "flask",
        "requests",
        "MarkupSafe"
    ],
    keywords=['flask', 'turnstile', "validate"],
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False
)
