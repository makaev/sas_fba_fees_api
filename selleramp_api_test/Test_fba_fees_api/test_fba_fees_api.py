import pytest
from repo_for_api_tests.sas_fba_fees_api.selleramp_api_test import helpers, Constants
import csv


@pytest.mark.usefixtures("fixture_class_instance_for_user")
@pytest.mark.usefixtures("fixture_class_instance_for_fee_engine")

class Test_fba_fees_api:

    path_to_folder = '/fba_fee_engine_repo/sas_fba_fee_engine/'
    file_path_post = f'/fba_fee_engine_repo/sas_fba_fee_engine/feeEngine_input_data.csv'
    file_path_sipp = f'{path_to_folder}post_data_sipp.json'
    file_path_expected_data = '/fba_fee_engine_repo/sas_fba_fee_engine/expected_sipp.json'
    file_path_sipp_bat = f'{path_to_folder}post_data_sipp_bat.json'
    file_path_expected_data_sipp_bat = f'{path_to_folder}expected_sipp_bat.json'
    file_path_dangerous = f'{path_to_folder}post_data_dangerous.json'
    file_path_expected_dangerous = f'{path_to_folder}expected_dangerous.json'
    output_csv_file_path = f'{path_to_folder}report_fee_engine.csv'
    output_csv_file_path_csv = f'{path_to_folder}selleramp_api_test/report_fee_engine_failed.csv'



    def test_user_class_instance(self):
        print(self.user_cls.__dict__)
        print(self.fee_engine_cls.__dict__)


    def test_login(self):
        user = self.user_cls
        logged_user, session = user.login_user()
        self.user_cls.logged_user = logged_user
        self.user_cls.session = session
        assert logged_user.status_code == 200


    def test_check_fba_fees_and_compare(self):
        sorted_passed_results = []
        sorted_failed_results = []
        with open(self.file_path_post, newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                dimension_unit = 'cm'
                weight_unit = 'kg'
                asin = row['asin']
                width = helpers.inches_to_cm(float(row['width']))
                height = helpers.inches_to_cm(float(row['height']))
                length = helpers.inches_to_cm(float(row['length']))
                weight = helpers.pounds_to_kg(float(row['weight']))
                expected_fba_fee = row['expected_fba']
                is_apparel = row['is_apparel']
                is_dangerous = row['is_dangerous']
                has_batteries = row['has_batteries']

                url, response = self.fee_engine_cls.get_fba_fees_extended(
                        headers=Constants.Headers("", "", "").headers_for_fee_engine_api(
                        authorization=Constants.Constants.BASIC_AUTH_GREEN_SANDBOX,
                        x_uid=Constants.Constants.X_UID,
                        x_api_token=Constants.Constants.X_API_TOKEN),
                    session=self.user_cls.session,
                    api_url=Constants.EndpointsConstants.FEE_ENGINE_API_URL,
                    asin=asin,
                    is_dangerous_goods=is_dangerous,
                    dimension_uom=str(dimension_unit),
                    weight_uom=str(weight_unit),
                    weight=weight,
                    width=width,
                    length=length,
                    height=height,
                    is_apparel=is_apparel)
                fba_fee_engine = response['shipping_fees']['domestic_fees']['estimated_fba_fee_normal']
                if int(has_batteries) == 1:
                    fba_fee_engine = fba_fee_engine + 0.11
                res_message = f"Width: {width}, Height: {height}, Length: {length}, Weight: {weight}, " \
                              f"Dimension_unit: {dimension_unit}, Weight_unit: {weight_unit}, " \
                              f"Pick and Pack Fee: {expected_fba_fee}, FbaFee: {fba_fee_engine}, has batteries: {has_batteries}"
                if float(fba_fee_engine) == float(expected_fba_fee):
                    sorted_passed_results.append(res_message)
                else:
                    sorted_failed_results.append(res_message)
                    print(res_message)
                    csv_row = [asin, width, height, length, weight, dimension_unit, weight_unit, expected_fba_fee, fba_fee_engine, url]
                    with open(self.output_csv_file_path_csv, mode='a', newline='', encoding='utf-8') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerow(csv_row)
            assert sorted_failed_results == []

