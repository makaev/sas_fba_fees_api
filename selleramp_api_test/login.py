import helpers
import re
import create_user
import requests
import Constants



user = create_user.CreateUser()
logged_user, session = user.login_user()
print(logged_user.text)
