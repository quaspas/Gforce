import collections
import json


def print_response(response):
    response = response.content.decode('utf-8')
    obj = json.loads(response, object_pairs_hook=collections.OrderedDict)
    print(json.dumps(obj, indent=4, ensure_ascii=False))