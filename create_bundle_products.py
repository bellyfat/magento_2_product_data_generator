import json
import uuid
import random
from datetime import datetime as time
import magento_api_wrapper as magento_api
import constants
import json_data

# get auth token first
token = magento_api.getAuthToken()
start_time = time.now()
# create simple products first
for bundle_product_index in range(0, 5000):
    simple_product_json = json_data.product
    first_product_sku = uuid.uuid4().hex[:6].lower()
    product_name = 'API Test Product - ' + \
        str(random.randint(1000, 99999)) + str(bundle_product_index)
    simple_product_json['product']['attribute_set_id'] = 56
    simple_product_json['sku'] = first_product_sku
    simple_product_json['product']['sku'] = first_product_sku
    simple_product_json['product']['name'] = product_name
    simple_product_json['product']

    # post product data
    first_simple_product = magento_api.postData(
        constants.CREATE_PRODUCT_URL, json.dumps(simple_product_json), token)

    simple_product_json = json_data.product
    second_product_sku = uuid.uuid4().hex[:6].lower()
    product_name = 'API Test Product - ' + \
        str(random.randint(1000, 99999)) + str(bundle_product_index)
    simple_product_json['product']['attribute_set_id'] = 56
    simple_product_json['sku'] = second_product_sku
    simple_product_json['product']['sku'] = second_product_sku
    simple_product_json['product']['name'] = product_name
    simple_product_json['product']

    # post product data
    second_simple_product = magento_api.postData(
        constants.CREATE_PRODUCT_URL, json.dumps(simple_product_json), token)

    # bundle product creation logic
    bundle_product_json = json_data.bundle_product
    bundle_product_json['product']['sku'] = uuid.uuid4().hex[:6].lower()
    bundle_product_json['product']['name'] = 'Bundle Product - ' + \
        str(bundle_product_index)

    bundle_product_json['product']['extension_attributes']['bundle_product_options'][0]['product_links'][0]['sku'] = first_product_sku
    bundle_product_json['product']['extension_attributes']['bundle_product_options'][0]['product_links'][1]['sku'] = second_product_sku

    # post bundle product data
    bundle_product = magento_api.postData(
        constants.CREATE_PRODUCT_URL, json.dumps(bundle_product_json), token)

end_time = time.now()
print(end_time - start_time)
