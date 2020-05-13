#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_api_gateway_endpoint
short_description: Configure IBM Cloud 'ibm_api_gateway_endpoint' resource

version_added: "2.9"

description:
    - Create, update or destroy an IBM Cloud 'ibm_api_gateway_endpoint' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.5.2
    - Terraform v0.12.20

options:
    name:
        description:
            - (Required for new resource) Endpoint name
        required: False
        type: str
    managed:
        description:
            - Managed indicates if endpoint is online or offline.
        required: False
        type: bool
        default: False
    provider_id:
        description:
            - Provider ID of an endpoint allowable values user-defined and whisk
        required: False
        type: str
        default: user-defined
    type:
        description:
            - Action type of Endpoint ALoowable values are share, unshare, manage, unmanage
        required: False
        type: str
        default: unshare
    service_instance_crn:
        description:
            - (Required for new resource) Api Gateway Service Instance Crn
        required: False
        type: str
    open_api_doc_name:
        description:
            - (Required for new resource) Json File path
        required: False
        type: str
    routes:
        description:
            - Invokable routes for an endpoint
        required: False
        type: list
        elements: str
    shared:
        description:
            - The Shared status of an endpoint
        required: False
        type: bool
    base_path:
        description:
            - Base path of an endpoint
        required: False
        type: str
    endpoint_id:
        description:
            - Endpoint ID
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
        type: str
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
        type: str
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
        type: str
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('name', 'str'),
    ('service_instance_crn', 'str'),
    ('open_api_doc_name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'name',
    'managed',
    'provider_id',
    'type',
    'service_instance_crn',
    'open_api_doc_name',
    'routes',
    'shared',
    'base_path',
    'endpoint_id',
]

# define available arguments/parameters a user can pass to the module
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import env_fallback
from ansible.module_utils.ibmcloud_utils.ibmcloud import Terraform, ibmcloud_terraform
module_args = dict(
    name=dict(
        required=False,
        type='str'),
    managed=dict(
        default=False,
        type='bool'),
    provider_id=dict(
        default='user-defined',
        type='str'),
    type=dict(
        default='unshare',
        type='str'),
    service_instance_crn=dict(
        required=False,
        type='str'),
    open_api_doc_name=dict(
        required=False,
        type='str'),
    routes=dict(
        required=False,
        elements='',
        type='list'),
    shared=dict(
        required=False,
        type='bool'),
    base_path=dict(
        required=False,
        type='str'),
    endpoint_id=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud_terraform(
        resource_type='ibm_api_gateway_endpoint',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.5.2',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
