from typing import Optional, List, Union
from enum import Enum


class Course:
    reference: str

    def __init__(self, reference: str) -> None:
        self.reference = reference


class EventEventGroups:
    event_group: Course

    def __init__(self, event_group: Course) -> None:
        self.event_group = event_group


class AssignTimeConstraintAppliesTo:
    event_groups: EventEventGroups

    def __init__(self, event_groups: EventEventGroups) -> None:
        self.event_groups = event_groups


class AssignTimeConstraintTimeGroups:
    time_group: Course

    def __init__(self, time_group: Course) -> None:
        self.time_group = time_group


class Constraint:
    name: str
    required: bool
    weight: int
    cost_function: str
    applies_to: AssignTimeConstraintAppliesTo
    id: str
    time_groups: Optional[AssignTimeConstraintTimeGroups]
    duration: Optional[int]

    def __init__(self, name: str, required: bool, weight: int, cost_function: str, applies_to: AssignTimeConstraintAppliesTo, id: str, time_groups: Optional[AssignTimeConstraintTimeGroups], duration: Optional[int]) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.id = id
        self.time_groups = time_groups
        self.duration = duration


class PurpleResourceGroups:
    resource_group: List[Course]

    def __init__(self, resource_group: List[Course]) -> None:
        self.resource_group = resource_group


class AvoidClashesConstraintAppliesTo:
    resource_groups: PurpleResourceGroups

    def __init__(self, resource_groups: PurpleResourceGroups) -> None:
        self.resource_groups = resource_groups


class AvoidClashesConstraint:
    name: str
    required: bool
    weight: int
    cost_function: str
    applies_to: AvoidClashesConstraintAppliesTo
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: str, applies_to: AvoidClashesConstraintAppliesTo, id: str) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.id = id


class PurpleResources:
    resource: Course

    def __init__(self, resource: Course) -> None:
        self.resource = resource


class AvoidUnavailableTimesConstraintAppliesTo:
    resources: PurpleResources

    def __init__(self, resources: PurpleResources) -> None:
        self.resources = resources


class AvoidUnavailableTimesConstraintTimes:
    time: List[Course]

    def __init__(self, time: List[Course]) -> None:
        self.time = time


class AvoidUnavailableTimesConstraint:
    name: str
    required: bool
    weight: int
    cost_function: str
    applies_to: AvoidUnavailableTimesConstraintAppliesTo
    times: AvoidUnavailableTimesConstraintTimes
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: str, applies_to: AvoidUnavailableTimesConstraintAppliesTo, times: AvoidUnavailableTimesConstraintTimes, id: str) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.times = times
        self.id = id


class FluffyResources:
    resource: List[Course]

    def __init__(self, resource: List[Course]) -> None:
        self.resource = resource


class ClusterBusyTimesConstraintAppliesTo:
    resources: FluffyResources

    def __init__(self, resources: FluffyResources) -> None:
        self.resources = resources


class ClusterBusyTimesConstraintTimeGroups:
    time_group: List[Course]

    def __init__(self, time_group: List[Course]) -> None:
        self.time_group = time_group


class ClusterBusyTimesConstraint:
    name: str
    required: bool
    weight: int
    cost_function: str
    applies_to: ClusterBusyTimesConstraintAppliesTo
    time_groups: ClusterBusyTimesConstraintTimeGroups
    minimum: int
    maximum: int
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: str, applies_to: ClusterBusyTimesConstraintAppliesTo, time_groups: ClusterBusyTimesConstraintTimeGroups, minimum: int, maximum: int, id: str) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.time_groups = time_groups
        self.minimum = minimum
        self.maximum = maximum
        self.id = id


class PurpleEventGroups:
    event_group: List[Course]

    def __init__(self, event_group: List[Course]) -> None:
        self.event_group = event_group


class DistributeSplitEventsConstraintAppliesTo:
    event_groups: PurpleEventGroups

    def __init__(self, event_groups: PurpleEventGroups) -> None:
        self.event_groups = event_groups


class DistributeSplitEventsConstraint:
    name: str
    required: bool
    weight: int
    cost_function: str
    applies_to: DistributeSplitEventsConstraintAppliesTo
    duration: int
    minimum: int
    maximum: int
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: str, applies_to: DistributeSplitEventsConstraintAppliesTo, duration: int, minimum: int, maximum: int, id: str) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.duration = duration
        self.minimum = minimum
        self.maximum = maximum
        self.id = id


class ResourceResourceGroups:
    resource_group: Course

    def __init__(self, resource_group: Course) -> None:
        self.resource_group = resource_group


