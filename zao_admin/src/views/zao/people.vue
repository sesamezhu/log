<script setup lang="tsx">
import { ContentWrap } from '@/components/ContentWrap'
import { Search } from '@/components/Search'
import { Dialog } from '@/components/Dialog'
import { Table } from '@/components/Table'
import { getTableListApi, saveTableApi, delTableListApi } from '@/api/zao/people'
import { useTable } from '@/hooks/web/useTable'
import { ZaoPeopleType } from '@/api/zao/types'
import { ref, unref, reactive } from 'vue'
import Write from './people/Write.vue'
import Detail from './people/Detail.vue'
import Blood from './people/Blood.vue'
import { CrudSchema, useCrudSchemas } from '@/hooks/web/useCrudSchemas'
import { BaseButton } from '@/components/Button'

const ids = ref<string[]>([])

const { tableRegister, tableState, tableMethods } = useTable({
  fetchDataApi: async () => {
    const { currentPage, pageSize } = tableState
    const res = await getTableListApi({
      pageIndex: unref(currentPage),
      pageSize: unref(pageSize),
      ...unref(searchParams)
    })
    return {
      list: res.data.list,
      total: res.data.total
    }
  },
  fetchDelApi: async () => {
    const res = await delTableListApi(unref(ids))
    return !!res
  }
})
const { loading, dataList, total, currentPage, pageSize } = tableState
const { getList, getElTableExpose, delList } = tableMethods

const searchParams = ref({})
const setSearchParams = (params: any) => {
  searchParams.value = params
  getList()
}

const crudSchemas = reactive<CrudSchema[]>([
  {
    field: 'id',
    label: 'id',
    width: '64px',
    search: {
      hidden: true
    },
    form: {
      hidden: true
    }
  },
  {
    field: 'last',
    label: 'last',
    search: {
      hidden: true
    }
  },
  {
    field: 'first',
    label: 'first'
  },
  {
    field: 'birth',
    label: 'birth',
    search: {
      hidden: true
    },
    form: {
      component: 'DatePicker',
      componentProps: {
        type: 'date',
        valueFormat: 'YYYY-MM-DD'
      }
    }
  },
  {
    field: 'nick',
    label: 'nick'
  },
  {
    field: 'father',
    label: 'father',
    hidden: true,
    search: {
      hidden: true
    }
  },
  {
    field: 'mother',
    label: 'mother',
    hidden: true,
    search: {
      hidden: true
    }
  },
  {
    field: 'mate',
    label: 'mate',
    hidden: true,
    search: {
      hidden: true
    }
  },
  {
    field: 'gender',
    label: 'gender',
    hidden: true,
    search: {
      hidden: true
    }
  },
  {
    field: 'phone',
    label: 'phone'
  },
  {
    field: 'phone2',
    label: 'phone2',
    hidden: true,
    search: {
      hidden: true
    }
  },
  {
    field: 'address',
    label: 'address',
    hidden: true,
    search: {
      hidden: true
    }
  },
  {
    field: 'address2',
    label: 'address2',
    hidden: true,
    search: {
      hidden: true
    }
  },
  {
    field: 'work',
    label: 'work',
    hidden: true,
    search: {
      hidden: true
    }
  },
  {
    field: 'z_relation',
    label: 'z_relation',
    hidden: true,
    search: {
      hidden: true
    }
  },
  {
    field: 'z_blood',
    label: 'z_blood',
    hidden: true,
    search: {
      hidden: true
    }
  },
  {
    field: 'death',
    label: 'death',
    hidden: true,
    form: {
      component: 'DatePicker',
      componentProps: {
        type: 'date',
        valueFormat: 'YYYY-MM-DD'
      }
    }
  },
  {
    field: 'text',
    label: 'text',
    width: '500px',
    search: {
      hidden: true
    },
    form: {
      component: 'Editor',
      colProps: {
        span: 24
      }
    },
    detail: {
      span: 24
    }
  },
  {
    field: 'action',
    width: '300px',
    label: 'Action',
    search: {
      hidden: true
    },
    form: {
      hidden: true
    },
    detail: {
      hidden: true
    },
    table: {
      slots: {
        default: (data: any) => {
          return (
            <>
              <BaseButton type="primary" onClick={() => action(data.row, 'edit')}>
                edit
              </BaseButton>
              <BaseButton type="success" onClick={() => action(data.row, 'detail')}>
                view
              </BaseButton>
              <BaseButton type="success" onClick={() => action(data.row, 'blood')}>
                graph
              </BaseButton>
              <BaseButton type="danger" onClick={() => delData(data.row)}>
                del
              </BaseButton>
            </>
          )
        }
      }
    }
  }
])

// @ts-ignore
const { allSchemas } = useCrudSchemas(crudSchemas)

const dialogVisible = ref(false)
const dialogTitle = ref('')

const currentRow = ref<ZaoPeopleType | null>(null)
const actionType = ref('')

const AddAction = () => {
  dialogTitle.value = 'add'
  currentRow.value = null
  dialogVisible.value = true
  actionType.value = ''
}

const delLoading = ref(false)

const delData = async (row: ZaoPeopleType | null) => {
  const elTableExpose = await getElTableExpose()
  ids.value = row
    ? [row.id]
    : elTableExpose?.getSelectionRows().map((v: ZaoPeopleType) => v.id) || []
  delLoading.value = true
  await delList(unref(ids).length).finally(() => {
    delLoading.value = false
  })
}

const action = (row: ZaoPeopleType, type: string) => {
  dialogTitle.value = type === 'edit' ? 'people.edit' : 'people.detail'
  actionType.value = type
  currentRow.value = row
  dialogVisible.value = true
}

const writeRef = ref<ComponentRef<typeof Write>>()

const saveLoading = ref(false)

const save = async () => {
  const write = unref(writeRef)
  const formData = await write?.submit()
  if (formData) {
    saveLoading.value = true
    const res = await saveTableApi(formData)
      .catch(() => {})
      .finally(() => {
        saveLoading.value = false
      })
    if (res) {
      dialogVisible.value = false
      currentPage.value = 1
      getList()
    }
  }
}
</script>

<template>
  <ContentWrap>
    <Search :schema="allSchemas.searchSchema" @search="setSearchParams" @reset="setSearchParams" />

    <div class="mb-10px">
      <BaseButton type="primary" @click="AddAction">add</BaseButton>
    </div>

    <Table
      v-model:pageSize="pageSize"
      v-model:currentPage="currentPage"
      :columns="allSchemas.tableColumns"
      :data="dataList"
      :loading="loading"
      :pagination="{
        total: total
      }"
      @register="tableRegister"
    />
  </ContentWrap>

  <Dialog v-model="dialogVisible" :title="dialogTitle">
    <Write
      v-if="actionType === 'edit'"
      ref="writeRef"
      :form-schema="allSchemas.formSchema"
      :current-row="currentRow"
    />
    <Detail
      v-if="actionType === 'detail'"
      :detail-schema="allSchemas.detailSchema"
      :current-row="currentRow"
    />
    <Blood v-if="actionType === 'blood'" :current-row="currentRow" />
    <template #footer>
      <BaseButton
        v-if="actionType === 'edit'"
        type="primary"
        :loading="saveLoading"
        @click="save"
      >
        save
      </BaseButton>
      <BaseButton @click="dialogVisible = false">close</BaseButton>
    </template>
  </Dialog>
</template>
