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
module: ibm_pi_network_info
short_description: Retrieve IBM Cloud 'ibm_pi_network' resource

version_added: "2.9"

description:
    - Retrieve an IBM Cloud 'ibm_pi_network' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.5.2
    - Terraform v0.12.20

options:
    cidr:
        description:
            - None
        required: False
        type: str
    available_ip_count:
        description:
            - None
        required: False
        type: float
    used_ip_count:
        description:
            - None
        required: False
        type: float
    used_ip_percent:
        description:
            - None
        required: False
        type: float
    name:
        description:
            - None
        required: False
        type: str
    pi_cloud_instance_id:
        description:
            - None
        required: True
        type: str
    type:
        description:
            - None
        required: False
        type: str
    vlan_id:
        description:
            - None
        required: False
        type: int
    gateway:
        description:
            - None
        required: False
        type: str
    pi_network_name:
        description:
            - Network Name to be used for pvminstances
        required: True
        type: str
    zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environment
              variable 'IC_ZONE'.
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
    ('pi_cloud_instance_id', 'str'),
    ('pi_network_name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'cidr',
    'available_ip_count',
    'used_ip_count',
    'used_ip_percent',
    'name',
    'pi_cloud_instance_id',
    'type',
    'vlan_id',
    'gateway',
    'pi_network_name',
]

# define available arguments/parameters a user can pass to the module
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import env_fallback
from ansible.module_utils.ibmcloud_utils.ibmcloud import Terraform, ibmcloud_terraform
module_args = dict(
    cidr=dict(
        required=False,
        type='str'),
    available_ip_count=dict(
        required=False,
        type='float'),
    used_ip_count=dict(
        required=False,
        type='float'),
    used_ip_percent=dict(
        required=False,
        type='float'),
    name=dict(
        required=False,
        type='str'),
    pi_cloud_instance_id=dict(
        required=True,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    vlan_id=dict(
        required=False,
        type='int'),
    gateway=dict(
        required=False,
        type='str'),
    pi_network_name=dict(
        required=True,
        type='str'),
    zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE'])),
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
        resource_type='ibm_pi_network',
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
