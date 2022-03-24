from typing import List, Union


class TimeDay:
    reference: str

    def __init__(self, reference: str) -> None:
        self.reference = reference


class TimeTimeGroups:
    time_group: Union[List[TimeDay], TimeDay]

    def __init__(self, time_group: Union[List[TimeDay], TimeDay]) -> None:
        self.time_group = time_group


class Time:
    name: str
    day: TimeDay
    time_groups: TimeTimeGroups
    id: str

    def __init__(self, name: str, day: TimeDay, time_groups: TimeTimeGroups, id: str) -> None:
        self.name = name
        self.day = day
        self.time_groups = time_groups
        self.id = id


class TimeGroupsDay:
    name: str
    id: str

    def __init__(self, name: str, id: str) -> None:
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


