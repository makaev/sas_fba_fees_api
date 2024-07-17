import requests
import json
from selleramp_api_test import Constants
from selleramp_api_test import create_user


class FbaFeeEngine:

    def __init__(self):
        pass

    def get_fba_fees(self, session, api_url, headers, asin, is_dangerous_goods, dimension_uom, weight_uom, weight, width, length, height):
        url = \
            f"{api_url}v2/products/{asin}/fba-fees?" \
            f"is_dangerous_goods={is_dangerous_goods}" \
            f"&dimension_uom={dimension_uom}" \
            f"&weight_uom={weight_uom}" \
            f"&weight={weight}" \
            f"&width={width}" \
            f"&length={length}" \
            f"&height={height}"
        payload = {}
        response = session.get(url=url, headers=headers, data=payload)
        print(f"FBA FeeEngine request url: {url}")
        print(f"FBA FeeEngine response:")
        response_json = response.json()
        print(json.dumps(response_json, sort_keys=True, indent=4))
        return url, response_json


    def get_fba_fees_extended(self, session, api_url, headers, asin, is_dangerous_goods, is_apparel, dimension_uom, weight_uom, weight, width, length, height):
        url = \
            f"{api_url}v2/products/{asin}/fba-fees?" \
            f"is_dangerous_goods={is_dangerous_goods}" \
            f"&dimension_uom={dimension_uom}" \
            f"&weight_uom={weight_uom}" \
            f"&weight={weight}" \
            f"&width={width}" \
            f"&length={length}" \
            f"&height={height}" \
            f"&is_apparel={is_apparel}"
        payload = {}
        response = session.get(url=url, headers=headers, data=payload)
        # print(f"FBA FeeEngine request url: {url}")
        # print(f"FBA FeeEngine response:")
        response_json = response.json()
        # print(json.dumps(response_json, sort_keys=True, indent=4))
        return url, response_json
