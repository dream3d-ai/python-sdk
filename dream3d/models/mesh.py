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

from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from dream3d.models.lo_ra import LoRA
from dream3d.models.mesh_category import MeshCategory
from dream3d.models.mesh_format import MeshFormat
from dream3d.models.mesh_status import MeshStatus
from dream3d.models.mesh_type import MeshType

class Mesh(BaseModel):
    """
    Mesh
    """
    type: Optional[MeshType] = None
    category: Optional[MeshCategory] = None
    name: Optional[StrictStr] = None
    prompt: Optional[StrictStr] = None
    status: Optional[MeshStatus] = None
    public: Optional[StrictBool] = None
    creator_id: Optional[StrictInt] = None
    format: Optional[MeshFormat] = None
    embedding: Optional[conlist(Union[StrictFloat, StrictInt])] = None
    extents: Optional[conlist(Union[StrictFloat, StrictInt])] = None
    parent_mesh_id: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    avatar_image_url: Optional[StrictStr] = None
    glb_url: Optional[StrictStr] = None
    preview_url: Optional[StrictStr] = None
    obj_url: Optional[StrictStr] = None
    mtl_url: Optional[StrictStr] = None
    albedo_url: Optional[StrictStr] = None
    lora: Optional[LoRA] = None
    __properties = ["type", "category", "name", "prompt", "status", "public", "creator_id", "format", "embedding", "extents", "parent_mesh_id", "id", "created_at", "updated_at", "avatar_image_url", "glb_url", "preview_url", "obj_url", "mtl_url", "albedo_url", "lora"]

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
    def from_json(cls, json_str: str) -> Mesh:
        """Create an instance of Mesh from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of lora
        if self.lora:
            _dict['lora'] = self.lora.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Mesh:
        """Create an instance of Mesh from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Mesh.parse_obj(obj)

        _obj = Mesh.parse_obj({
            "type": obj.get("type"),
            "category": obj.get("category"),
            "name": obj.get("name"),
            "prompt": obj.get("prompt"),
            "status": obj.get("status"),
            "public": obj.get("public"),
            "creator_id": obj.get("creator_id"),
            "format": obj.get("format"),
            "embedding": obj.get("embedding"),
            "extents": obj.get("extents"),
            "parent_mesh_id": obj.get("parent_mesh_id"),
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "avatar_image_url": obj.get("avatar_image_url"),
            "glb_url": obj.get("glb_url"),
            "preview_url": obj.get("preview_url"),
            "obj_url": obj.get("obj_url"),
            "mtl_url": obj.get("mtl_url"),
            "albedo_url": obj.get("albedo_url"),
            "lora": LoRA.from_dict(obj.get("lora")) if obj.get("lora") is not None else None
        })
        return _obj

