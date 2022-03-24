from enum import Enum
from typing import List


class Course:
    reference: str

    def __init__(self, reference: str) -> None:
        self.reference = reference


class EventEventGroups:
    event_group: Course

    def __init__(self, event_group: Course) -> None:
        self.event_group = event_group


class Role(Enum):
    CLASS = "Class"
    TEACHER = "Teacher"


class Resource:
    role: Role
    resource_type: Course
    reference: str

    def __init__(self, role: Role, resource_type: Course, reference: str) -> None:
        self.role = role
        self.resource_type = resource_type
        self.reference = reference


class Resources:
    resource: List[Resource]

    def __init__(self, resource: List[Resource]) -> None:
        self.resource = resource


class Event:
    name: str
    duration: int
    course: Course
    resources: Resources
    event_groups: EventEventGroups
    id: str

    def __init__(self, name: str, duration: int, course: Course, resources: Resources, event_groups: EventEventGroups, id: str) -> None:
        self.name = name
        self.duration = duration
        self.course = course
        self.resources = resources
        self.event_groups = event_groups
        self.id = id


class EventGroup:
    name: str
    id: str

    def __init__(self, name: str, id: str) -> None:
        self.name = name
        self.id = id


class EventsEventGroups:
    course: List[EventGroup]
    event_group: EventGroup

    def __init__(self, course: List[EventGroup], event_group: EventGroup) -> None:
        self.course = course
        self.event_group = event_group


class Events:
    event_groups: EventsEventGroups
    event: List[Event]

    def __init__(self, event_groups: EventsEventGroups, event: List[Event]) -> None:
        self.event_groups = event_groups
        self.event = event

