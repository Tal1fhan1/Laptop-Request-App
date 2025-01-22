import os
import requests

from dotenv import find_dotenv, load_dotenv


def get_items(url):
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    userId = os.getenv('USER_ID')
    password = os.getenv('PASSWORD')
    try:
        response = requests.get(url, auth=(
            userId, password))

        if response.status_code == 200:
            items = response.json()
            return items
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def main(barcode):

    url2 = f'https://africadatacentres.assetspire.cloud/en-us/assets/asset?asset_id={barcode}'

    items = get_items(url2)

    if items:
        if items['count'] >= 1:
            for i in range(len(items['results'])):
                if 'asset_description' in items['results'][i]:
                    if items['results'][i]['asset_description'] == 'Laptop':
                        if 'assigned_to_user' in items['results'][i]:
                            return 'This laptop belongs to: ' + items['results'][i]['assigned_to_user']
                        else:
                            return 'This laptop has not been assigned to a user yet. Please try again later'
                    else:
                        return 'The Asset ID you provided is not associated with a laptop. Please try a different Asset ID.'
        else:

            return 'The Asset ID you provided does not exist. Please try a different Asset ID.'
    else:
        return 'The API Request has failed. Please try again.'


if __name__ == '__main__':
    main()
