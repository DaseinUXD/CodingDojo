# Assignment: Practice your pip in your virtual environment
## Objectives
1. Get accustomed to using commands required to use pip modules.
2. Practice using a virtual environment

Run these commands in the order instructed. Your assignment submission should be a .txt file that includes a short explanation of what you were able to learn about each command by doing a brief (1-2 min) web search for each term. If it is relevant, include the output of your command and your understanding of what it means. It is important to always read your terminal output and try to understand it.

Reminder: when your virtualenv is activated, you may use the pip command. If not, use pip3.

## Run the following commands:  

##### Note: I used a virtual envionment for the first set of commands

`pip install Django==1.11.9`  

* *Installs specific Django version 1.11.9*

`pip list` 
* *Listed all the installed modules and packages within my virtual environment* 

`deactivate` (This will deactivate your virtual environment)  
* *Deactivated the virtual environment I previously activated*
  
`pip3 list`  (How is the result different from when you ran pip list with the virtualenv activated? Hint, you should not have as many things listed when the virtualenv is deactivated. If your results are the same, go back and figure out what went wrong.)  
* *The result is different insofar as the packages and modules listed are installed globally*  
  
`source myVirtualEnvs/py3Env/Scripts/activate`(Adjust the path as needed to re-activate the virtualenv; for windows call myEnvironments/py3Env/Scripts/activate)  

`pip install Django==1.11.9` (We know you already ran this one. What information do you see returned in terminal after this command?)  
Requirement already satisfied: Django==1.11.9 in d:\codingdojo\dojoassignments\python3\myvirtualenvs\py3env\lib\site-packages (1.11.9)  
Requirement already satisfied: pytz in d:\codingdojo\dojoassignments\python3\myvirtualenvs\py3env\lib\site-packages (from Django==1.11.9) (2018.4)  
(py3Env)

