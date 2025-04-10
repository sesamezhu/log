import request from '@/axios'
import type { ZaoLogType } from './types'

export const logPostApi = (data: ZaoLogType): Promise<IResponse> => {
  return request.post({ url: '/flask/log/post', data })
}

export const saveTableApi = (data: Partial<ZaoLogType>): Promise<IResponse> => {
  return request.post({ url: '/flask/log/update', data })
}

function pad(num: number) {
  return num.toString().padStart(2, '0')
}

export const zao_format_dt = (now: Date): string => {
  return `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}T${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`
}

export const delTableListApi = (ids: string[] | number[]): Promise<IResponse> => {
  return request.post({ url: '/flask/log/delete', data: { ids } })
}

export const getTableListApi = (params: any) => {
  return request.get({ url: '/flask/log/list', params })
}
