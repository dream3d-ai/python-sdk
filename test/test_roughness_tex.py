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
from dream3d.models.roughness_tex import RoughnessTex  # noqa: E501
from dream3d.rest import ApiException

class TestRoughnessTex(unittest.TestCase):
    """RoughnessTex unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RoughnessTex
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoughnessTex`
        """
        model = dream3d.models.roughness_tex.RoughnessTex()  # noqa: E501
        if include_optional :
            return RoughnessTex(
            )
        else :
            return RoughnessTex(
        )
        """

    def testRoughnessTex(self):
        """Test RoughnessTex"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
