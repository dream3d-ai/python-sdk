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
from dream3d.models.location_inner import LocationInner  # noqa: E501
from dream3d.rest import ApiException

class TestLocationInner(unittest.TestCase):
    """LocationInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LocationInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LocationInner`
        """
        model = dream3d.models.location_inner.LocationInner()  # noqa: E501
        if include_optional :
            return LocationInner(
            )
        else :
            return LocationInner(
        )
        """

    def testLocationInner(self):
        """Test LocationInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
