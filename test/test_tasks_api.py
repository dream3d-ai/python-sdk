# coding: utf-8

"""
    dream3d

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import dream3d
from dream3d.api.tasks_api import TasksApi  # noqa: E501
from dream3d.rest import ApiException


class TestTasksApi(unittest.TestCase):
    """TasksApi unit test stubs"""

    def setUp(self):
        self.api = dream3d.api.tasks_api.TasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_v1_tasks_task_id_get(self):
        """Test case for get_api_v1_tasks_task_id_get

        Get  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()