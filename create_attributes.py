import json
import ast
from faker import Faker
import magento_api_wrapper as magento_api
import constants
import json_data

# faker for random naming of attribute
faker = Faker()

# get auth token first
token = magento_api.getAuthToken()
print(token)

# creating attributes set
for atr_set_index in range(0, 5):
    attribute_set_json = json_data.attribute_set
    attribute_set_json['attributeSet']['attribute_set_name'] = faker.name() + 'API' + \
        str(atr_set_index)
    attribute_set_response = magento_api.postData(
        constants.CREATE_ATTRIBUTESET_URL, json.dumps(attribute_set_json), token)
    attribute_set_response = ast.literal_eval(attribute_set_response)
    attribute_set_id = attribute_set_response['attribute_set_id']
    # Create attribute group
    for atr_group_index in range(0, 5):
        attribute_group_json = json_data.attribute_group
        attribute_group_json['group']['attribute_group_name'] = faker.name(
        ) + 'API' + str(atr_group_index)
        attribute_group_json['group']['attribute_set_id'] = attribute_set_id
        attribute_group_json['extension_attributes']['attribute_group_code'] = "test_api_" + \
            str(atr_group_index)
        attribute_group_response = magento_api.postData(
            constants.CREATE_ATTRIBUTE_GROUP_URL, json.dumps(attribute_group_json), token)
        attribute_group_response = ast.literal_eval(attribute_group_json)
        attribute_group_id = attribute_group_response['attribute_group_id']

        # create attributes
        for atr_index in range(0, 5):
            attribute_json = json_data.attribute
