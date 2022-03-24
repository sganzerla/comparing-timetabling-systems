from enum import Enum
from typing import List, Union, Optional


class Color(Enum):
    THE_0099_FF = "#0099FF"


class EventGroup:
    reference: str

    def __init__(self, reference: str) -> None:
        self.reference = reference


class EventEventGroups:
    event_group: Union[List[EventGroup], EventGroup]

    def __init__(self, event_group: Union[List[EventGroup], EventGroup]) -> None:
        self.event_group = event_group


class Resource:
    reference: Optional[str]
    role: Optional[int]
    resource_type: Optional[EventGroup]

    def __init__(self, reference: Optional[str], role: Optional[int], resource_type: Optional[EventGroup]) -> None:
        self.reference = reference
        self.role = role
        self.resource_type = resource_type


class Resources:
    resource: List[Resource]

    def __init__(self, resource: List[Resource]) -> None:
        self.resource = resource


class Event:
    name: str
    duration: int
    resources: Resources
    event_groups: EventEventGroups
    id: str
    color: Color

    def __init__(self, name: str, duration: int, resources: Resources, event_groups: EventEventGroups, id: str, color: Color) -> None:
        self.name = name
        self.duration = duration
        self.resources = resources
        self.event_groups = event_groups
        self.id = id
        self.color = color


class EventGroupsEventGroupClass:
    name: str
    id: str

    def __init__(self, name: str, id: str) -> None:
        self.name = name
        self.id = id


class EventsEventGroups:
    event_group: List[EventGroupsEventGroupClass]

    def __init__(self, event_group: List[EventGroupsEventGroupClass]) -> None:
        self.event_group = event_group


class Events:
    event_groups: EventsEventGroups
    event: List[Event]

    def __init__(self, event_groups: EventsEventGroups, event: List[Event]) -> None:
        self.event_groups = event_groups
        self.event = event

