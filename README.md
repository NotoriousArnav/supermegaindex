# Super Mega Index
An Large Index of Mega.nz Links.

## Install
1. Clone the Repo
```bash
git clone https://github.com/NotoriousArnav/supermegaindex.git
cd supermegaindex
```
2. Run pip3 to install dependencies
```bash
pip3 install -r requirements.txt
```
3. Run using gunicorn
```bash
gunicorn --reload superindex.wsgi:app 0.0.0.0:8000
```

**If you are Hosting it in a Server then Read NGINX or Apache Docs on how to setup a reverse proxy and make this a system service

**Also Make Sure you have a Admin Account on the Instance to Control the Data Circulation. To do that just run the following command
```bash
python manage.py createsuperuser
```

## API
- /api/auth/token/
Route for generating User API Tokens for Token Based Auth
cURL (Token Generation):
```bash
curl -X POST \
    -H 'Content-Type: application/json'\
    -d '{"username":"foo","password":"bar"}'\
    https://arnv2004.pythonanywhere.com
```

Usage:

Just Include "Authorization" Header with "Token your_token" to access any Route that requires API Key, like /api/records (POST)

cURL (Example Usage):
```bash
curl -H 'Authorization: Token your_token' \
    https://arnv2004.pythonanywhere.com
```

- /api/records
    - GET
    Using the API with GET Request doesn't require any API key and is free to use.

    cURL (Fetch Data):
    ```bash
    curl https://arnv2004.pythonanywhere.com/api/records | jq # jq isn't required but is a nice to have tool :)
    ```
    - POST
    Using POST Request Requires an API key, to avoid spam in database. See example_scripts/example_bulk_upload_script.py

**To Ensuure a Good User Experience, all the API endoints are made with Django Rest Framework to have a nice GUI when opened in browser.
