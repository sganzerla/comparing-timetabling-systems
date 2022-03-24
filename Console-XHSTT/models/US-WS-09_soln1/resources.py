from enum import Enum
from typing import List, Union, Optional


class Reference(Enum):
    ROOM = "Room"
    ROOM_ALL = "Room_All"
    ROOM_DEPT_1 = "Room_Dept_1"
    ROOM_DEPT_10 = "Room_Dept_10"
    ROOM_DEPT_12 = "Room_Dept_12"
    ROOM_DEPT_13 = "Room_Dept_13"
    ROOM_DEPT_15 = "Room_Dept_15"
    ROOM_DEPT_2 = "Room_Dept_2"
    ROOM_DEPT_22 = "Room_Dept_22"
    ROOM_DEPT_28 = "Room_Dept_28"
    ROOM_DEPT_3 = "Room_Dept_3"
    ROOM_DEPT_4 = "Room_Dept_4"
    ROOM_DEPT_5 = "Room_Dept_5"
    ROOM_DEPT_6 = "Room_Dept_6"
    ROOM_DEPT_7 = "Room_Dept_7"
    ROOM_DEPT_8 = "Room_Dept_8"
    ROOM_DEPT_9 = "Room_Dept_9"
    TEACHER = "Teacher"
    TEACHER_ALL = "Teacher_All"


class ResourceTypeElement:
    reference: Reference

    def __init__(self, reference: Reference) -> None:
        self.reference = reference


class ResourceResourceGroups:
    resource_group: Union[List[ResourceTypeElement], ResourceTypeElement]

    def __init__(self, resource_group: Union[List[ResourceTypeElement], ResourceTypeElement]) -> None:
        self.resource_group = resource_group


class Resource:
    name: str
    resource_type: ResourceTypeElement
    resource_groups: Optional[ResourceResourceGroups]
    id: str

    def __init__(self, name: str, resource_type: ResourceTypeElement, resource_groups: Optional[ResourceResourceGroups], id: str) -> None:
        self.name = name
        self.resource_type = resource_type
        self.resource_groups = resource_groups
        self.id = id


class ResourcesResourceGroups:
    resource_group: List[Resource]

    def __init__(self, resource_group: List[Resource]) -> None:
        self.resource_group = resource_group


class ResourceType:
    name: Reference
    id: Reference

    def __init__(self, name: Reference, id: Reference) -> None:
        self.name = name
        self.id = id


class ResourceTypes:
    resource_type: List[ResourceType]

    def __init__(self, resource_type: List[ResourceType]) -> None:
        self.resource_type = resource_type


class Resources:
    resource_types: ResourceTypes
    resource_groups: ResourcesResourceGroups
    resource: List[Resource]

    def __init__(self, resource_types: ResourceTypes, resource_groups: ResourcesResourceGroups, resource: List[Resource]) -> None:
        self.resource_types = resource_types
        self.resource_groups = resource_groups
        self.resource = resource

