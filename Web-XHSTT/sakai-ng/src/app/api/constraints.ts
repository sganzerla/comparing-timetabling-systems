export interface Constraints {
    AssignTimeConstraint: AssignTimeConstraint
    SplitEventsConstraint: SplitEventsConstraint
    DistributeSplitEventsConstraint: DistributeSplitEventsConstraint[]
    PreferTimesConstraint: PreferTimesConstraint
    SpreadEventsConstraint: SpreadEventsConstraint
    AvoidClashesConstraint: AvoidClashesConstraint
    AvoidUnavailableTimesConstraint: AvoidUnavailableTimesConstraint[]
    LimitIdleTimesConstraint: LimitIdleTimesConstraint
    ClusterBusyTimesConstraint: ClusterBusyTimesConstraint[]
  }

  export interface AssignTimeConstraint {
    Id: string
    Name: string
    Required: string
    Weight: string
    CostFunction: string
    AppliesTo: AppliesTo
  }

  export interface AppliesTo {
    EventGroups: EventGroups
  }

  export interface EventGroups {
    EventGroup: EventGroup
  }

  export interface EventGroup {
    "@Reference": string
  }

  export interface SplitEventsConstraint {
    Id: string
    Name: string
    Required: string
    Weight: string
    CostFunction: string
    AppliesTo: AppliesTo2
    MinimumDuration: string
    MaximumDuration: string
    MinimumAmount: string
    MaximumAmount: string
  }

  export interface AppliesTo2 {
    EventGroups: EventGroups2
  }

  export interface EventGroups2 {
    EventGroup: EventGroup2
  }

  export interface EventGroup2 {
    "@Reference": string
  }

  export interface DistributeSplitEventsConstraint {
    Id: string
    Name: string
    Required: string
    Weight: string
    CostFunction: string
    AppliesTo: AppliesTo3
    Duration: string
    Minimum: string
    Maximum: string
  }

  export interface AppliesTo3 {
    EventGroups: EventGroup3[]
  }

  export interface EventGroup3 {
    "@Reference": string
  }

  export interface PreferTimesConstraint {
    Id: string
    Name: string
    Required: string
    Weight: string
    CostFunction: string
    AppliesTo: AppliesTo4
    TimeGroups: TimeGroups
    Duration: string
  }

  export interface AppliesTo4 {
    EventGroups: EventGroups3
  }

  export interface EventGroups3 {
    EventGroup: EventGroup4
  }

  export interface EventGroup4 {
    "@Reference": string
  }

  export interface TimeGroups {
    TimeGroup: TimeGroup
  }

  export interface TimeGroup {
    "@Reference": string
  }

  export interface SpreadEventsConstraint {
    Id: string
    Name: string
    Required: string
    Weight: string
    CostFunction: string
    AppliesTo: AppliesTo5
    TimeGroups: TimeGroup2[]
  }

  export interface AppliesTo5 {
    EventGroups: EventGroup5[]
  }

  export interface EventGroup5 {
    "@Reference": string
  }

  export interface TimeGroup2 {
    "@Reference": string
    Minimum: string
    Maximum: string
  }

  export interface AvoidClashesConstraint {
    Id: string
    Name: string
    Required: string
    Weight: string
    CostFunction: string
    AppliesTo: AppliesTo6
  }

  export interface AppliesTo6 {
    ResourceGroups: ResourceGroup[]
  }

  export interface ResourceGroup {
    "@Reference": string
  }

  export interface AvoidUnavailableTimesConstraint {
    Id: string
    Name: string
    Required: string
    Weight: string
    CostFunction: string
    AppliesTo: AppliesTo7
    Times: Time[]
  }

  export interface AppliesTo7 {
    Resources: Resources
  }

  export interface Resources {
    Resource: Resource
  }

  export interface Resource {
    "@Reference": string
  }

  export interface Time {
    "@Reference": string
  }

  export interface LimitIdleTimesConstraint {
    Id: string
    Name: string
    Required: string
    Weight: string
    CostFunction: string
    AppliesTo: AppliesTo8
    TimeGroups: TimeGroup3[]
    Minimum: string
    Maximum: string
  }

  export interface AppliesTo8 {
    ResourceGroups: ResourceGroups
  }

  export interface ResourceGroups {
    ResourceGroup: ResourceGroup2
  }

  export interface ResourceGroup2 {
    "@Reference": string
  }

  export interface TimeGroup3 {
    "@Reference": string
  }

  export interface ClusterBusyTimesConstraint {
    Id: string
    Name: string
    Required: string
    Weight: string
    CostFunction: string
    AppliesTo: AppliesTo9
    TimeGroups: TimeGroup4[]
    Minimum: string
    Maximum: string
  }

  export interface AppliesTo9 {
    Resources: Resource2[]
  }

  export interface Resource2 {
    "@Reference": string
  }

  export interface TimeGroup4 {
    "@Reference": string
  }
