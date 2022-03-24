from enum import Enum
from typing import Optional, List


class Reference(Enum):
    CLASS = "Class"
    GR_CLASSES = "gr_Classes"
    GR_TEACHERS = "gr_Teachers"
    TEACHER = "Teacher"


class ResourceTypeClass:
    reference: Reference

    def __init__(self, reference: Reference) -> None:
        self.reference = reference


class ResourceResourceGroups:
    resource_group: ResourceTypeClass

    def __init__(self, resource_group: ResourceTypeClass) -> None:
        self.resource_group = resource_group


class Resource:
    name: str
    resource_type: ResourceTypeClass
    resource_groups: Optional[ResourceResourceGroups]
    id: str

    def __init__(self, name: str, resource_type: ResourceTypeClass, resource_groups: Optional[ResourceResourceGroups], id: str) -> None:
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

