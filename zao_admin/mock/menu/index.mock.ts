import Mock from 'mockjs'
import { SUCCESS_CODE } from '@/constants'

const timeout = 1000

export default [
  {
    url: '/mock/menu/zao',
    method: 'get',
    timeout,
    response: () => {
      return {
        code: SUCCESS_CODE,
        data: {
          list: [
            {
              path: '/zao',
              component: '#',
              meta: {
                title: 'log',
                icon: 'vi-clarity:document-solid'
              },
              name: 'zao',
              status: Mock.Random.integer(0, 1),
              id: 4,
              type: 0,
              parentId: undefined,
              title: 'log',
              children: [
                {
                  path: 'log',
                  name: 'log',
                  status: Mock.Random.integer(0, 1),
                  id: 5,
                  type: 1,
                  parentId: 4,
                  title: 'log',
                  meta: {
                    title: 'log'
                  }
                }
              ]
            }
          ]
        }
      }
    }
  },
  // 列表接口
  {
    url: '/mock/menu/list',
    method: 'get',
    timeout,
    response: () => {
      return {
        code: SUCCESS_CODE,
        data: {
          list: [
            {
              path: '/dashboard',
              component: '#',
              redirect: '/dashboard/analysis',
              name: 'Dashboard',
              status: Mock.Random.integer(0, 1),
              id: 1,
              type: 0,
              parentId: undefined,
              title: '首页',
              meta: {
                title: '首页',
                icon: 'vi-ant-design:dashboard-filled',
                alwaysShow: true
              },
              children: [
                {
                  path: 'analysis',
                  component: 'views/Dashboard/Analysis',
                  name: 'Analysis',
                  status: Mock.Random.integer(0, 1),
                  id: 2,
                  type: 1,
                  parentId: 1,
                  title: '分析页',
                  permissionList: [
                    {
                      id: 1,
                      label: '新增',
                      value: 'add'
                    },
                    {
                      id: 2,
                      label: '编辑',
                      value: 'edit'
                    }
                  ],
                  meta: {
                    title: '分析页',
                    noCache: true,
                    permission: ['add', 'edit']
                  }
                },
                {
                  path: 'workplace',
                  component: 'views/Dashboard/Workplace',
                  name: 'Workplace',
                  status: Mock.Random.integer(0, 1),
                  id: 3,
                  type: 1,
                  parentId: 1,
                  title: '工作台',
                  permissionList: [
                    {
                      id: 1,
                      label: '新增',
                      value: 'add'
                    },
                    {
                      id: 2,
                      label: '编辑',
                      value: 'edit'
                    },
                    {
                      id: 3,
                      label: '删除',
                      value: 'delete'
                    }
                  ],
                  meta: {
                    title: '工作台',
                    noCache: true
                  }
                }
              ]
            },
            {
              path: '/zao',
              component: '#',
              meta: {
                title: 'log',
                icon: 'vi-clarity:document-solid'
              },
              name: 'zao',
              status: Mock.Random.integer(0, 1),
              id: 4,
              type: 0,
              parentId: undefined,
              title: 'log',
              children: [
                {
                  path: 'log',
                  name: 'log',
                  status: Mock.Random.integer(0, 1),
                  id: 5,
                  type: 1,
                  parentId: 4,
                  title: 'log',
                  meta: {
                    title: 'log'
                  }
                }
              ]
            }
          ]
        }
      }
    }
  }
]
