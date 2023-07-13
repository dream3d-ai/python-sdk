# coding: utf-8

"""
    dream3d

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import dream3d
from dream3d.models.project_create import ProjectCreate  # noqa: E501
from dream3d.rest import ApiException

class TestProjectCreate(unittest.TestCase):
    """ProjectCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectCreate`
        """
        model = dream3d.models.project_create.ProjectCreate()  # noqa: E501
        if include_optional :
            return ProjectCreate(
                name = '', 
                owner_id = 56, 
                s3_uri = '', 
                preview_uri = '', 
                edited_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                latest_artifact_id = '', 
                public = True, 
                payload = None, 
                is_new = True
            )
        else :
            return ProjectCreate(
                owner_id = 56,
        )
        """

    def testProjectCreate(self):
        """Test ProjectCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()