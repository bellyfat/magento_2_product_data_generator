import json
import uuid

import magento_api_wrapper as magento_api
import constants
import json_data

# faker for random naming of attribute


# get auth token first
token = magento_api.getAuthToken()

# Create Base Categories
for base_cat_index in range(0, 1):

    parent_category_json = json_data.category
    parent_category_json['category']['name'] = "Base Category - " + \
        uuid.uuid4().hex[:6].lower() + str(base_cat_index)

    # post data
    parent_cat_response = magento_api.postData(
        constants.CREATE_CATEGORY_URL, json.dumps(parent_category_json), token)

    parent_cat_response = json.loads(parent_cat_response)
    parent_cat_id = parent_cat_response['id']

    for l1_cat_index in range(0, 2):

        l1_category_json = json_data.category
        l1_category_json['category']['name'] = "Child 1 Category - " + \
            uuid.uuid4().hex[:6].lower() + str(l1_cat_index)
        l1_category_json['category']['parent_id'] = parent_cat_id

        # post data
        l1_cat_response = magento_api.postData(
            constants.CREATE_CATEGORY_URL, json.dumps(l1_category_json), token)

        l1_cat_response = json.loads(l1_cat_response)
        l1_cat_id = l1_cat_response['id']

        for l2_cat_index in range(0, 3):

            l2_category_json = json_data.category
            l2_category_json['category']['name'] = "Child 2 Category - " + \
                uuid.uuid4().hex[:6].lower() + str(l2_cat_index)
            l2_category_json['category']['parent_id'] = l1_cat_id

            # post data
            l2_cat_response = magento_api.postData(
                constants.CREATE_CATEGORY_URL, json.dumps(l2_category_json), token)
print("Categories created successfully.")
