export interface Events {
    EventGroups: EventGroups
    Event: Event[]
  }

  export interface EventGroups {
    Course: Course[]
    EventGroup: EventGroup
  }

  export interface Course {
    Id: string
    Name: string
  }

  export interface EventGroup {
    Id: string
    Name: string
  }

  export interface Event {
    Id: string
    Name: string
    Duration: string
    Course: Course2
    Resources: Resource[]
    EventGroups: EventGroups2
  }

  export interface Course2 {
    "@Reference": string
  }

  export interface Resource {
    "@Reference": string
    Role: string
    ResourceType: ResourceType
  }

  export interface ResourceType {
    "@Reference": string
  }

  export interface EventGroups2 {
    EventGroup: EventGroup2
  }

  export interface EventGroup2 {
    "@Reference": string
  }
