from enum import Enum
from typing import List, Optional, Union


class EventGroup:
    reference: str

    def __init__(self, reference: str) -> None:
        self.reference = reference


class EventGroups:
    event_group: EventGroup

    def __init__(self, event_group: EventGroup) -> None:
        self.event_group = event_group


class AssignResourceConstraintAppliesTo:
    event_groups: EventGroups

    def __init__(self, event_groups: EventGroups) -> None:
        self.event_groups = event_groups


class CostFunction(Enum):
    LINEAR = "Linear"


class Reference(Enum):
    DAY_0 = "Day_0"
    DAY_1 = "Day_1"
    DAY_2 = "Day_2"
    DAY_3 = "Day_3"
    DAY_4 = "Day_4"


class TimeGroup:
    minimum: int
    maximum: int
    reference: Reference

    def __init__(self, minimum: int, maximum: int, reference: Reference) -> None:
        self.minimum = minimum
        self.maximum = maximum
        self.reference = reference


class AssignResourceConstraintTimeGroups:
    time_group: List[TimeGroup]

    def __init__(self, time_group: List[TimeGroup]) -> None:
        self.time_group = time_group


class Constraint:
    name: str
    required: bool
    weight: int
    cost_function: CostFunction
    applies_to: AssignResourceConstraintAppliesTo
    role: Optional[int]
    id: str
    time_groups: Optional[AssignResourceConstraintTimeGroups]

    def __init__(self, name: str, required: bool, weight: int, cost_function: CostFunction, applies_to: AssignResourceConstraintAppliesTo, role: Optional[int], id: str, time_groups: Optional[AssignResourceConstraintTimeGroups]) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.role = role
        self.id = id
        self.time_groups = time_groups


class AppliesToResourceGroups:
    resource_group: List[EventGroup]

    def __init__(self, resource_group: List[EventGroup]) -> None:
        self.resource_group = resource_group


class AvoidClashesConstraintAppliesTo:
    resource_groups: AppliesToResourceGroups

    def __init__(self, resource_groups: AppliesToResourceGroups) -> None:
        self.resource_groups = resource_groups


class AvoidClashesConstraint:
    name: str
    required: bool
    weight: int
    cost_function: CostFunction
    applies_to: AvoidClashesConstraintAppliesTo
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: CostFunction, applies_to: AvoidClashesConstraintAppliesTo, id: str) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.id = id


class Events:
    event: Union[List[EventGroup], EventGroup]

    def __init__(self, event: Union[List[EventGroup], EventGroup]) -> None:
        self.event = event


class AppliesToAppliesTo:
    events: Events

    def __init__(self, events: Events) -> None:
        self.events = events


class PreferResourcesConstraintResourceGroups:
    resource_group: EventGroup

    def __init__(self, resource_group: EventGroup) -> None:
        self.resource_group = resource_group


class Resources:
    resource: EventGroup

    def __init__(self, resource: EventGroup) -> None:
        self.resource = resource


class PreferResourcesConstraint:
    name: str
    required: bool
    weight: int
    cost_function: CostFunction
    applies_to: Union[AppliesToAppliesTo, str]
    resources: Optional[Resources]
    role: int
    id: str
    resource_groups: Optional[PreferResourcesConstraintResourceGroups]

    def __init__(self, name: str, required: bool, weight: int, cost_function: CostFunction, applies_to: Union[AppliesToAppliesTo, str], resources: Optional[Resources], role: int, id: str, resource_groups: Optional[PreferResourcesConstraintResourceGroups]) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.resources = resources
        self.role = role
        self.id = id
        self.resource_groups = resource_groups


class PreferTimesConstraintAppliesTo:
    events: Optional[Events]
    event_groups: Optional[EventGroups]

    def __init__(self, events: Optional[Events], event_groups: Optional[EventGroups]) -> None:
        self.events = events
        self.event_groups = event_groups


class PreferTimesConstraintTimeGroups:
    time_group: EventGroup

    def __init__(self, time_group: EventGroup) -> None:
        self.time_group = time_group


class Times:
    time: List[EventGroup]

    def __init__(self, time: List[EventGroup]) -> None:
        self.time = time


class PreferTimesConstraint:
    name: str
    required: bool
    weight: int
    cost_function: CostFunction
    applies_to: PreferTimesConstraintAppliesTo
    times: Optional[Times]
    duration: int
    id: str
    time_groups: Optional[PreferTimesConstraintTimeGroups]

    def __init__(self, name: str, required: bool, weight: int, cost_function: CostFunction, applies_to: PreferTimesConstraintAppliesTo, times: Optional[Times], duration: int, id: str, time_groups: Optional[PreferTimesConstraintTimeGroups]) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.times = times
        self.duration = duration
        self.id = id
        self.time_groups = time_groups


class SplitEventsConstraint:
    name: str
    required: bool
    weight: int
    cost_function: CostFunction
    applies_to: AppliesToAppliesTo
    minimum_duration: int
    maximum_duration: int
    minimum_amount: int
    maximum_amount: int
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: CostFunction, applies_to: AppliesToAppliesTo, minimum_duration: int, maximum_duration: int, minimum_amount: int, maximum_amount: int, id: str) -> None:
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


class Constraints:
    assign_resource_constraint: Constraint
    assign_time_constraint: Constraint
    split_events_constraint: List[SplitEventsConstraint]
    prefer_resources_constraint: List[PreferResourcesConstraint]
    prefer_times_constraint: List[PreferTimesConstraint]
    spread_events_constraint: List[Constraint]
    avoid_clashes_constraint: AvoidClashesConstraint

    def __init__(self, assign_resource_constraint: Constraint, assign_time_constraint: Constraint, split_events_constraint: List[SplitEventsConstraint], prefer_resources_constraint: List[PreferResourcesConstraint], prefer_times_constraint: List[PreferTimesConstraint], spread_events_constraint: List[Constraint], avoid_clashes_constraint: AvoidClashesConstraint) -> None:
        self.assign_resource_constraint = assign_resource_constraint
        self.assign_time_constraint = assign_time_constraint
        self.split_events_constraint = split_events_constraint
        self.prefer_resources_constraint = prefer_resources_constraint
        self.prefer_times_constraint = prefer_times_constraint
        self.spread_events_constraint = spread_events_constraint
        self.avoid_clashes_constraint = avoid_clashes_constraint

