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
from dream3d.models.related_user import RelatedUser  # noqa: E501
from dream3d.rest import ApiException

class TestRelatedUser(unittest.TestCase):
    """RelatedUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RelatedUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelatedUser`
        """
        model = dream3d.models.related_user.RelatedUser()  # noqa: E501
        if include_optional :
            return RelatedUser(
                id = 56, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                first_name = '', 
                last_name = '', 
                email = '', 
                phone_number = '', 
                photo = ''
            )
        else :
            return RelatedUser(
        )
        """

    def testRelatedUser(self):
        """Test RelatedUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