class LimitIdleTimesConstraintAppliesTo:
    resource_groups: ResourceResourceGroups

    def __init__(self, resource_groups: ResourceResourceGroups) -> None:
        self.resource_groups = resource_groups


class LimitIdleTimesConstraint:
    name: str
    required: bool
    weight: int
    cost_function: str
    applies_to: LimitIdleTimesConstraintAppliesTo
    time_groups: ClusterBusyTimesConstraintTimeGroups
    minimum: int
    maximum: int
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: str, applies_to: LimitIdleTimesConstraintAppliesTo, time_groups: ClusterBusyTimesConstraintTimeGroups, minimum: int, maximum: int, id: str) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.time_groups = time_groups
        self.minimum = minimum
        self.maximum = maximum
        self.id = id


class SplitEventsConstraint:
    name: str
    required: bool
    weight: int
    cost_function: str
    applies_to: AssignTimeConstraintAppliesTo
    minimum_duration: int
    maximum_duration: int
    minimum_amount: int
    maximum_amount: int
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: str, applies_to: AssignTimeConstraintAppliesTo, minimum_duration: int, maximum_duration: int, minimum_amount: int, maximum_amount: int, id: str) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.minimum_duration = minimum_duration
        self.maximum_duration = maximum_duration
        self.minimum_amount = minimum_amount
        self.maximum_amount = maximum_amount
        self.id = id


class TimeGroup:
    minimum: int
    maximum: int
    reference: str

    def __init__(self, minimum: int, maximum: int, reference: str) -> None:
        self.minimum = minimum
        self.maximum = maximum
        self.reference = reference


class SpreadEventsConstraintTimeGroups:
    time_group: List[TimeGroup]

    def __init__(self, time_group: List[TimeGroup]) -> None:
        self.time_group = time_group


class SpreadEventsConstraint:
    name: str
    required: bool
    weight: int
    cost_function: str
    applies_to: DistributeSplitEventsConstraintAppliesTo
    time_groups: SpreadEventsConstraintTimeGroups
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: str, applies_to: DistributeSplitEventsConstraintAppliesTo, time_groups: SpreadEventsConstraintTimeGroups, id: str) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.time_groups = time_groups
        self.id = id


class Constraints:
    assign_time_constraint: Constraint
    split_events_constraint: SplitEventsConstraint
    distribute_split_events_constraint: List[DistributeSplitEventsConstraint]
    prefer_times_constraint: Constraint
    spread_events_constraint: SpreadEventsConstraint
    avoid_clashes_constraint: AvoidClashesConstraint
    avoid_unavailable_times_constraint: List[AvoidUnavailableTimesConstraint]
    limit_idle_times_constraint: LimitIdleTimesConstraint
    cluster_busy_times_constraint: List[ClusterBusyTimesConstraint]

    def __init__(self, assign_time_constraint: Constraint, split_events_constraint: SplitEventsConstraint, distribute_split_events_constraint: List[DistributeSplitEventsConstraint], prefer_times_constraint: Constraint, spread_events_constraint: SpreadEventsConstraint, avoid_clashes_constraint: AvoidClashesConstraint, avoid_unavailable_times_constraint: List[AvoidUnavailableTimesConstraint], limit_idle_times_constraint: LimitIdleTimesConstraint, cluster_busy_times_constraint: List[ClusterBusyTimesConstraint]) -> None:
        self.assign_time_constraint = assign_time_constraint
        self.split_events_constraint = split_events_constraint
        self.distribute_split_events_constraint = distribute_split_events_constraint
        self.prefer_times_constraint = prefer_times_constraint
        self.spread_events_constraint = spread_events_constraint
        self.avoid_clashes_constraint = avoid_clashes_constraint
        self.avoid_unavailable_times_constraint = avoid_unavailable_times_constraint
        self.limit_idle_times_constraint = limit_idle_times_constraint
        self.cluster_busy_times_constraint = cluster_busy_times_constraint


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


class EventResources:
    resource: List[Resource]

    def __init__(self, resource: List[Resource]) -> None:
        self.resource = resource


class PurpleEvent:
    name: str
    duration: int
    course: Course
    resources: EventResources
    event_groups: EventEventGroups
    id: str

    def __init__(self, name: str, duration: int, course: Course, resources: EventResources, event_groups: EventEventGroups, id: str) -> None:
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


class InstanceEvents:
    event_groups: EventsEventGroups
    event: List[PurpleEvent]

    def __init__(self, event_groups: EventsEventGroups, event: List[PurpleEvent]) -> None:
        self.event_groups = event_groups
        self.event = event


