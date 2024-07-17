import requests
import re
from bs4 import BeautifulSoup


base_url = "https://green-sas.selleramp.com"
login_url = f"{base_url}/site/login?src="
basic_auth_green_sas = 'Basic c2FzOjNueDI2dDNyZ3UwbWxkOGc='
email = 'a.makaev%2Breactivate%40mobidev.biz'
password = 'Temp@123'



def headers_with_basic_auth(basic_auth):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8,uk;q=0.7',
        'authorization': basic_auth,
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://green-sas.selleramp.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    return headers


def headers_with_basic_auth_for_login(basic_auth):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8,uk;q=0.7',
        'authorization': basic_auth,
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://green-sas.selleramp.com',
        'priority': 'u=0, i',
        'referer': 'https://green-sas.selleramp.com/site/login',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    return headers


def cookies_to_string(cookies):
    cookies_list = [f"{cookie.name}={cookie.value}" for cookie in cookies]
    return '; '.join(cookies_list)


def get_request_with_basic_auth(url, headers, data):
    response = requests.request("GET", url=url, headers=headers, data=data)
    # print(response.text)
    print(response.cookies)
    return response


def post_request_with_basic_auth_and_cookies(url, headers, data, cookies):
    response = requests.request("POST", url=url, headers=headers, data=data, cookies=cookies)
    # print(response.text)
    # print(response.cookies)
    print(response.request.body)
    print(response.text)
    print(response.status_code)
    return response


def get_cookies(response):
    cookies = response.cookies
    return cookies


def extract_csrf_token(html_content):
    pattern = r'<meta\s+name="csrf-token"\s+content="([^"]+)"\s*/?>'
    match = re.search(pattern, html_content, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        return None


def extract_csrf_token_bs(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    csrf_token_meta = soup.find('meta', attrs={'name': 'csrf-token'})
    if csrf_token_meta:
        csrf_token = csrf_token_meta.get('content')
        print(f"CSRF Token: {csrf_token}")
        return csrf_token
    else:
        print("CSRF Token meta tag not found")
        return None


def payload_for_login(csrf_token, email, password, remeber_me_0, remeber_me_1, login_button):
    payload = f"_csrf-sasend={csrf_token}&LoginForm[email]={email}&LoginForm[password]={password}&LoginForm[rememberMe]={remeber_me_0}&LoginForm[rememberMe]={remeber_me_1}&login-button={login_button}"
    return payload.encode()


def get_request_search_product(self):

    pass


login_form = get_request_with_basic_auth(url=login_url, headers=headers_with_basic_auth(basic_auth_green_sas), data={})
csrf_token = extract_csrf_token_bs(login_form.text)
logged_user = post_request_with_basic_auth_and_cookies(url=login_url,
                        headers=headers_with_basic_auth_for_login(basic_auth=basic_auth_green_sas),
                                                       data=payload_for_login(csrf_token=csrf_token,
                                                                              email=email,
                                                                              password=password,
                                                                              remeber_me_0=0,
                                                                              remeber_me_1=1,
                                                                              login_button=''),cookies=get_cookies(login_form))
print(logged_user.headers)