`pip freeze` (What's the difference between freeze and list?)  
* `pip freeze` outputs installed packages in requirements format and thus suitable for a requirements file.

Next, `cd` into your Desktop directory (`cd ~/Desktop`), then run this command: `pip freeze > requirements.txt`. What do you see when `ls`? What's inside this file?
* contents of the file are the same results as `pip freeze`

`pip uninstall Django`

Asked if i wanted to:
<a name="Uninstall"></a>Uninstalling Django-1.11.9:
  Would remove:  
  
    d:\codingdojo\dojoassignments\python3\myvirtualenvs\py3env\lib\site-packages\django-1.11.9.dist-info\*
    d:\codingdojo\dojoassignments\python3\myvirtualenvs\py3env\lib\site-packages\django\*
    d:\codingdojo\dojoassignments\python3\myvirtualenvs\py3env\scripts\django-admin.exe
    d:\codingdojo\dojoassignments\python3\myvirtualenvs\py3env\scripts\django-admin.py
    Proceed (y/n)?

I entered 'y' and returned:
  
`Successfully uninstalled Django-1.11.9`  

`pip show Django`  

Returned the active virtual environment:  
`(py3Env)`

Therefore, I reinstalled Django-1.11.9 and then ran `pip show Django`  
Returned:

    $ pip show Django  
    Name: Django  
    Version: 1.11.9  
    Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.  
    Home-page: https://www.djangoproject.com/  
    Author: Django Software Foundation  
    Author-email: foundation@djangoproject.com  
    License: BSD  
    Location: d:\codingdojo\dojoassignments\python3\myvirtualenvs\py3env\lib\site-packages  
    Requires: pytz  
    Required-by:  
    (py3Env)




<a name='Search'></a>'`pip search Flask` This one might take a moment to execute.

Flask-OrientDB (0.1)        - A Flask extension for using OrientDB with Flask  
Flask-Pure (0.5)            - Flask-Pure - a Flask extension for Pure.css  
Flask-SimpleMDE (0.3.0)     - Flask-SimpleMDE - a Flask extension for SimpleMDE  
Fifty-Flask (1.2.0)         - Flask enhancements.  
Flask-AutoIndex (0.6)       - The mod_autoindex for Flask  
Flask-BDEA (0.1.0)          - Flask-BDEA  
Flask-Chargebee (0.0.1)     - Flask-Chargebee  
Flask-Clearbit (0.1.0)      - Flask-Clearbit  
Flask-ElasticUtils (0.1.7)  - ElasticUtils for Flask  
Flask-FileRev (0.1.0)       - Flask-FileRev  
Flask-Gears (0.2)           - Gears for Flask  
Flask-GripControl (0.0.1)   - Flask GripControl  
Flask-Helper (0.19)         - Flask Helper  
Flask-Intercom (0.1.0)      - Flask-Intercom  
Flask-Keen (0.1.0)          - Flask-Keen  
Flask-Mustache (0.4.1)      - Mustache for Flask  
Flask-NextCaller (0.1.0)    - Flask-NextCaller  
Flask-OAuthlib (0.9.5)      - OAuthlib for Flask  
Flask-PubSub (0.1.0)        - Flask-PubSub  
Flask-Quik (0.1.1)          - Quik for Flask  
Flask-Shopify (0.2)         - Shopify Flask  
Flask-SPF (0.0.0)           - Flask-SPF  
Flask-SRI (0.1.0)           - Flask-SRI  
Flask-Stripe (0.1.0)        - Flask-Stripe  
Flask-TaskTiger (0.0.1)     - Flask TaskTiger  
flask-toolbox (0.0.2)       - A flask toolbox.  
Flask-Turbolinks (0.2.0)    - Turbolinks for Flask.  
Flask-Watson (0.1.0)        - Flask-Watson  
Flask-Weixin (0.5.0)        - Weixin for Flask.  
flask-ws (0.0.1.0)          - Websocket for flask.  
flask-ypaginate (0.1.3)     - Pagination for Flask  
sockjs-flask (0.3)          - SockJs for Flask  
airbrake-flask (1.0.7)      - airbrake-flask - Airbrake client for Python Flask  
Flask-Diced (0.3)           - Flask-Diced - CRUD views generator for Flask  
Flask-GeoIP (0.1.3          - Flask-GeoIP
Flask-GeoIP (0.1.3)         - Flask-GeoIP  

-------------

Simple Flask extension for pygeoip.  
flask-myapi (0.1)           - Flask-MyAPI - RESTful support library for Flask  
Flask-LoginManager (1.1.6)  - Flask-Loginmanager supports multiple roles and permissions for Flask, inspired by Flask-Login  
Flask-RESTive (0.0.3)       - Flask RESTive is a REST API Flask extension based on Flask-RESTful & Marshmallow.  
Flask-FlatPagesCut (0.5.1)  - Flask-FlatPagesCut is fork Flask-FlatPages (Provides flat static pages to a Flask application)  
flask-coffee2js (0.1.2)     - A small Flask extension that adds CoffeScript support to Flask.  
Flask-Collect (1.3.2)       - Flask-Collect -- Collect static files in Flask application  
flask-filters (0.3)         - The Flask Filter to use with flask-restful and Relational DB  
flask-lesscss (0.9.1)       - A small Flask extension that adds LessCSS support to Flask.  
flask-shell (0.1.3)         - Flask extension to improve shell command for the Flask CLI.  
flask-stylus2css (0.1)      - A small Flask extension that adds Stylus support to Flask.  
castle-flask (0.0.1)        - A Flask client for Castle.io  
Flask-Airbrake (0.0.3)      - Flask extension for Airbrake  
Flask-Alchy (0.5.0)         - Flask extension for alchy  
Flask-Auth (0.85)           - Auth extension for Flask.  
Flask-Autodoc (0.1.2)       - Documentation generator for flask  
Flask-Avatar (0.1.3)        - To generate avatar for flask  
Flask-Bcrypt (0.7.1)        - Brcrypt hashing for Flask.  
flask-blitzdb (0.1)         - Flask extension for blitzdb  
flask-bluelogin (0.2.7)     - Flask BlueLogin module  
flask-blueprint (1.2.2)     - Flask blueprint generator  
flask-bluestatic (0.1.0)    - Flask BlueStatic module  
Flask-Breve (0.2)           - Breve templating with Flask  
Flask-Builder (0.9)         - Flask-application factory  
Flask-Captain (0.1.1)       - Handle webhooks with Flask  
Flask-CAS (1.0.1)           - Flask extension for CAS  
Flask-CassandraDB (0.0.1)   - connect cassandra to flask  
Flask-Celery (2.4.3)        - Celery integration for Flask  
Flask-CKEditor (0.4.0)      - CKEditor integration for Flask.  
Flask-Config (0.2.1)        - Flask configuration class  
Flask-CuttlePool (0.2.0)    - A Flask extension for CuttlePool  
Flask-DBKit (0.0.1)         - dbkit integration for Flask.  
flask-discoverer (0.0.2)    - Flask API autodiscovery  
flask-dynamo (0.1.2)        - DynamoDB integration for Flask.  
Flask-Edits (0.8)           - Editable Content in Flask  
Flask-Enterprise (1.0)      - Enterprise capabilities for Flask  
flask-erppeek (1.0.1)       - ERPPeek Connector for Flask  
Flask-Extension (1.0)       - Demo for flask extension.  
Flask-Failsafe (0.2)        - A failsafe for the Flask reloader  
Flask-Flarf (0.0.5)         - Flask request filtering  
Flask-Fleem (0.0.5)         - Theming for Flask applications  
Flask-FluidDB (0.1)         - Fluiddb access for flask  
Flask-Formspree (0.3)       - formspree flask extension  
Flask-Fulfil (0.2.1)        - Fulfil.IO for Flask Apps  
Flask-Funnel (0.1.10)       - Asset management for Flask.  
flask-handlers (0.0.1)      - Handlers for Flask applications  
Flask-HttpCaching (0.01)    - flask http caching  
flask-hype (0.1.4)          - Flask extension for hype  
flask-iMail (0.1)           - Mailgun integration for Flask.  
flask-journey (0.1.4)       - Flask blueprint management  
flask-kser (0.2.1)          - Flask KSer example  
Flask-Lastuser (0.3.12)     - Flask extension for Lastuser  
Flask-Latch (0.1.0)         - Latch extension for Flask  
flask-logmanager (0.2.10)   - Flask LogManager module  
flask-logsocketio (0.1.4)   - Flask LogSocketIo module  
flask-macros (0.1.5)        - macros for flask projects  
flask-manager (0.0.1)       - A CRUD manager for Flask  
Flask-mongobit (0.1.2)      - MongoBit support in Flask  
Flask-MongoDB (0.0.1a8)     - MongoDB flask extension  
flask-monitor (0.2.6)       - Flask Monitor module  
Flask-MySQLdb (0.2.0)       - MySQLdb extension for Flask  
flask-nap (0.1)             - Flask REST Framework  
Flask-Navigation (0.2.0)    - The navigation of Flask application.  
flask-now (0.1.5)           - Flask App Generator  
Flask-OAuthRes (0.2.0)      - OAuth Resource for Flask  
Flask-OpenERP (0.3.1)       - OpenERP Connector for Flask  
(py3Env)  
markm@Aletheia MINGW64 ~/Desktop  
$


# Research Findings/Results
## pip
### Reference Guide
* [For extensive information on pip](https://pip.pypa.io/en/stable/reference/pip/)
### Basic Information
* pip is already installed for Python 2 >= 2.7.9 or Python 3 > 3.4 downloaded from [python.org](https://www.python.org "python.org")
* pip is a command line program. When you install pip, a pip command is added to your system, which can be run from the command prompt as follows:  
`$ pip <pip arguments>`
### Installing Packages
The most common scenario is to install from PyPI using Requirement Specifiers

    $ pip install SomePackage            # latest version  
    $ pip install SomePackage==1.0.4     # specific version  
    $ pip install 'SomePackage>=1.0.4'     # minimum version  
### Requirement Files
"Requirement Files" are files containing a list of items to be installed using p0ip0 install like so:  

    $ pip install -r requirements.txt
### pip list
#### Usage
`pip [options]`
#### Description
List installs packages, including editables.

Packages are listed in a case-insensitive sorted order.
#### Options

* __-o, --outdated__  
List outdated packages

* __-u, --uptodate__  
List uptodate packages

* __-e, --editable__  
List editable projects.

* __-l, --local__  
If in a virtualenv that has global access, do not list globally-installed packages.

* __--user__  
Only output packages installed in user-site.

* __--pre__  
Include pre-release and development versions. By default, pip only finds stable versions.

* __--format <list_format>__  
Select the output format among: columns (default), freeze, json, or legacy.

* __--not-required__  
List packages that are not dependencies of installed packages.

* __--exclude-editable__  
Exclude editable package from output.

* __--include-editable__  
Include editable package from output.

* __-i, --index-url <url>__  
Base URL of Python Package Index (default https://pypi.org/simple). This should point to a repository compliant with PEP 503 (the simple repository API) or a local directory laid out in the same format.

* __--extra-index-url <url>__  
Extra URLs of package indexes to use in addition to --index-url. Should follow the same rules as --index-url.

* __--no-index__  
Ignore package index (only looking at --find-links URLs instead).

* __-f, --find-links <url>__  
If a url or path to an html file, then parse for links to archives. If a local path or file:// url that's a directory, then look for archives in the directory listing.

* __--process-dependency-links__  
Enable the processing of dependency links.

###deactivate (virtualenv)  
Deactivates an active virtual environment

###pip freeze
*  Output installed packages in requirements format.
*  Suitable for generating a requirements file  
#### Example  
`pip freeze > requirements.txt`

###pip uninstall
#### Usage  
`pip [options] <package>...`  
`pip [options] -r <requirements file>...`
#### Description
Uninstall packages.  
pip is able to uninstall most installed packages. Known exceptions are:
* Pure distutils packages installed with `python setup.py install`, which leave behind no metadata to determine what files were installed.
* Script wrappers installed by `python setup.py develop`.
#### Options
**-r, --requirement** `<file>`

* Uninstall all the packages listed in the given requirements file.  This option can be used multiple times.

**-y, --yes**
* Don't ask for confirmation of uninstall deletions.
#### Example
* <a href="#Uninstall">See usage above.</a>  

### pip show
#### Usage
`pip [options] <package>`  
##### Description
* Show information about one or more installed packages
#### Options
*  **-f, --files**
*  **--verbose**

### pip search
#### Usage
`pip [options] <querry>`
####Description
Search for PyPI packages whose name or summary contains `<query>`.

#### Options
**-i, --index `<url>`**
* Base URL of Python Package Index (default https://pypi.org/pypi).

#### Examples
* <a href="#Search">See usage above.</a>  
