from enum import Enum
from typing import Optional, List, Union


class EventGroup:
    reference: str

    def __init__(self, reference: str) -> None:
        self.reference = reference


class PurpleEventGroups:
    event_group: EventGroup

    def __init__(self, event_group: EventGroup) -> None:
        self.event_group = event_group


class AssignTimeConstraintAppliesTo:
    event_groups: PurpleEventGroups

    def __init__(self, event_groups: PurpleEventGroups) -> None:
        self.event_groups = event_groups


class CostFunction(Enum):
    LINEAR = "Linear"


class AssignTimeConstraintTimeGroups:
    time_group: EventGroup

    def __init__(self, time_group: EventGroup) -> None:
        self.time_group = time_group


class Constraint:
    name: str
    required: bool
    weight: int
    cost_function: CostFunction
    applies_to: AssignTimeConstraintAppliesTo
    id: str
    time_groups: Optional[AssignTimeConstraintTimeGroups]
    duration: Optional[int]

    def __init__(self, name: str, required: bool, weight: int, cost_function: CostFunction, applies_to: AssignTimeConstraintAppliesTo, id: str, time_groups: Optional[AssignTimeConstraintTimeGroups], duration: Optional[int]) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.id = id
        self.time_groups = time_groups
        self.duration = duration


class PurpleResourceGroups:
    resource_group: List[EventGroup]

    def __init__(self, resource_group: List[EventGroup]) -> None:
        self.resource_group = resource_group


class AvoidClashesConstraintAppliesTo:
    resource_groups: PurpleResourceGroups

    def __init__(self, resource_groups: PurpleResourceGroups) -> None:
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


class Resources:
    resource: Union[List[EventGroup], EventGroup]

    def __init__(self, resource: Union[List[EventGroup], EventGroup]) -> None:
        self.resource = resource


class AvoidUnavailableTimesConstraintAppliesTo:
    resources: Resources

    def __init__(self, resources: Resources) -> None:
        self.resources = resources


class Times:
    time: Union[List[EventGroup], EventGroup]

    def __init__(self, time: Union[List[EventGroup], EventGroup]) -> None:
        self.time = time


class AvoidUnavailableTimesConstraint:
    name: str
    required: bool
    weight: int
    cost_function: CostFunction
    applies_to: AvoidUnavailableTimesConstraintAppliesTo
    times: Times
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: CostFunction, applies_to: AvoidUnavailableTimesConstraintAppliesTo, times: Times, id: str) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.times = times
        self.id = id


class FluffyResourceGroups:
    resource_group: EventGroup

    def __init__(self, resource_group: EventGroup) -> None:
        self.resource_group = resource_group


class LimitBusyTimesConstraintAppliesTo:
    resource_groups: Optional[FluffyResourceGroups]
    resources: Optional[Resources]

    def __init__(self, resource_groups: Optional[FluffyResourceGroups], resources: Optional[Resources]) -> None:
        self.resource_groups = resource_groups
        self.resources = resources


class LimitBusyTimesConstraintTimeGroups:
    time_group: Union[List[EventGroup], EventGroup]

    def __init__(self, time_group: Union[List[EventGroup], EventGroup]) -> None:
        self.time_group = time_group


class LimitBusyTimesConstraint:
    name: str
    required: bool
    weight: int
    cost_function: CostFunction
    applies_to: LimitBusyTimesConstraintAppliesTo
    time_groups: LimitBusyTimesConstraintTimeGroups
    minimum: int
    maximum: int
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: CostFunction, applies_to: LimitBusyTimesConstraintAppliesTo, time_groups: LimitBusyTimesConstraintTimeGroups, minimum: int, maximum: int, id: str) -> None:
        self.name = name
        self.required = required
        self.weight = weight
        self.cost_function = cost_function
        self.applies_to = applies_to
        self.time_groups = time_groups
        self.minimum = minimum
        self.maximum = maximum
        self.id = id


class LimitIdleTimesConstraintAppliesTo:
    resource_groups: FluffyResourceGroups

    def __init__(self, resource_groups: FluffyResourceGroups) -> None:
        self.resource_groups = resource_groups


class LimitIdleTimesConstraintTimeGroups:
    time_group: List[EventGroup]

    def __init__(self, time_group: List[EventGroup]) -> None:
        self.time_group = time_group


class LimitIdleTimesConstraint:
    name: str
    required: bool
    weight: int
    cost_function: CostFunction
    applies_to: LimitIdleTimesConstraintAppliesTo
    time_groups: LimitIdleTimesConstraintTimeGroups
    minimum: int
    maximum: int
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: CostFunction, applies_to: LimitIdleTimesConstraintAppliesTo, time_groups: LimitIdleTimesConstraintTimeGroups, minimum: int, maximum: int, id: str) -> None:
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
    cost_function: CostFunction
    applies_to: AssignTimeConstraintAppliesTo
    minimum_duration: int
    maximum_duration: int
    minimum_amount: int
    maximum_amount: int
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: CostFunction, applies_to: AssignTimeConstraintAppliesTo, minimum_duration: int, maximum_duration: int, minimum_amount: int, maximum_amount: int, id: str) -> None:
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


class FluffyEventGroups:
    event_group: Union[List[EventGroup], EventGroup]

    def __init__(self, event_group: Union[List[EventGroup], EventGroup]) -> None:
        self.event_group = event_group


class SpreadEventsConstraintAppliesTo:
    event_groups: FluffyEventGroups

    def __init__(self, event_groups: FluffyEventGroups) -> None:
        self.event_groups = event_groups


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
    cost_function: CostFunction
    applies_to: SpreadEventsConstraintAppliesTo
    time_groups: SpreadEventsConstraintTimeGroups
    id: str

    def __init__(self, name: str, required: bool, weight: int, cost_function: CostFunction, applies_to: SpreadEventsConstraintAppliesTo, time_groups: SpreadEventsConstraintTimeGroups, id: str) -> None:
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
    prefer_times_constraint: Constraint
    spread_events_constraint: List[SpreadEventsConstraint]
    link_events_constraint: Constraint
    avoid_clashes_constraint: AvoidClashesConstraint
    avoid_unavailable_times_constraint: List[AvoidUnavailableTimesConstraint]
    limit_idle_times_constraint: LimitIdleTimesConstraint
    limit_busy_times_constraint: List[LimitBusyTimesConstraint]

    def __init__(self, assign_time_constraint: Constraint, split_events_constraint: SplitEventsConstraint, prefer_times_constraint: Constraint, spread_events_constraint: List[SpreadEventsConstraint], link_events_constraint: Constraint, avoid_clashes_constraint: AvoidClashesConstraint, avoid_unavailable_times_constraint: List[AvoidUnavailableTimesConstraint], limit_idle_times_constraint: LimitIdleTimesConstraint, limit_busy_times_constraint: List[LimitBusyTimesConstraint]) -> None:
        self.assign_time_constraint = assign_time_constraint
        self.split_events_constraint = split_events_constraint
        self.prefer_times_constraint = prefer_times_constraint
        self.spread_events_constraint = spread_events_constraint
        self.link_events_constraint = link_events_constraint
        self.avoid_clashes_constraint = avoid_clashes_constraint
        self.avoid_unavailable_times_constraint = avoid_unavailable_times_constraint
        self.limit_idle_times_constraint = limit_idle_times_constraint
        self.limit_busy_times_constraint = limit_busy_times_constraint


