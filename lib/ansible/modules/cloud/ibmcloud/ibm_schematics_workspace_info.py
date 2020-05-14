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
module: ibm_schematics_workspace_info
short_description: Retrieve IBM Cloud 'ibm_schematics_workspace' resource

version_added: "2.9"

description:
    - Retrieve an IBM Cloud 'ibm_schematics_workspace' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.5.2
    - Terraform v0.12.20

options:
    workspace_id:
        description:
            - The id of workspace
        required: True
        type: str
    name:
        description:
            - The name of workspace
        required: False
        type: str
    types:
        description:
            - None
        required: False
        type: list
        elements: str
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    crn:
        description:
            - cloud resource name of the workspace
        required: False
        type: str
    location:
        description:
            - The location of workspace
        required: False
        type: str
    description:
        description:
            - The description of workspace
        required: False
        type: str
    catalog_ref:
        description:
            - Catalog references
        required: False
        type: dict
        elements: dict
    template_id:
        description:
            - The id of templates
        required: False
        type: list
        elements: str
    resource_group:
        description:
            - The resource group of workspace
        required: False
        type: str
    is_locked:
        description:
            - None
        required: False
        type: bool
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this workspace
        required: False
        type: str
    status:
        description:
            - The status of workspace
        required: False
        type: str
    is_frozen:
        description:
            - None
        required: False
        type: bool
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
    ('workspace_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'workspace_id',
    'name',
    'types',
    'tags',
    'crn',
    'location',
    'description',
    'catalog_ref',
    'template_id',
    'resource_group',
    'is_locked',
    'resource_controller_url',
    'status',
    'is_frozen',
]

# define available arguments/parameters a user can pass to the module
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import env_fallback
from ansible.module_utils.ibmcloud_utils.ibmcloud import Terraform, ibmcloud_terraform
module_args = dict(
    workspace_id=dict(
        required=True,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    types=dict(
        required=False,
        elements='',
        type='list'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    crn=dict(
        required=False,
        type='str'),
    location=dict(
        required=False,
        type='str'),
    description=dict(
        required=False,
        type='str'),
    catalog_ref=dict(
        required=False,
        elements='',
        type='dict'),
    template_id=dict(
        required=False,
        elements='',
        type='list'),
    resource_group=dict(
        required=False,
        type='str'),
    is_locked=dict(
        required=False,
        type='bool'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    status=dict(
        required=False,
        type='str'),
    is_frozen=dict(
        required=False,
        type='bool'),
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
        resource_type='ibm_schematics_workspace',
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
