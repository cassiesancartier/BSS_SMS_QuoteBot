'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncomment to configure in file.
ACCOUNT_SID = "ACba92b413588da3fb9e475a5344e0e3ce" 
AUTH_TOKEN = "183f87a88bf7230e8192ec1b54e5b68b"
BSSSPAM_APP_SID = "APc36deb3789ab04c3918e72299365ca6d"
BSS_SPAM_ID = "+19789562878"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACba92b413588da3fb9e475a5344e0e3ce']
AUTH_TOKEN = os.environ['183f87a88bf7230e8192ec1b54e5b68b']
BSSSPAM_APP_SID = os.environ['APc36deb3789ab04c3918e72299365ca6d']
BSS_SPAM_ID = os.environ['+19789562878']
