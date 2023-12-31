# coding: utf-8

"""
    dream3d

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist

class Light(BaseModel):
    """
    Light
    """
    type: Optional[StrictStr] = 'DIRECTIONAL'
    color: conlist(Union[StrictFloat, StrictInt]) = Field(...)
    intensity: Union[StrictFloat, StrictInt] = Field(...)
    direction: conlist(Union[StrictFloat, StrictInt]) = Field(...)
    __properties = ["type", "color", "intensity", "direction"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Light:
        """Create an instance of Light from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Light:
        """Create an instance of Light from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Light.parse_obj(obj)

        _obj = Light.parse_obj({
            "type": obj.get("type") if obj.get("type") is not None else 'DIRECTIONAL',
            "color": obj.get("color"),
            "intensity": obj.get("intensity"),
            "direction": obj.get("direction")
        })
        return _obj

