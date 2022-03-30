export interface Resources {
    ResourceTypes: ResourceType[]
    ResourceGroups: ResourceGroup[]
    Resource: Resource[]
  }

  export interface ResourceType {
    "@Id": string
    Name: string
  }

  export interface ResourceGroup {
    "@Id": string
    Name: string
    ResourceType: ResourceType2
  }

  export interface ResourceType2 {
    "@Reference": string
  }

  export interface Resource {
    "@Id": string
    Name: string
    ResourceType: ResourceType3
    ResourceGroups: ResourceGroups
  }

  export interface ResourceType3 {
    "@Reference": string
  }

  export interface ResourceGroups {
    ResourceGroup: ResourceGroup2
  }

  export interface ResourceGroup2 {
    "@Reference": string
  }
