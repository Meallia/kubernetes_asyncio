# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.26.9
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.resource_v1alpha1_api import ResourceV1alpha1Api  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestResourceV1alpha1Api(unittest.TestCase):
    """ResourceV1alpha1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.resource_v1alpha1_api.ResourceV1alpha1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_namespaced_pod_scheduling(self):
        """Test case for create_namespaced_pod_scheduling

        """
        pass

    def test_create_namespaced_resource_claim(self):
        """Test case for create_namespaced_resource_claim

        """
        pass

    def test_create_namespaced_resource_claim_template(self):
        """Test case for create_namespaced_resource_claim_template

        """
        pass

    def test_create_resource_class(self):
        """Test case for create_resource_class

        """
        pass

    def test_delete_collection_namespaced_pod_scheduling(self):
        """Test case for delete_collection_namespaced_pod_scheduling

        """
        pass

    def test_delete_collection_namespaced_resource_claim(self):
        """Test case for delete_collection_namespaced_resource_claim

        """
        pass

    def test_delete_collection_namespaced_resource_claim_template(self):
        """Test case for delete_collection_namespaced_resource_claim_template

        """
        pass

    def test_delete_collection_resource_class(self):
        """Test case for delete_collection_resource_class

        """
        pass

    def test_delete_namespaced_pod_scheduling(self):
        """Test case for delete_namespaced_pod_scheduling

        """
        pass

    def test_delete_namespaced_resource_claim(self):
        """Test case for delete_namespaced_resource_claim

        """
        pass

    def test_delete_namespaced_resource_claim_template(self):
        """Test case for delete_namespaced_resource_claim_template

        """
        pass

    def test_delete_resource_class(self):
        """Test case for delete_resource_class

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_namespaced_pod_scheduling(self):
        """Test case for list_namespaced_pod_scheduling

        """
        pass

    def test_list_namespaced_resource_claim(self):
        """Test case for list_namespaced_resource_claim

        """
        pass

    def test_list_namespaced_resource_claim_template(self):
        """Test case for list_namespaced_resource_claim_template

        """
        pass

    def test_list_pod_scheduling_for_all_namespaces(self):
        """Test case for list_pod_scheduling_for_all_namespaces

        """
        pass

    def test_list_resource_claim_for_all_namespaces(self):
        """Test case for list_resource_claim_for_all_namespaces

        """
        pass

    def test_list_resource_claim_template_for_all_namespaces(self):
        """Test case for list_resource_claim_template_for_all_namespaces

        """
        pass

    def test_list_resource_class(self):
        """Test case for list_resource_class

        """
        pass

    def test_patch_namespaced_pod_scheduling(self):
        """Test case for patch_namespaced_pod_scheduling

        """
        pass

    def test_patch_namespaced_pod_scheduling_status(self):
        """Test case for patch_namespaced_pod_scheduling_status

        """
        pass

    def test_patch_namespaced_resource_claim(self):
        """Test case for patch_namespaced_resource_claim

        """
        pass

    def test_patch_namespaced_resource_claim_status(self):
        """Test case for patch_namespaced_resource_claim_status

        """
        pass

    def test_patch_namespaced_resource_claim_template(self):
        """Test case for patch_namespaced_resource_claim_template

        """
        pass

    def test_patch_resource_class(self):
        """Test case for patch_resource_class

        """
        pass

    def test_read_namespaced_pod_scheduling(self):
        """Test case for read_namespaced_pod_scheduling

        """
        pass

    def test_read_namespaced_pod_scheduling_status(self):
        """Test case for read_namespaced_pod_scheduling_status

        """
        pass

    def test_read_namespaced_resource_claim(self):
        """Test case for read_namespaced_resource_claim

        """
        pass

    def test_read_namespaced_resource_claim_status(self):
        """Test case for read_namespaced_resource_claim_status

        """
        pass

    def test_read_namespaced_resource_claim_template(self):
        """Test case for read_namespaced_resource_claim_template

        """
        pass

    def test_read_resource_class(self):
        """Test case for read_resource_class

        """
        pass

    def test_replace_namespaced_pod_scheduling(self):
        """Test case for replace_namespaced_pod_scheduling

        """
        pass

    def test_replace_namespaced_pod_scheduling_status(self):
        """Test case for replace_namespaced_pod_scheduling_status

        """
        pass

    def test_replace_namespaced_resource_claim(self):
        """Test case for replace_namespaced_resource_claim

        """
        pass

    def test_replace_namespaced_resource_claim_status(self):
        """Test case for replace_namespaced_resource_claim_status

        """
        pass

    def test_replace_namespaced_resource_claim_template(self):
        """Test case for replace_namespaced_resource_claim_template

        """
        pass

    def test_replace_resource_class(self):
        """Test case for replace_resource_class

        """
        pass


if __name__ == '__main__':
    unittest.main()