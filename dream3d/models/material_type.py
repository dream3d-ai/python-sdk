# coding: utf-8

"""
    dream3d

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class MaterialType(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    GENERATED = 'generated'
    UPLOADED = 'uploaded'

    @classmethod
    def from_json(cls, json_str: str) -> MaterialType:
        """Create an instance of MaterialType from a JSON string"""
        return MaterialType(json.loads(json_str))


