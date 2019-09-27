import json
from faker import Faker
import uuid

import magento_api_wrapper as magento_api
import constants
import json_data

# faker for random naming of attribute
faker = Faker()

# get auth token first
token = magento_api.getAuthToken()

# creating attributes set
for atr_set_index in range(0, 50):

    # update attributes
    attribute_set_json = json_data.attribute_set
    attribute_set_json['attributeSet']['attribute_set_name'] = 'Testable API AttributeSet -' + uuid.uuid4().hex[:6].upper() + \
        str(atr_set_index)

    # post data
    attribute_set_response = magento_api.postData(
        constants.CREATE_ATTRIBUTESET_URL, json.dumps(attribute_set_json), token)

    attribute_set_response = json.loads(attribute_set_response)
    attribute_set_id = attribute_set_response['attribute_set_id']
    # Create attribute group
    for atr_group_index in range(0, 2):

        # update attributes
        attribute_group_json = json_data.attribute_group
        attribute_group_json['group']['attribute_group_name'] = faker.name(
        ) + 'API' + str(atr_group_index)
        attribute_group_json['group']['attribute_set_id'] = attribute_set_id
        attribute_group_json['group']['extension_attributes']['attribute_group_code'] = "test2_api_" + uuid.uuid4().hex[:6].upper() + \
            str(atr_group_index)

        # post group data
        attribute_group_response = magento_api.postData(
            constants.CREATE_ATTRIBUTE_GROUP_URL, json.dumps(attribute_group_json), token)
        attribute_group_response = json.loads(attribute_group_response)
        attribute_group_id = attribute_group_response['attribute_group_id']

        # create attributes
        for atr_index in range(0, 100):

            # update attribute
            attribute_json = json_data.attribute
            attribute_json['attribute']['default_frontend_label'] = attribute_json[
                'attribute']['default_frontend_label'] + uuid.uuid4().hex[:6].upper() + str(atr_index)
            attribute_json['attribute']['attribute_code'] = "api_atr_" + uuid.uuid4().hex[:6].lower() + \
                str(atr_index)
            attribute_json['attribute']['default_frontend_label'] = "API Attribute - " + uuid.uuid4().hex[:6].upper() + \
                str(atr_index)
            attribute_json['attribute']['default_value'] = "Default Value -" + uuid.uuid4().hex[:6].upper() + \
                str(atr_index)

            # post data
            attribute_response = magento_api.postData(
                constants.CREATE_ATTRIBUTE_URL, json.dumps(attribute_json), token)
            attribute_response = json.loads(attribute_response)
            attribute_id = attribute_response['attribute_id']
            attribute_code = attribute_response['attribute_code']

            # assign attribute to attribute set and group
            map_attribute_json = json_data.map_attribute
            map_attribute_json['attributeSetId'] = attribute_set_id
            map_attribute_json['attributeGroupId'] = attribute_group_id
            map_attribute_json['attributeCode'] = attribute_code

            # post data
            map_attribute_response = magento_api.postData(
                constants.MAP_ATTRIBUTE_TO_ATTR_SET, json.dumps(map_attribute_json), token)

print("Attributes created successfully.")
