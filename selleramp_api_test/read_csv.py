import csv

def read_csv_and_extract_columns(file_path):
    with open(file_path, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            width = row['width']
            height = row['height']
            length = row['length']
            weight = row['weight']
            pick_and_pack_fee = row['pick_and_pack_fee']
            print(f"Width: {width}, Height: {height}, Length: {length}, Weight: {weight}, Pick and Pack Fee: {pick_and_pack_fee}")

# Example usage
# file_path = f'/Users/user/subscription_status_api/fba_fee_engine_repo/sas_fba_fee_engine/profit_calc_data_us.csv'
# read_csv_and_extract_columns(file_path)

print(round(3.5900000000000003,2))