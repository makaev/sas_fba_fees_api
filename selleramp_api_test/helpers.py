from repo_for_api_tests.sas_fba_fees_api.selleramp_api_test import Constants
import re
import json
import csv
from bs4 import BeautifulSoup


def make_headers(authorization, referer, user_agent):
    headers_instance = Constants.Headers(authorization, referer, user_agent)
    headers = headers_instance.headers_with_basic_auth(authorization=authorization,
                                                       referer=referer,
                                                       user_agent=user_agent)
    return headers


def headers_content_type():
    headers = make_headers(authorization=Constants.Constants.BASIC_AUTH_GREEN_SANDBOX,
                           referer=Constants.Constants.REFERER_GREEN_SANDBOX,
                           user_agent=Constants.Constants.USER_AGENT)
    headers['content-type'] = 'application/x-www-form-urlencoded'
    return headers


def headers_content_type_with_auth(cookie):
    headers = make_headers(authorization=Constants.Constants.BASIC_AUTH_GREEN_SANDBOX,
                           referer=Constants.Constants.REFERER_GREEN_SANDBOX,
                           user_agent=Constants.Constants.USER_AGENT)
    headers['content-type'] = 'application/x-www-form-urlencoded'
    headers['Cookie'] = cookie
    return headers


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def read_csv_and_extract_columns(file_path):
    with open(file_path, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        return csvreader


def extract_data_and_compare(file_path, output_csv_file_path, response, asin, is_dangerous):
    failed = []
    passed = []
    data = read_json_file(file_path)
    with open(output_csv_file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        # csvwriter.writerow(['ASIN', 'Status', 'Expected Value', 'Received Value', 'Message'])
        if is_dangerous == False:
            for fees in data:
                if fees['asin'] == asin:
                    fba_fee_expected = fees['feeAmount_base']
                    sipp_discount_expected = fees['feeAmount_discount']
                    feeAmount_total_expected = fba_fee_expected + (sipp_discount_expected)
                    # print(round(feeAmount_total_expected, 2))
                    estimated_fba_fee_normal = response['shipping_fees']['domestic_fees']['estimated_fba_fee_normal']
                    if fba_fee_expected == round(estimated_fba_fee_normal, 2):
                        message = f" ----- Success. Test for ASIN: {asin} passed. Expected value {fba_fee_expected} == " \
                                  f"received value {estimated_fba_fee_normal} "
                        print(message)
                        csvwriter.writerow([asin, 'Success', fba_fee_expected, estimated_fba_fee_normal, message])
                        passed.append(message)
                    elif fba_fee_expected != round(estimated_fba_fee_normal, 2):
                        message = f"------ Warning. Test for ASIN: {asin} failed. Expected value {fba_fee_expected} != " \
                                  f"received value {estimated_fba_fee_normal} "
                        print(message)
                        failed.append(message)
                        csvwriter.writerow([asin, 'Success', fba_fee_expected, estimated_fba_fee_normal, message])


        if is_dangerous:
            for fees in data:
                if fees['asin'] == asin:
                    fba_fee_expected = fees['feeAmount_base']
                    estimated_fba_fee_normal = response['shipping_fees']['domestic_fees']['estimated_fba_fee_normal']
                    if fba_fee_expected == round(estimated_fba_fee_normal, 2):
                        message = f" ----- Success. Test for DG ASIN: {asin} passed. Expected value {fba_fee_expected}" \
                                  f" == received value {estimated_fba_fee_normal} "
                        print(message)
                        csvwriter.writerow([asin, 'Success', fba_fee_expected, estimated_fba_fee_normal, message])
                        passed.append(message)
                    elif fba_fee_expected != round(estimated_fba_fee_normal, 2):
                        message = f"------ Warning. Test for DG ASIN: {asin} failed. Expected value {fba_fee_expected} " \
                                  f"!= received value {estimated_fba_fee_normal} "
                        print(message)
                        csvwriter.writerow([asin, 'Success', fba_fee_expected, estimated_fba_fee_normal, message])
                        failed.append(message)
    return failed, passed


def cookies_to_string(cookies):
    cookies_list = [f"{cookie.name}={cookie.value}" for cookie in cookies]
    return '; '.join(cookies_list)


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


def extract_identity_sasend_value(text):
    match = re.search(r"_identity-sasend=([^;]+)", text)
    if match:
        extracted_value = match.group(0)
        return extracted_value
    else:
        return 'Not found'


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


def make_cookie_string_with_wukn_and_id_sasend(wukn, identity_sasend):
    return f"wukn={wukn}; _identity-sasend={identity_sasend}"


def payload_for_login(csrf_token, email, password, remeber_me_0, remeber_me_1, login_button):
    payload = f"_csrf-sasend={csrf_token}&" \
              f"LoginForm[email]={email}&" \
              f"LoginForm[password]={password}&" \
              f"LoginForm[rememberMe]={remeber_me_0}&" \
              f"LoginForm[rememberMe]={remeber_me_1}&" \
              f"login-button={login_button}"
    return payload.encode()


def all_lists_empty(lists):
    for lst in lists:
        if len(lst) != 0:
            return lists
    return True


def cm_toInches(cm):
    res = cm / 2.54
    print (f"Size inches is: {res}")
    return res


def inches_to_cm(inches):
    return inches * 2.54


def ounces_to_kg(ounces):
    return ounces * 0.0283495


def pounds_to_kg(pounds):
    kilograms = pounds * 0.45359237
    return kilograms