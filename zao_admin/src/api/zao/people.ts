import request from '@/axios'
import type { ZaoPeopleType } from './types'

export const logPostApi = (data: ZaoPeopleType): Promise<IResponse> => {
  return request.post({ url: '/flask/people/post', data })
}

export const saveTableApi = (data: Partial<ZaoPeopleType>): Promise<IResponse> => {
  return request.post({ url: '/flask/people/update', data })
}

export const delTableListApi = (ids: string[] | number[]): Promise<IResponse> => {
  return request.post({ url: '/flask/people/delete', data: { ids } })
}

export const getTableListApi = (params: any) => {
  return request.get({ url: '/flask/people/list', params })
}
