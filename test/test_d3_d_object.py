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
from dream3d.models.d3_d_object import D3DObject  # noqa: E501
from dream3d.rest import ApiException

class TestD3DObject(unittest.TestCase):
    """D3DObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test D3DObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `D3DObject`
        """
        model = dream3d.models.d3_d_object.D3DObject()  # noqa: E501
        if include_optional :
            return D3DObject(
                id = '', 
                geometry = 'boxBufferGeometry', 
                position = [
                    1.337
                    ], 
                scale = [
                    1.337
                    ], 
                scale_linked = True, 
                rotation = [
                    1.337
                    ], 
                color = '', 
                matrix_world = [
                    1.337
                    ], 
                prompt = '', 
                mesh_id = '', 
                description = '', 
                mesh_url = '', 
                args = [
                    1.337
                    ], 
                visible = True, 
                url = '', 
                root_id = '', 
                parent_id = '', 
                children = [
                    ''
                    ], 
                material_strength = 1.337, 
                detail_strength = 1.337, 
                material_id = '', 
                material_preset = 'glass', 
                material_shader = 'DIFFUSE', 
                material_properties = dream3d.models.material_properties.MaterialProperties(
                    color = null, 
                    color_tex = null, 
                    roughness = 1.337, 
                    roughness_tex = null, 
                    metalness = 1.337, 
                    metalness_tex = null, 
                    normal_tex = null, 
                    normaltilt_iar = 1.337, 
                    specular = 1.337, 
                    albedo_color = null, 
                    subsurface_color = null, 
                    radiation_length = 1.337, 
                    light_emission = 1.337, 
                    refraction_index = null, 
                    flags = null, )
            )
        else :
            return D3DObject(
                id = '',
                geometry = 'boxBufferGeometry',
                position = [
                    1.337
                    ],
                scale = [
                    1.337
                    ],
                rotation = [
                    1.337
                    ],
                color = '',
        )
        """

    def testD3DObject(self):
        """Test D3DObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()