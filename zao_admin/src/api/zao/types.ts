export type ZaoLogType = {
  id?: number
  created?: string
  updated?: string
  happened: string
  place?: string
  loggee?: string
  type?: string
  text?: string
  minutes: number
  logging?: string
  status?: number // 0 hidden 1 valid
}
