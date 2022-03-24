from enum import Enum
from typing import Union, List


class ID(Enum):
    GR_FR = "gr_Fr"
    GR_MO = "gr_Mo"
    GR_TH = "gr_Th"
    GR_TIMES_DURATION_TWO = "gr_TimesDurationTwo"
    GR_TU = "gr_Tu"
    GR_WE = "gr_We"


class Day:
    reference: ID

    def __init__(self, reference: ID) -> None:
        self.reference = reference


class TimeGroupsTimeGroups:
    time_group: Day

    def __init__(self, time_group: Day) -> None:
        self.time_group = time_group


class Time:
    name: str
    day: Day
    time_groups: Union[TimeGroupsTimeGroups, str]
    id: str

    def __init__(self, name: str, day: Day, time_groups: Union[TimeGroupsTimeGroups, str], id: str) -> None:
        self.name = name
        self.day = day
        self.time_groups = time_groups
        self.id = id


class TimeGroup:
    name: str
    id: ID

    def __init__(self, name: str, id: ID) -> None:
        self.name = name
        self.id = id


class TimesTimeGroups:
    day: List[TimeGroup]
    time_group: TimeGroup

    def __init__(self, day: List[TimeGroup], time_group: TimeGroup) -> None:
        self.day = day
        self.time_group = time_group


class Times:
    time_groups: TimesTimeGroups
    time: List[Time]

    def __init__(self, time_groups: TimesTimeGroups, time: List[Time]) -> None:
        self.time_groups = time_groups
        self.time = time


