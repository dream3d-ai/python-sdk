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
from dream3d.models.mesh_update import MeshUpdate  # noqa: E501
from dream3d.rest import ApiException

class TestMeshUpdate(unittest.TestCase):
    """MeshUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MeshUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MeshUpdate`
        """
        model = dream3d.models.mesh_update.MeshUpdate()  # noqa: E501
        if include_optional :
            return MeshUpdate(
                name = '', 
                prompt = '', 
                public = True, 
                status = 'pending', 
                extents = [
                    1.337
                    ]
            )
        else :
            return MeshUpdate(
        )
        """

    def testMeshUpdate(self):
        """Test MeshUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
