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
from dream3d.models.image_in import ImageIn  # noqa: E501
from dream3d.rest import ApiException

class TestImageIn(unittest.TestCase):
    """ImageIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ImageIn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImageIn`
        """
        model = dream3d.models.image_in.ImageIn()  # noqa: E501
        if include_optional :
            return ImageIn(
                data_uri = ''
            )
        else :
            return ImageIn(
                data_uri = '',
        )
        """

    def testImageIn(self):
        """Test ImageIn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
