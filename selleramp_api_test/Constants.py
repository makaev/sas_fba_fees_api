class Constants:

    BASE_URL_GREEN_SANDBOX = "https://green-sandbox.selleramp.com"
    BASE_URL_BLUE_SANDBOX = "https://blue-sandbox.selleramp.com"
    BASE_URL_GREEN_STAGE = "https://blue-stage.selleramp.com"
    BASE_URL_BLUE_STAGE = "https://blue-stage.selleramp.com"
    BASE_URL_GREEN_SAS = "https://green-sas.selleramp.com"
    BASE_URL_BLUE_SAS = "https://blue-sas.selleramp.com"

    BASIC_AUTH_GREEN_SAS = 'Basic c2FzOjNueDI2dDNyZ3UwbWxkOGc='
    BASIC_AUTH_BLUE_SAS = 'Basic c2FzOjNueDI2dDNyZ3UwbWxkOGc='
    BASIC_AUTH_GREEN_STAGING = "Basic c2FzOjBjZGk0am1zdnFpOG1nZnM="
    BASIC_AUTH_BLUE_STAGING = "Basic c2FzOjBjZGk0am1zdnFpOG1nZnM="
    BASIC_AUTH_GREEN_SANDBOX = "Basic c2FzOnRhNXM4cGFmaW9qa3R2NjE="
    BASIC_AUTH_BLUE_SANDBOX = "Basic c2FzOnRhNXM4cGFmaW9qa3R2NjE="

    REFERER_GREEN_SANDBOX = BASE_URL_GREEN_SANDBOX + "/"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    X_API_TOKEN = 'jN13FmoMX4pzmBN0-Emxdo1P1OWszd50'
    X_UID = '11'
    IDENTITY_SASEND = '_identity-sasend=57d146c07c9a307323478de8b57e4c201eba0689f57b2436547a6ea98fc19e43a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_identity-sasend%22%3Bi%3A1%3Bs%3A47%3A%22%5B11%2C%22k1XXcp-T7qLefQ08sU-JJ66ZLidOX6aB%22%2C2592000%5D%22%3B%7D'
    WUKN = 'ddb7cee4c766425ef89ddcfc17dadb0324f93d6f2a748395c401016b143a128ba%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22wukn%22%3Bi%3A1%3Bs%3A36%3A%22b3ee8a17-780d-4328-a4fa-5255f3f0a02d%22%3B%7D'

class EndpointsConstants():

    LOGIN = "/site/login"
    LOGIN_URL = "https://green-sandbox.selleramp.com/site/login"
    FEE_ENGINE_API_URL = "https://green-sandbox.selleramp.com/api/"
    LOOKUP = "/sas/lookup"
    LOOKUP_SEARCH_TERM = "/sas/lookup?SasLookup%5Bsearch_term%5D="
    API_DO = "/api/do"


class Predefined_test_data:

    email = 'a.makaev%2B1%40mobidev.biz'
    password = 'Dev.5462:'



class Headers:

    def __init__(self, authorization, referer, user_agent):
        self.authorization = authorization
        self.referer = referer
        self.user_agent = user_agent


    def headers_with_basic_auth(self, authorization, referer, user_agent):
        headers = {
            'authorization': authorization,
            'referer': referer,
            'user-agent': user_agent
        }
        return headers


    def headers_with_basic_auth_and_content_type(self, authorization, referer, user_agent):
        headers = {
            'authorization': authorization,
            'referer': referer,
            'user-agent': user_agent
        }
        return headers


    def headers_with_basic_auth_and_cookies(self, authorization, referer, user_agent, cookie):
        headers = {
            'authorization': authorization,
            'referer': referer,
            'user-agent': user_agent,
            'cookie':cookie
        }
        return headers


    def headers_for_fee_engine_api(self, authorization, x_api_token, x_uid):
        headers = {
            'authorization': authorization,
            'x-api-token': x_api_token,
            'x-uid': x_uid
        }
        return headers