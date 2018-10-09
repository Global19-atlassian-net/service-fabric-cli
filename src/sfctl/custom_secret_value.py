# -----------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -----------------------------------------------------------------------------

"""Commands related to Service Fabric Mesh secret value commands and operations"""

def get_secret_value(client, secret_resource_name, secret_value_resource_name, show_value):
    secret_data = client.get(secret_resource_name, secret_value_resource_name)
    if show_value:
        secret_value = client.show(secret_resource_name, secret_value_resource_name)
        secret_data.value = secret_value['value']
    return secret_data

