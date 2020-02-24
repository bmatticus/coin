"""
Coin Market Interation Class
"""

import requests
import datetime

class CoinMarket(object):
    """
    Coin market interaction
    """

    def __init__(self):
        """
        Initialize instance of CoinMarket class. Set API host/ETC
        """

        self.api_host = "pro-api.coinmarketcap.com"
        self.api_base_path = "v1/cryptocurrency"
        self.api_key_file = "api_key"
        self.fields_of_interest = [
            "circulating_supply",
            "name",
            "quote:USD:price",
            "symbol",
            "total_supply"
        ]

    def _headers(self):
        """
        Private method, _ prefix, to define the headers for requests to CoinMarket


        :return: Header dictionary
        """

        with open(self.api_key_file, "r") as api_key_file:
            self.api_key = str(api_key_file.read())
            self.api_key = self.api_key.strip()


        return {"X-CMC_PRO_API_KEY": self.api_key}


    def _get_api_path(self, path):
        """
        Private mathod to generate API path for CoinMarket based on target endpoint.

        :param path: Target endpoint path
        :return: Full API path
        """

        return "https://{host}/{base}/{path}".format(host=self.api_host, base=self.api_base_path, path=path)


    def get_latest_listing(self):
        """
        Retrieves latest listings for coins

        :return: List of dictionary objects containin coin data
        """

        response = requests.get(self._get_api_path(path="listings/latest"), headers=self._headers())

        items = []
        if response is not None and "data" in response.json():
            for item in response.json()["data"]:
                flat_item = {}
                for field in self.fields_of_interest:
                    field_path = field.split(':')
                    value = item

                    for cur_path in field_path:
                        if cur_path in value:
                            value = value[cur_path]
                        else:
                            value = {}

                    flat_item[field] = value


                flat_item['timestamp'] = datetime.datetime.now().isoformat()
                items.append(flat_item)

        return items
