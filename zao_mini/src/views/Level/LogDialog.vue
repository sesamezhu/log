<script setup lang="ts">
import { ContentWrap } from '@/components/ContentWrap'
import { Search } from '@/components/Search'
import { Dialog } from '@/components/Dialog'
import { useI18n } from '@/hooks/web/useI18n'
import { ElButton } from 'element-plus'
import { Table } from '@/components/Table'
import { getLogListApi, delLogListApi } from '@/api/zao'
import { useTable } from '@/hooks/web/useTable'
import { ZaoLogType } from '@/api/zao/types'
import { ref, unref, reactive } from 'vue'
// import EventWrite from './EventWrite.vue'
// import EventDetail from './EventDetail.vue'
import { CrudSchema, useCrudSchemas } from '@/hooks/web/useCrudSchemas'

defineOptions({
  name: 'menu1-3'
})

const ids = ref<string[]>([])

const { tableRegister, tableState, tableMethods } = useTable({
  fetchDataApi: async () => {
    const { currentPage, pageSize } = tableState
    const res = await getLogListApi({
      pageIndex: unref(currentPage),
      pageSize: unref(pageSize),
      ...unref(searchParams)
    })
    console.log('API响应数据:', res)
    return {
      list: res.data.list,
      total: res.data.total
    }
  },
  fetchDelApi: async () => {
    const res = await delLogListApi(unref(ids))
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

const { t } = useI18n()

const crudSchemas = reactive<CrudSchema[]>([
  {
    field: 'selection',
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
      type: 'selection'
    }
  },
  {
    field: 'index',
    label: t('tableDemo.index'),
    type: 'index',
    search: {
      hidden: true
    },
    form: {
      hidden: true
    },
    detail: {
      hidden: false
    }
  },
  {
    field: 'id',
    label: 'id',
    form: {
      hidden: true
    },
    search: {
      hidden: true
    }
  },
  {
    field: 'happened',
    label: 'happened',
    search: {
      component: 'Input'
    },
    detail: {
      span: 4
    },
    form: {
      component: 'DatePicker',
      componentProps: {
        type: 'datetime',
        valueFormat: 'YYYY-MM-DD HH:mm:ss'
      },
      hidden: true
    }
  },
  {
    field: 'place',
    label: 'place',
    search: {
      hidden: true
    }
  },
  {
    field: 'loggee',
    label: 'loggee',
    search: {
      hidden: false
    }
  },
  {
    field: 'type',
    label: 'type',
    search: {
      hidden: true
    }
  },
  {
    field: 'text',
    label: 'text',
    search: {
      hidden: true
    }
  },
  {
    field: 'minutes',
    label: 'minutes',
    search: {
      hidden: true
    }
  },
  {
    field: 'action',
    width: '260px',
    label: t('tableDemo.action'),
    search: {
      hidden: true
    },
    form: {
      hidden: true
    },
    detail: {
      hidden: true
    }
  }
])

// @ts-ignore
const { allSchemas } = useCrudSchemas(crudSchemas)

const dialogVisible = ref(false)
const dialogTitle = ref('')

const currentRow = ref<ZaoLogType | null>(null)
const actionType = ref('')

const AddAction = () => {
  dialogTitle.value = t('exampleDemo.add')
  currentRow.value = null
  dialogVisible.value = true
  actionType.value = ''
}

const delLoading = ref(false)

const delData = async (row: ZaoLogType | null) => {
  const elTableExpose = await getElTableExpose()
  ids.value = row ? [row.id] : elTableExpose?.getSelectionRows().map((v: ZaoLogType) => v.id) || []
  delLoading.value = true
  await delList(unref(ids).length).finally(() => {
    delLoading.value = false
  })
}

const saveLoading = ref(false)
</script>

<template>
  <ContentWrap>
    <div>LogDialog</div>
  </ContentWrap>
  <ContentWrap>
    <Search :schema="allSchemas.searchSchema" @search="setSearchParams" @reset="setSearchParams" />

    <div class="mb-10px">
      <ElButton type="primary" @click="AddAction">{{ t('exampleDemo.add') }}</ElButton>
      <ElButton :loading="delLoading" type="danger" @click="delData(null)">
        {{ t('exampleDemo.del') }}
      </ElButton>
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
    <template #footer>
      <ElButton v-if="actionType !== 'detail'" type="primary" :loading="saveLoading">
        {{ t('exampleDemo.save') }}
      </ElButton>
      <ElButton @click="dialogVisible = false">{{ t('dialogDemo.close') }}</ElButton>
    </template>
  </Dialog>
</template>
