# disability-parking-badge-automation

### Ministry of Transport would not respond to the online form, so I automated it to keep sending until they do.

To use this script you'll need to install the `requirements.txt` using:
```
pip install -r requirements.txt
```

and have a `.env` file in the same folder that looks like that:

```
DRIVER_PATH='Path/to/Firefox WebDriver'
PDF_PATH='/Path/to/ApplicationForm.pdf'
FULL_NAME='Your Name'
ID='111111111'
EMAIL='youremail@mail.com'
PHONE_NUMBER='0501234567'
```
