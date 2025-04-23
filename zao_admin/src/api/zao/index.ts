import request from '@/axios'
import type { ZaoLogType } from './types'

export const logPostApi = (data: ZaoLogType): Promise<IResponse> => {
  return request.post({ url: '/flask/log/post', data })
}

export const saveTableApi = (data: Partial<ZaoLogType>): Promise<IResponse> => {
  return request.post({ url: '/flask/log/update', data })
}

export const delTableListApi = (ids: string[] | number[]): Promise<IResponse> => {
  return request.post({ url: '/flask/log/delete', data: { ids } })
}

export const getTableListApi = (params: any) => {
  return request.get({ url: '/flask/log/list', params })
}
