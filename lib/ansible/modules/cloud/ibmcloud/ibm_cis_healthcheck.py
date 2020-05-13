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
module: ibm_cis_healthcheck
short_description: Configure IBM Cloud 'ibm_cis_healthcheck' resource

version_added: "2.9"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cis_healthcheck' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.5.2
    - Terraform v0.12.20

options:
    path:
        description:
            - path
        required: False
        type: str
    timeout:
        description:
            - timeout
        required: False
        type: int
        default: 5
    cis_id:
        description:
            - (Required for new resource) CIS instance crn
        required: False
        type: str
    allow_insecure:
        description:
            - allow_insecure
        required: False
        type: bool
        default: False
    created_on:
        description:
            - None
        required: False
        type: str
    retries:
        description:
            - retries
        required: False
        type: int
        default: 2
    interval:
        description:
            - interval
        required: False
        type: int
        default: 60
    follow_redirects:
        description:
            - follow_redirects
        required: False
        type: bool
    port:
        description:
            - None
        required: False
        type: int
    description:
        description:
            - description
        required: False
        type: str
    expected_codes:
        description:
            - expected_codes
        required: False
        type: str
    type:
        description:
            - type
        required: False
        type: str
        default: http
    method:
        description:
            - method
        required: False
        type: str
    modified_on:
        description:
            - None
        required: False
        type: str
    expected_body:
        description:
            - expected_body
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
    ('cis_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'path',
    'timeout',
    'cis_id',
    'allow_insecure',
    'created_on',
    'retries',
    'interval',
    'follow_redirects',
    'port',
    'description',
    'expected_codes',
    'type',
    'method',
    'modified_on',
    'expected_body',
]

# define available arguments/parameters a user can pass to the module
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import env_fallback
from ansible.module_utils.ibmcloud_utils.ibmcloud import Terraform, ibmcloud_terraform
module_args = dict(
    path=dict(
        required=False,
        type='str'),
    timeout=dict(
        default=5,
        type='int'),
    cis_id=dict(
        required=False,
        type='str'),
    allow_insecure=dict(
        default=False,
        type='bool'),
    created_on=dict(
        required=False,
        type='str'),
    retries=dict(
        default=2,
        type='int'),
    interval=dict(
        default=60,
        type='int'),
    follow_redirects=dict(
        required=False,
        type='bool'),
    port=dict(
        required=False,
        type='int'),
    description=dict(
        required=False,
        type='str'),
    expected_codes=dict(
        required=False,
        type='str'),
    type=dict(
        default='http',
        type='str'),
    method=dict(
        required=False,
        type='str'),
    modified_on=dict(
        required=False,
        type='str'),
    expected_body=dict(
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
        resource_type='ibm_cis_healthcheck',
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
