# Shortener
A very simple url shortener written in Python using Django. Similar to a service like bit.ly or tinyurl, given a url, the site returns a smaller link in the shortener's domain, which redirects to the given url when searched. 

# Usage
## Clone repository
```
git clone https://github.com/tarush-g/shortener.git
cd shortener
```
## Install dependencies
```
pip install -r requirements.txt
```
## Migrate databases
```
python manage.py migrate
```
## Run server
```
python manage.py runserver
```
Make sure to include a .env file with the Django [secret key](https://docs.djangoproject.com/en/4.2/topics/signing/#protecting-secret-key-and-secret-key-fallbacks) as an environment variable.