class InstanceMetaData:
    name: str
    contributor: str
    date: str
    country: str
    description: str
    remarks: str

    def __init__(self, name: str, contributor: str, date: str, country: str, description: str, remarks: str) -> None:
        self.name = name
        self.contributor = contributor
        self.date = date
        self.country = country
        self.description = description
        self.remarks = remarks


class ResourceGroupElement:
    name: str
    resource_type: Course
    resource_groups: Optional[ResourceResourceGroups]
    id: str

    def __init__(self, name: str, resource_type: Course, resource_groups: Optional[ResourceResourceGroups], id: str) -> None:
        self.name = name
        self.resource_type = resource_type
        self.resource_groups = resource_groups
        self.id = id


class ResourcesResourceGroups:
    resource_group: List[ResourceGroupElement]

    def __init__(self, resource_group: List[ResourceGroupElement]) -> None:
        self.resource_group = resource_group


class ResourceTypes:
    resource_type: List[EventGroup]

    def __init__(self, resource_type: List[EventGroup]) -> None:
        self.resource_type = resource_type


class InstanceResources:
    resource_types: ResourceTypes
    resource_groups: ResourcesResourceGroups
    resource: List[ResourceGroupElement]

    def __init__(self, resource_types: ResourceTypes, resource_groups: ResourcesResourceGroups, resource: List[ResourceGroupElement]) -> None:
        self.resource_types = resource_types
        self.resource_groups = resource_groups
        self.resource = resource


class Time:
    name: str
    day: Course
    time_groups: Union[AssignTimeConstraintTimeGroups, str]
    id: str

    def __init__(self, name: str, day: Course, time_groups: Union[AssignTimeConstraintTimeGroups, str], id: str) -> None:
        self.name = name
        self.day = day
        self.time_groups = time_groups
        self.id = id


class TimesTimeGroups:
    day: List[EventGroup]
    time_group: EventGroup

    def __init__(self, day: List[EventGroup], time_group: EventGroup) -> None:
        self.day = day
        self.time_group = time_group


class InstanceTimes:
    time_groups: TimesTimeGroups
    time: List[Time]

    def __init__(self, time_groups: TimesTimeGroups, time: List[Time]) -> None:
        self.time_groups = time_groups
        self.time = time


class Instance:
    meta_data: InstanceMetaData
    times: InstanceTimes
    resources: InstanceResources
    events: InstanceEvents
    constraints: Constraints
    id: str

    def __init__(self, meta_data: InstanceMetaData, times: InstanceTimes, resources: InstanceResources, events: InstanceEvents, constraints: Constraints, id: str) -> None:
        self.meta_data = meta_data
        self.times = times
        self.resources = resources
        self.events = events
        self.constraints = constraints
        self.id = id


class Instances:
    instance: Instance

    def __init__(self, instance: Instance) -> None:
        self.instance = instance


class SolutionGroupMetaData:
    contributor: str
    date: str
    description: str

    def __init__(self, contributor: str, date: str, description: str) -> None:
        self.contributor = contributor
        self.date = date
        self.description = description


class FluffyEvent:
    duration: int
    time: Course
    reference: str

    def __init__(self, duration: int, time: Course, reference: str) -> None:
        self.duration = duration
        self.time = time
        self.reference = reference


class SolutionEvents:
    event: List[FluffyEvent]

    def __init__(self, event: List[FluffyEvent]) -> None:
        self.event = event


class Solution:
    events: SolutionEvents
    reference: str
    description: Optional[str]

    def __init__(self, events: SolutionEvents, reference: str, description: Optional[str]) -> None:
        self.events = events
        self.reference = reference
        self.description = description


class SolutionGroup:
    meta_data: SolutionGroupMetaData
    solution: Solution
    id: str

    def __init__(self, meta_data: SolutionGroupMetaData, solution: Solution, id: str) -> None:
        self.meta_data = meta_data
        self.solution = solution
        self.id = id


class SolutionGroups:
    solution_group: List[SolutionGroup]

    def __init__(self, solution_group: List[SolutionGroup]) -> None:
        self.solution_group = solution_group


class HighSchoolTimetableArchive:
    instances: Instances
    solution_groups: SolutionGroups

    def __init__(self, instances: Instances, solution_groups: SolutionGroups) -> None:
        self.instances = instances
        self.solution_groups = solution_groups


class Welcome2:
    high_school_timetable_archive: HighSchoolTimetableArchive

    def __init__(self, high_school_timetable_archive: HighSchoolTimetableArchive) -> None:
        self.high_school_timetable_archive = high_school_timetable_archive
