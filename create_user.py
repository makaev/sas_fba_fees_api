from selleramp_api_test import Constants
from selleramp_api_test import helpers
import requests
import json


class CreateUser:

    def __init__(self):
        pass

    default_content_type = 'application/x-www-form-urlencoded'

    def headers_default(self):
        default_headers = helpers.make_headers(authorization=Constants.Constants.BASIC_AUTH_GREEN_SANDBOX,
                                               referer=Constants.Constants.REFERER_GREEN_SANDBOX,
                                               user_agent=Constants.Constants.USER_AGENT)
        self.headers = default_headers
        return default_headers


    def headers_content_type(self, content_type):
        headers = self.headers_default()
        headers['content-type'] = content_type
        return headers


    def get_request_with_basic_auth(self, url, data, headers):
        session = requests.Session()
        response = session.get(url=url, headers=headers, data=data)
        return response


    def post_request_with_basic_auth_and_cookies(self, url, data, headers, cookies):
        session = requests.Session()
        response = session.post(url=url, data=data, headers=headers, cookies=cookies, allow_redirects=True)
        return response, session


    def get_html_login_form(self):
        headers = self.headers_default()
        html_form = self.get_request_with_basic_auth(url=Constants.EndpointsConstants.LOGIN_URL, data={},
                                                     headers=headers)
        csrf_token = helpers.extract_csrf_token_bs(html_content=html_form.text)
        cookies = html_form.cookies

        return html_form, csrf_token, cookies


    def login_user(self):
        html_form, csrf_token, cookies = self.get_html_login_form()
        payload = helpers.payload_for_login(csrf_token=csrf_token,
                                            email=Constants.Predefined_test_data.email,
                                            password=Constants.Predefined_test_data.password,
                                            remeber_me_0=0,
                                            remeber_me_1=1,
                                            login_button='')
        logged_user, session = self.post_request_with_basic_auth_and_cookies(url=Constants.EndpointsConstants.LOGIN_URL,
                                                                                     data=payload,
                                                                                     headers=self.headers_content_type(content_type=self.default_content_type),
                                                                                     cookies=cookies)
        # print(logged_user.text)
        # print(session.cookies.get_dict())
        return logged_user, session
