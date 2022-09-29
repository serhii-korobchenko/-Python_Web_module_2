import requests
import xmltodict


class RequestConnection:
    def __init__(self, request):
        self.request = request

    def get_data_from_url(self, url):
        return self.request.get(url)


class ApiClient:
    def __init__(self, fetch):
        self.fetch = fetch

    def get_xml(self, url):
        response = self.fetch.get_data_from_url(url)
        return response.text


def xml_dict_adapter(xml):
    obj = xmltodict.parse(xml)
    convert_json = dict(obj)
    return convert_json


def parse_course(data):
    course = None
    exchangerates = data.get("exchangerates", None)
    if exchangerates:
        course = exchangerates.get("@BaseCurrency", 0)
    return course


api_client = ApiClient(RequestConnection(requests))

data_xml = api_client.get_xml(
    "https://api.privatbank.ua/p24api/exchange_rates?date=12.12.2020"
)
course = parse_course(xml_dict_adapter(data_xml))
print(course)