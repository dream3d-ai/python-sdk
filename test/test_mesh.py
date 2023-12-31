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
from dream3d.models.mesh import Mesh  # noqa: E501
from dream3d.rest import ApiException

class TestMesh(unittest.TestCase):
    """Mesh unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Mesh
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Mesh`
        """
        model = dream3d.models.mesh.Mesh()  # noqa: E501
        if include_optional :
            return Mesh(
                type = 'generated', 
                category = 'all', 
                name = '', 
                prompt = '', 
                status = 'pending', 
                public = True, 
                creator_id = 56, 
                format = 'glb', 
                embedding = [
                    1.337
                    ], 
                extents = [
                    1.337
                    ], 
                parent_mesh_id = '', 
                id = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                avatar_image_url = '', 
                glb_url = '', 
                preview_url = '', 
                obj_url = '', 
                mtl_url = '', 
                albedo_url = '', 
                lora = dream3d.models.lo_ra.LoRA(
                    id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    mesh_id = '', 
                    status = 'pending', 
                    images = [
                        dream3d.models.image.Image(
                            url = '', 
                            key = '', )
                        ], 
                    zip_url = '', 
                    model_s3_url = '', 
                    image_dir = '', 
                    model_key = '', 
                    zip_key = '', )
            )
        else :
            return Mesh(
        )
        """

    def testMesh(self):
        """Test Mesh"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
