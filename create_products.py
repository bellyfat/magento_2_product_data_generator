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
for product_index in range(0, 5000):
    simple_product_json = json_data.product
    product_sku = uuid.uuid4().hex[:6].lower()
    product_name = 'API Test Product - ' + \
        str(random.randint(1000, 99999)) + str(product_index)
    simple_product_json['product']['attribute_set_id'] = 56
    simple_product_json['sku'] = product_sku
    simple_product_json['product']['sku'] = product_sku
    simple_product_json['product']['name'] = product_name
    simple_product_json['product']

    # post product data
    response = magento_api.postData(
        constants.CREATE_PRODUCT_URL, json.dumps(simple_product_json), token)


end_time = time.now()
print(end_time - start_time)
