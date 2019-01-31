"""

"""

import requests
import json

class CoinMarket(object):
    """
    Coin market interaction
    """

    def __init__(self):
        """

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


        :return:
        """

        with open(self.api_key_file, "r") as api_key_file:
            self.api_key = str(api_key_file.read())
            self.api_key = self.api_key.strip()


        return {"X-CMC_PRO_API_KEY": self.api_key}


    def _get_api_path(self, path):
        """

        :param path:
        :return:
        """

        return "https://{host}/{base}/{path}".format(host=self.api_host, base=self.api_base_path, path=path)


    def get_latest_listing(self):
        """


        :return:
        """

        response = requests.get(self._get_api_path(path="listings/latest"), headers=self._headers())

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

                print flat_item