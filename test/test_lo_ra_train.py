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
from dream3d.models.lo_ra_train import LoRATrain  # noqa: E501
from dream3d.rest import ApiException

class TestLoRATrain(unittest.TestCase):
    """LoRATrain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LoRATrain
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoRATrain`
        """
        model = dream3d.models.lo_ra_train.LoRATrain()  # noqa: E501
        if include_optional :
            return LoRATrain(
                params = dream3d.models.lo_ra_params.LoRAParams(
                    train_text_encoder = True, 
                    train_batch_size = 56, 
                    gradient_accumulation_steps = 56, 
                    gradient_checkpointing = True, 
                    lr_scheduler = 'constant', 
                    scale_lr = True, 
                    lr_warmup_steps = 56, 
                    clip_ti_decay = True, 
                    color_jitter = True, 
                    continue_inversion = True, 
                    continue_inversion_lr = 1.337, 
                    initializer_tokens = '', 
                    learning_rate_text = 1.337, 
                    learning_rate_ti = 1.337, 
                    learning_rate_unet = 1.337, 
                    lr_scheduler_lora = 'constant', 
                    lr_warmup_steps_lora = 56, 
                    max_train_steps_ti = 56, 
                    max_train_steps_tuning = 56, 
                    placeholder_token_at_data = '', 
                    placeholder_tokens = '<s1>|<s2>', 
                    weight_decay_lora = 1.337, 
                    weight_decay_ti = 1.337, )
            )
        else :
            return LoRATrain(
                params = dream3d.models.lo_ra_params.LoRAParams(
                    train_text_encoder = True, 
                    train_batch_size = 56, 
                    gradient_accumulation_steps = 56, 
                    gradient_checkpointing = True, 
                    lr_scheduler = 'constant', 
                    scale_lr = True, 
                    lr_warmup_steps = 56, 
                    clip_ti_decay = True, 
                    color_jitter = True, 
                    continue_inversion = True, 
                    continue_inversion_lr = 1.337, 
                    initializer_tokens = '', 
                    learning_rate_text = 1.337, 
                    learning_rate_ti = 1.337, 
                    learning_rate_unet = 1.337, 
                    lr_scheduler_lora = 'constant', 
                    lr_warmup_steps_lora = 56, 
                    max_train_steps_ti = 56, 
                    max_train_steps_tuning = 56, 
                    placeholder_token_at_data = '', 
                    placeholder_tokens = '<s1>|<s2>', 
                    weight_decay_lora = 1.337, 
                    weight_decay_ti = 1.337, ),
        )
        """

    def testLoRATrain(self):
        """Test LoRATrain"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
