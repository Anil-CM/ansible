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
module: ibm_lbaas_info
short_description: Retrieve IBM Cloud 'ibm_lbaas' resource

version_added: "2.9"

description:
    - Retrieve an IBM Cloud 'ibm_lbaas' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.5.2
    - Terraform v0.12.20

options:
    status:
        description:
            - None
        required: False
        type: str
    ssl_ciphers:
        description:
            - None
        required: False
        type: list
        elements: str
    health_monitors:
        description:
            - None
        required: False
        type: list
        elements: dict
    name:
        description:
            - None
        required: True
        type: str
    description:
        description:
            - None
        required: False
        type: str
    type:
        description:
            - None
        required: False
        type: str
    server_instances:
        description:
            - None
        required: False
        type: list
        elements: dict
    server_instances_up:
        description:
            - None
        required: False
        type: int
    active_connections:
        description:
            - None
        required: False
        type: int
    use_system_public_ip_pool:
        description:
            - None
        required: False
        type: bool
    protocols:
        description:
            - None
        required: False
        type: list
        elements: dict
    datacenter:
        description:
            - None
        required: False
        type: str
    vip:
        description:
            - None
        required: False
        type: str
    server_instances_down:
        description:
            - None
        required: False
        type: int
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
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'status',
    'ssl_ciphers',
    'health_monitors',
    'name',
    'description',
    'type',
    'server_instances',
    'server_instances_up',
    'active_connections',
    'use_system_public_ip_pool',
    'protocols',
    'datacenter',
    'vip',
    'server_instances_down',
]

# define available arguments/parameters a user can pass to the module
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import env_fallback
from ansible.module_utils.ibmcloud_utils.ibmcloud import Terraform, ibmcloud_terraform
module_args = dict(
    status=dict(
        required=False,
        type='str'),
    ssl_ciphers=dict(
        required=False,
        elements='',
        type='list'),
    health_monitors=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=True,
        type='str'),
    description=dict(
        required=False,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    server_instances=dict(
        required=False,
        elements='',
        type='list'),
    server_instances_up=dict(
        required=False,
        type='int'),
    active_connections=dict(
        required=False,
        type='int'),
    use_system_public_ip_pool=dict(
        required=False,
        type='bool'),
    protocols=dict(
        required=False,
        elements='',
        type='list'),
    datacenter=dict(
        required=False,
        type='str'),
    vip=dict(
        required=False,
        type='str'),
    server_instances_down=dict(
        required=False,
        type='int'),
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

    result = ibmcloud_terraform(
        resource_type='ibm_lbaas',
        tf_type='data',
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
