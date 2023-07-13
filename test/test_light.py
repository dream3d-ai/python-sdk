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
from dream3d.models.light import Light  # noqa: E501
from dream3d.rest import ApiException

class TestLight(unittest.TestCase):
    """Light unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Light
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Light`
        """
        model = dream3d.models.light.Light()  # noqa: E501
        if include_optional :
            return Light(
                type = 'DIRECTIONAL', 
                color = [
                    1.337
                    ], 
                intensity = 1.337, 
                direction = [
                    1.337
                    ]
            )
        else :
            return Light(
                color = [
                    1.337
                    ],
                intensity = 1.337,
                direction = [
                    1.337
                    ],
        )
        """

    def testLight(self):
        """Test Light"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
