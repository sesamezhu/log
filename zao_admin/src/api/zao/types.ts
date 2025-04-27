export type ZaoYuanType = {
  id?: number
  created?: string
  updated?: string
  status?: number // 0 hidden 1 valid
}

export type ZaoLogType = ZaoYuanType & {
  happened: string
  place?: string
  loggee?: string
  type?: string
  text?: string
  minutes: number
  logging?: string
}

export type ZaoPeopleType = ZaoYuanType & {
  first: string
  last?: string
  nick?: string
  father?: number
  mother?: number
  mate?: number
  birth?: string
  death?: string
  gender?: number // 0 male 1 female
  phone?: string
  phone2?: string
  email?: string
  address?: string
  address2?: string
  work?: string
  z_relation?: string
  z_blood?: number
  text?: string
  children?: ZaoPeopleType[]
  mates?: ZaoMatesType[]
}

export type ZaoMatesType = {
  mate: ZaoPeopleType
  father: ZaoPeopleType
  mother: ZaoPeopleType
}

function pad(num: number) {
  return num.toString().padStart(2, '0')
}

export const zao_format_dt = (now: Date): string => {
  return `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}T${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`
}
