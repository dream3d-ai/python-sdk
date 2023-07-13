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


from typing import Any, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from dream3d.models.render_aspect_ratio import RenderAspectRatio
from dream3d.models.scene import Scene
from dream3d.models.wysiwyg_version import WysiwygVersion

class Payload(BaseModel):
    """
    Payload
    """
    prompt: Optional[StrictStr] = ''
    negative_prompt: Optional[StrictStr] = None
    scene: Optional[Scene] = None
    aspect_ratio: Optional[RenderAspectRatio] = None
    num_images_per_prompt: Optional[StrictInt] = 1
    strength: Optional[Union[StrictFloat, StrictInt]] = 0.75
    material_alpha: Optional[Union[StrictFloat, StrictInt]] = 1.0
    num_inference_steps: Optional[StrictInt] = 20
    num_reference_free_steps: Optional[StrictInt] = 0
    num_control_free_steps: Optional[StrictInt] = 0
    guidance_scale: Optional[Union[StrictFloat, StrictInt]] = 7.5
    blur_radius: Optional[Union[StrictFloat, StrictInt]] = 0.0
    seed: Optional[StrictInt] = None
    floor: Optional[StrictBool] = True
    use_seed: Optional[StrictBool] = False
    control_ranges: Optional[conlist(conlist(Any))] = None
    lora_ids: Optional[conlist(StrictStr)] = None
    lora_scales: Optional[conlist(Union[StrictFloat, StrictInt])] = None
    model_type: Optional[WysiwygVersion] = None
    style_reference_id: Optional[StrictStr] = None
    __properties = ["prompt", "negative_prompt", "scene", "aspect_ratio", "num_images_per_prompt", "strength", "material_alpha", "num_inference_steps", "num_reference_free_steps", "num_control_free_steps", "guidance_scale", "blur_radius", "seed", "floor", "use_seed", "control_ranges", "lora_ids", "lora_scales", "model_type", "style_reference_id"]

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
    def from_json(cls, json_str: str) -> Payload:
        """Create an instance of Payload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of scene
        if self.scene:
            _dict['scene'] = self.scene.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Payload:
        """Create an instance of Payload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Payload.parse_obj(obj)

        _obj = Payload.parse_obj({
            "prompt": obj.get("prompt") if obj.get("prompt") is not None else '',
            "negative_prompt": obj.get("negative_prompt"),
            "scene": Scene.from_dict(obj.get("scene")) if obj.get("scene") is not None else None,
            "aspect_ratio": obj.get("aspect_ratio"),
            "num_images_per_prompt": obj.get("num_images_per_prompt") if obj.get("num_images_per_prompt") is not None else 1,
            "strength": obj.get("strength") if obj.get("strength") is not None else 0.75,
            "material_alpha": obj.get("material_alpha") if obj.get("material_alpha") is not None else 1.0,
            "num_inference_steps": obj.get("num_inference_steps") if obj.get("num_inference_steps") is not None else 20,
            "num_reference_free_steps": obj.get("num_reference_free_steps") if obj.get("num_reference_free_steps") is not None else 0,
            "num_control_free_steps": obj.get("num_control_free_steps") if obj.get("num_control_free_steps") is not None else 0,
            "guidance_scale": obj.get("guidance_scale") if obj.get("guidance_scale") is not None else 7.5,
            "blur_radius": obj.get("blur_radius") if obj.get("blur_radius") is not None else 0.0,
            "seed": obj.get("seed"),
            "floor": obj.get("floor") if obj.get("floor") is not None else True,
            "use_seed": obj.get("use_seed") if obj.get("use_seed") is not None else False,
            "control_ranges": obj.get("control_ranges"),
            "lora_ids": obj.get("lora_ids"),
            "lora_scales": obj.get("lora_scales"),
            "model_type": obj.get("model_type"),
            "style_reference_id": obj.get("style_reference_id")
        })
        return _obj

