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
module: ibm_certificate_manager_order
short_description: Configure IBM Cloud 'ibm_certificate_manager_order' resource

version_added: "2.9"

description:
    - Create, update or destroy an IBM Cloud 'ibm_certificate_manager_order' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.5.2
    - Terraform v0.12.20

options:
    has_previous:
        description:
            - Has Previous
        required: False
        type: str
    certificate_manager_instance_id:
        description:
            - (Required for new resource) Certificate manager instance ID
        required: False
        type: str
    domain_validation_method:
        description:
            - Domain validation methods
        required: False
        type: str
        default: dns - 01
    issuer:
        description:
            - Certificate issuer info
        required: False
        type: str
    key_algorithm:
        description:
            - Keyalgorithm info
        required: False
        type: str
    imported:
        description:
            - set to true if certificate is imported
        required: False
        type: bool
    domains:
        description:
            - (Required for new resource) List of domain names
        required: False
        type: list
        elements: str
    rotate_keys:
        description:
            - Keys are sorated if set to true
        required: False
        type: bool
        default: False
    dns_provider_instance_crn:
        description:
            - DNS provider instance CRN
        required: False
        type: str
    algorithm:
        description:
            - Algorithm info
        required: False
        type: str
    name:
        description:
            - (Required for new resource) Certificate name
        required: False
        type: str
    status:
        description:
            - Status  of the certificate
        required: False
        type: str
    description:
        description:
            - Certicate description
        required: False
        type: str
    begins_on:
        description:
            - Cerificate validity from date
        required: False
        type: int
    expires_on:
        description:
            - Certificaet expairy date
        required: False
        type: int
    issuance_info:
        description:
            - None
        required: False
        type: dict
        elements: dict
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
    ('certificate_manager_instance_id', 'str'),
    ('domains', 'list'),
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'has_previous',
    'certificate_manager_instance_id',
    'domain_validation_method',
    'issuer',
    'key_algorithm',
    'imported',
    'domains',
    'rotate_keys',
    'dns_provider_instance_crn',
    'algorithm',
    'name',
    'status',
    'description',
    'begins_on',
    'expires_on',
    'issuance_info',
]

# define available arguments/parameters a user can pass to the module
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import env_fallback
from ansible.module_utils.ibmcloud_utils.ibmcloud import Terraform, ibmcloud_terraform
module_args = dict(
    has_previous=dict(
        required=False,
        type='str'),
    certificate_manager_instance_id=dict(
        required=False,
        type='str'),
    domain_validation_method=dict(
        default='dns - 01',
        type='str'),
    issuer=dict(
        required=False,
        type='str'),
    key_algorithm=dict(
        required=False,
        type='str'),
    imported=dict(
        required=False,
        type='bool'),
    domains=dict(
        required=False,
        elements='',
        type='list'),
    rotate_keys=dict(
        default=False,
        type='bool'),
    dns_provider_instance_crn=dict(
        required=False,
        type='str'),
    algorithm=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    status=dict(
        required=False,
        type='str'),
    description=dict(
        required=False,
        type='str'),
    begins_on=dict(
        required=False,
        type='int'),
    expires_on=dict(
        required=False,
        type='int'),
    issuance_info=dict(
        required=False,
        elements='',
        type='dict'),
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
        resource_type='ibm_certificate_manager_order',
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
