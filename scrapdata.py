from typing import Tuple, List, Any, Dict

import requests
from bs4 import BeautifulSoup
import json


class GetCash:
    def __init__(self):
        self.url = "https://minfin.com.ua/ua/currency/"
        # self.connection = sqlite3.connect('C:\\Users\\Vova\\Desktop\\taskyukon\\db.sqlite3')
        # self.cursor = self.connection.cursor()

    def get_data(self) -> Tuple[List[Any], List[Any]]:
        '''
        Get html from web-site and retrive to list keys and list values
        :return lists keys and values in tuple:
        '''
        type_cash = []
        value_cash = []
        web_page = requests.get(self.url).text
        doc = BeautifulSoup(web_page, "html.parser")
        table_values = doc.find(class_='table-response mfm-table mfcur-table-lg mfcur-table-lg-currency has-no-tfoot')
        trs = table_values.find_all('tr')
        for tr in trs[1:]:
            type_cash.append(tr.find('td', attrs={'class': 'mfcur-table-cur'}).find('a').text)
            value_cash.append(tr.find('td', attrs={'data-title': 'НБУ'})
                              .find('span', {'class': 'mfcur-nbu-full-wrap'}).text)
        return type_cash, value_cash

    def convert_data_to_dict(self, tuple_keys_and_values: Tuple[List[Any], List[Any]]) -> Dict:
        '''
        Convert lists to dictionary
        :param tuple_keys_and_values:
        :return dict:
        '''
        json_data = {}
        for key, value in zip(tuple_keys_and_values[0], tuple_keys_and_values[1]):
            json_data[key] = value[:len(value) - 2].strip()
        json_data["UAH"] = '1'
        return json_data

    def convert_data_to_json(self, dictionary_data: Dict) -> json:
        """
        Convert dict to json
        :param dictionary_data:
        :return json:
        """
        converted_data = json.dumps(dictionary_data)
        return converted_data


a = GetCash()
two_lists = a.get_data()
dict_conv = a.convert_data_to_dict(two_lists)
json_conv = a.convert_data_to_json(dict_conv)
print(json_conv)
