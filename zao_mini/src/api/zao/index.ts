import request from '@/axios'
import type { ZaoLogType } from './types'

export const logPostApi = (data: ZaoLogType): Promise<IResponse> => {
  return request.post({ url: '/flask/log/post', data })
}
