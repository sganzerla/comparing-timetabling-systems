from enum import Enum
from typing import List, Union, Optional


class Reference(Enum):
    DAY_0 = "Day_0"
    DAY_1 = "Day_1"
    DAY_2 = "Day_2"
    DAY_3 = "Day_3"
    DAY_4 = "Day_4"
    GR_TIMES_DURATION_FOUR = "gr_TimesDurationFour"
    GR_TIMES_DURATION_THREE = "gr_TimesDurationThree"
    GR_TIMES_DURATION_TWO = "gr_TimesDurationTwo"


class TimeDay:
    reference: Reference

    def __init__(self, reference: Reference) -> None:
        self.reference = reference


class TimeTimeGroups:
    time_group: Union[List[TimeDay], TimeDay]

    def __init__(self, time_group: Union[List[TimeDay], TimeDay]) -> None:
        self.time_group = time_group


class Time:
    name: str
    day: TimeDay
    time_groups: Optional[TimeTimeGroups]
    id: str

    def __init__(self, name: str, day: TimeDay, time_groups: Optional[TimeTimeGroups], id: str) -> None:
        self.name = name
        self.day = day
        self.time_groups = time_groups
        self.id = id


class TimeGroupsDay:
    name: str
    id: Reference

    def __init__(self, name: str, id: Reference) -> None:
        self.name = name
        self.id = id


class TimesTimeGroups:
    day: List[TimeGroupsDay]
    time_group: List[TimeGroupsDay]

    def __init__(self, day: List[TimeGroupsDay], time_group: List[TimeGroupsDay]) -> None:
        self.day = day
        self.time_group = time_group


class Times:
    time_groups: TimesTimeGroups
    time: List[Time]

    def __init__(self, time_groups: TimesTimeGroups, time: List[Time]) -> None:
        self.time_groups = time_groups
        self.time = time

