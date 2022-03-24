from typing import List, Union, Optional
from enum import Enum


class TimeElement:
    reference: str

    def __init__(self, reference: str) -> None:
        self.reference = reference


class EventEventGroups:
    event_group: Union[List[TimeElement], TimeElement]

    def __init__(self, event_group: Union[List[TimeElement], TimeElement]) -> None:
        self.event_group = event_group


class Role(Enum):
    CLASS = "Class"
    CLASS1 = "Class1"
    COPRESENCE = "Copresence"
    CO_PRESENCE = "CoPresence"
    TEACHER = "Teacher"


class ResourceElement:
    role: Role
    resource_type: TimeElement
    reference: str

    def __init__(self, role: Role, resource_type: TimeElement, reference: str) -> None:
        self.role = role
        self.resource_type = resource_type
        self.reference = reference


class Resources:
    resource: Union[List[ResourceElement], ResourceElement]

    def __init__(self, resource: Union[List[ResourceElement], ResourceElement]) -> None:
        self.resource = resource


class Event:
    name: str
    duration: int
    course: TimeElement
    resources: Resources
    event_groups: Optional[EventEventGroups]
    id: str
    time: Optional[TimeElement]

    def __init__(self, name: str, duration: int, course: TimeElement, resources: Resources, event_groups: Optional[EventEventGroups], id: str, time: Optional[TimeElement]) -> None:
        self.name = name
        self.duration = duration
        self.course = course
        self.resources = resources
        self.event_groups = event_groups
        self.id = id
        self.time = time


class EventGroupsCourse:
    name: str
    id: str

    def __init__(self, name: str, id: str) -> None:
        self.name = name
        self.id = id


class EventsEventGroups:
    course: List[EventGroupsCourse]
    event_group: List[EventGroupsCourse]

    def __init__(self, course: List[EventGroupsCourse], event_group: List[EventGroupsCourse]) -> None:
        self.course = course
        self.event_group = event_group


class Events:
    event_groups: EventsEventGroups
    event: List[Event]

    def __init__(self, event_groups: EventsEventGroups, event: List[Event]) -> None:
        self.event_groups = event_groups
        self.event = event

