# Dream3D Python SDK

## Requirements

Python 3.7+

## Installation & Usage
### pip install


```sh
pip install git+https://github.com/dream3d-ai/python-sdk.git
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import dream3d
from dream3d.configuration import Configuration
from dream3d.rest import ApiException
from pprint import pprint

configuration = dream3d.Configuration(
    access_token=<YOUR_ACCESS_TOKEN>,
)

# Enter a context with an instance of the API client
async with dream3d.ApiClient(configuration=configuration) as api_client:
    # Create an instance of the API class
    api_instance = dream3d.ArtifactsApi(api_client)
    project_id = 'project_id_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    type = dream3d.ArtifactType() # ArtifactType |  (optional)

    try:
        # Get All
        api_response = await api_instance.get_all_api_v1_artifacts_project_project_id_get(project_id, skip=skip, limit=limit, type=type)
        print("The response of ArtifactsApi->get_all_api_v1_artifacts_project_project_id_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->get_all_api_v1_artifacts_project_project_id_get: %s\n" % e)

```

## Documentation for API Endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArtifactsApi* | [**get_all_api_v1_artifacts_project_project_id_get**](docs/ArtifactsApi.md#get_all_api_v1_artifacts_project_project_id_get) | **GET** /api/v1/artifacts/project/{project_id} | Get All
*ArtifactsApi* | [**get_api_v1_artifacts_artifact_id_get**](docs/ArtifactsApi.md#get_api_v1_artifacts_artifact_id_get) | **GET** /api/v1/artifacts/{artifact_id} | Get
*ArtifactsApi* | [**get_children_artifacts_api_v1_artifacts_project_project_id_parent_id_get**](docs/ArtifactsApi.md#get_children_artifacts_api_v1_artifacts_project_project_id_parent_id_get) | **GET** /api/v1/artifacts/project/{project_id}/{parent_id} | Get Children Artifacts
*ArtifactsApi* | [**get_feed_api_v1_artifacts_feed_get**](docs/ArtifactsApi.md#get_feed_api_v1_artifacts_feed_get) | **GET** /api/v1/artifacts/feed | Get Feed
*ArtifactsApi* | [**get_opengraph_url_api_v1_artifacts_artifact_id_og_get**](docs/ArtifactsApi.md#get_opengraph_url_api_v1_artifacts_artifact_id_og_get) | **GET** /api/v1/artifacts/{artifact_id}/og | Get Opengraph Url
*ArtifactsApi* | [**get_public_url_api_v1_artifacts_artifact_id_public_get**](docs/ArtifactsApi.md#get_public_url_api_v1_artifacts_artifact_id_public_get) | **GET** /api/v1/artifacts/{artifact_id}/public | Get Public Url
*ArtifactsApi* | [**get_templates_api_v1_artifacts_templates_get**](docs/ArtifactsApi.md#get_templates_api_v1_artifacts_templates_get) | **GET** /api/v1/artifacts/templates | Get Templates
*ArtifactsApi* | [**get_url_api_v1_artifacts_artifact_id_url_get**](docs/ArtifactsApi.md#get_url_api_v1_artifacts_artifact_id_url_get) | **GET** /api/v1/artifacts/{artifact_id}/url | Get Url
*ArtifactsApi* | [**like_api_v1_artifacts_artifact_id_like_put**](docs/ArtifactsApi.md#like_api_v1_artifacts_artifact_id_like_put) | **PUT** /api/v1/artifacts/{artifact_id}/like | Like
*ArtifactsApi* | [**record_view_api_v1_artifacts_artifact_id_view_post**](docs/ArtifactsApi.md#record_view_api_v1_artifacts_artifact_id_view_post) | **POST** /api/v1/artifacts/{artifact_id}/view | Record View
*ArtifactsApi* | [**remix_api_v1_artifacts_artifact_id_remix_post**](docs/ArtifactsApi.md#remix_api_v1_artifacts_artifact_id_remix_post) | **POST** /api/v1/artifacts/{artifact_id}/remix | Remix
*ArtifactsApi* | [**toggle_like_api_v1_artifacts_artifact_id_toggle_like_put**](docs/ArtifactsApi.md#toggle_like_api_v1_artifacts_artifact_id_toggle_like_put) | **PUT** /api/v1/artifacts/{artifact_id}/toggle-like | Toggle Like
*ArtifactsApi* | [**unlike_api_v1_artifacts_artifact_id_unlike_put**](docs/ArtifactsApi.md#unlike_api_v1_artifacts_artifact_id_unlike_put) | **PUT** /api/v1/artifacts/{artifact_id}/unlike | Unlike
*ArtifactsApi* | [**update_api_v1_artifacts_artifact_id_put**](docs/ArtifactsApi.md#update_api_v1_artifacts_artifact_id_put) | **PUT** /api/v1/artifacts/{artifact_id} | Update
*ArtifactsApi* | [**upscale_api_v1_artifacts_artifact_id_upscale_post**](docs/ArtifactsApi.md#upscale_api_v1_artifacts_artifact_id_upscale_post) | **POST** /api/v1/artifacts/{artifact_id}/upscale | Upscale
*MaterialsApi* | [**create_api_v1_materials_post**](docs/MaterialsApi.md#create_api_v1_materials_post) | **POST** /api/v1/materials/ | Create
*MaterialsApi* | [**get_api_v1_materials_material_id_get**](docs/MaterialsApi.md#get_api_v1_materials_material_id_get) | **GET** /api/v1/materials/{material_id} | Get
*MaterialsApi* | [**update_api_v1_materials_material_id_put**](docs/MaterialsApi.md#update_api_v1_materials_material_id_put) | **PUT** /api/v1/materials/{material_id} | Update
*MeshesApi* | [**create_avatar_api_v1_meshes_avatar_post**](docs/MeshesApi.md#create_avatar_api_v1_meshes_avatar_post) | **POST** /api/v1/meshes/avatar | Create Avatar
*MeshesApi* | [**create_prompt_api_v1_meshes_prompt_post**](docs/MeshesApi.md#create_prompt_api_v1_meshes_prompt_post) | **POST** /api/v1/meshes/prompt | Create Prompt
*MeshesApi* | [**create_upload_api_v1_meshes_upload_post**](docs/MeshesApi.md#create_upload_api_v1_meshes_upload_post) | **POST** /api/v1/meshes/upload | Create Upload
*MeshesApi* | [**delete_api_v1_meshes_mesh_id_delete**](docs/MeshesApi.md#delete_api_v1_meshes_mesh_id_delete) | **DELETE** /api/v1/meshes/{mesh_id} | Delete
*MeshesApi* | [**get_all_api_v1_meshes_get**](docs/MeshesApi.md#get_all_api_v1_meshes_get) | **GET** /api/v1/meshes/ | Get All
*MeshesApi* | [**get_api_v1_meshes_mesh_id_get**](docs/MeshesApi.md#get_api_v1_meshes_mesh_id_get) | **GET** /api/v1/meshes/{mesh_id} | Get
*MeshesApi* | [**regenerate_prompt_api_v1_meshes_regenerate_mesh_id_put**](docs/MeshesApi.md#regenerate_prompt_api_v1_meshes_regenerate_mesh_id_put) | **PUT** /api/v1/meshes/regenerate/{mesh_id} | Regenerate Prompt
*MeshesApi* | [**search_api_v1_meshes_search_get**](docs/MeshesApi.md#search_api_v1_meshes_search_get) | **GET** /api/v1/meshes/search | Search
*MeshesApi* | [**update_api_v1_meshes_mesh_id_put**](docs/MeshesApi.md#update_api_v1_meshes_mesh_id_put) | **PUT** /api/v1/meshes/{mesh_id} | Update
*ProjectsApi* | [**add_mesh_api_v1_projects_project_id_meshes_mesh_id_put**](docs/ProjectsApi.md#add_mesh_api_v1_projects_project_id_meshes_mesh_id_put) | **PUT** /api/v1/projects/{project_id}/meshes/{mesh_id} | Add Mesh
*ProjectsApi* | [**create_api_v1_projects_post**](docs/ProjectsApi.md#create_api_v1_projects_post) | **POST** /api/v1/projects/ | Create
*ProjectsApi* | [**delete_api_v1_projects_project_id_delete**](docs/ProjectsApi.md#delete_api_v1_projects_project_id_delete) | **DELETE** /api/v1/projects/{project_id} | Delete
*ProjectsApi* | [**get_all_api_v1_projects_get**](docs/ProjectsApi.md#get_all_api_v1_projects_get) | **GET** /api/v1/projects/ | Get All
*ProjectsApi* | [**get_api_v1_projects_project_id_get**](docs/ProjectsApi.md#get_api_v1_projects_project_id_get) | **GET** /api/v1/projects/{project_id} | Get
*ProjectsApi* | [**get_meshes_api_v1_projects_project_id_meshes_get**](docs/ProjectsApi.md#get_meshes_api_v1_projects_project_id_meshes_get) | **GET** /api/v1/projects/{project_id}/meshes | Get Meshes
*ProjectsApi* | [**remove_mesh_api_v1_projects_project_id_meshes_mesh_id_delete**](docs/ProjectsApi.md#remove_mesh_api_v1_projects_project_id_meshes_mesh_id_delete) | **DELETE** /api/v1/projects/{project_id}/meshes/{mesh_id} | Remove Mesh
*ProjectsApi* | [**update_api_v1_projects_project_id_put**](docs/ProjectsApi.md#update_api_v1_projects_project_id_put) | **PUT** /api/v1/projects/{project_id} | Update
*RenderApi* | [**create_api_v1_render_project_id_post**](docs/RenderApi.md#create_api_v1_render_project_id_post) | **POST** /api/v1/render/{project_id} | Create
*RenderApi* | [**extract_prompt_api_v1_render_extract_prompt_post**](docs/RenderApi.md#extract_prompt_api_v1_render_extract_prompt_post) | **POST** /api/v1/render/extract-prompt | Extract Prompt
*StatusApi* | [**get_status_get**](docs/StatusApi.md#get_status_get) | **GET** / | Get Status
*TasksApi* | [**get_api_v1_tasks_task_id_get**](docs/TasksApi.md#get_api_v1_tasks_task_id_get) | **GET** /api/v1/tasks/{task_id} | Get


## Documentation For Models

 - [Artifact](docs/Artifact.md)
 - [ArtifactStatus](docs/ArtifactStatus.md)
 - [ArtifactType](docs/ArtifactType.md)
 - [ArtifactUpdate](docs/ArtifactUpdate.md)
 - [Camera](docs/Camera.md)
 - [ColorTex](docs/ColorTex.md)
 - [D3DObject](docs/D3DObject.md)
 - [Flags](docs/Flags.md)
 - [GeometryType](docs/GeometryType.md)
 - [HDRI](docs/HDRI.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [Image](docs/Image.md)
 - [ImageIn](docs/ImageIn.md)
 - [Light](docs/Light.md)
 - [Material](docs/Material.md)
 - [MaterialCreateUpload](docs/MaterialCreateUpload.md)
 - [MaterialFlag](docs/MaterialFlag.md)
 - [MaterialPreset](docs/MaterialPreset.md)
 - [MaterialProperties](docs/MaterialProperties.md)
 - [MaterialShader](docs/MaterialShader.md)
 - [MaterialType](docs/MaterialType.md)
 - [MaterialUpdate](docs/MaterialUpdate.md)
 - [Mesh](docs/Mesh.md)
 - [MeshCategory](docs/MeshCategory.md)
 - [MeshCreateGenerate](docs/MeshCreateGenerate.md)
 - [MeshFormat](docs/MeshFormat.md)
 - [MeshStatus](docs/MeshStatus.md)
 - [MeshType](docs/MeshType.md)
 - [MeshUpdate](docs/MeshUpdate.md)
 - [MetalnessTex](docs/MetalnessTex.md)
 - [MeterUsage](docs/MeterUsage.md)
 - [Msg](docs/Msg.md)
 - [NormalTex](docs/NormalTex.md)
 - [Payload](docs/Payload.md)
 - [Project](docs/Project.md)
 - [ProjectCreate](docs/ProjectCreate.md)
 - [ProjectUpdate](docs/ProjectUpdate.md)
 - [RelatedUser](docs/RelatedUser.md)
 - [RenderAspectRatio](docs/RenderAspectRatio.md)
 - [RenderPayload](docs/RenderPayload.md)
 - [RoughnessTex](docs/RoughnessTex.md)
 - [Scene](docs/Scene.md)
 - [TaskStatus](docs/TaskStatus.md)
 - [UserAdminCreate](docs/UserAdminCreate.md)
 - [UserAdminInvite](docs/UserAdminInvite.md)
 - [UserUpdate](docs/UserUpdate.md)
 - [ValidationError](docs/ValidationError.md)
 - [WysiwygVersion](docs/WysiwygVersion.md)
