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
from dream3d.models.material_properties import MaterialProperties  # noqa: E501
from dream3d.rest import ApiException

class TestMaterialProperties(unittest.TestCase):
    """MaterialProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MaterialProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MaterialProperties`
        """
        model = dream3d.models.material_properties.MaterialProperties()  # noqa: E501
        if include_optional :
            return MaterialProperties(
                color = None, 
                color_tex = None, 
                roughness = 1.337, 
                roughness_tex = None, 
                metalness = 1.337, 
                metalness_tex = None, 
                normal_tex = None, 
                normaltilt_iar = 1.337, 
                specular = 1.337, 
                albedo_color = None, 
                subsurface_color = None, 
                radiation_length = 1.337, 
                light_emission = 1.337, 
                refraction_index = None, 
                flags = None
            )
        else :
            return MaterialProperties(
        )
        """

    def testMaterialProperties(self):
        """Test MaterialProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()