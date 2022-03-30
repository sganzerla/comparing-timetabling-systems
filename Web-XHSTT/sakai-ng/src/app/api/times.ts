export interface Times {
    TimeGroups: TimeGroups
    Time: Time[]
  }

  export interface TimeGroups {
    Day: Day[]
    TimeGroup: TimeGroup
  }

  export interface Day {
    "@Id": string
    Name: string
  }

  export interface TimeGroup {
    "@Id": string
    Name: string
  }

  export interface Time {
    "@Id": string
    Name: string
    Day: Day2
    TimeGroups: any
  }

  export interface Day2 {
    "@Reference": string
  }
