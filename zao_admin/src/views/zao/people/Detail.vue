<script setup lang="ts">
import { PropType, onMounted, ref } from 'vue'
import type { ZaoPeopleType } from '@/api/zao/types'
import { Descriptions, DescriptionsSchema } from '@/components/Descriptions'
import { getPeopleTreeApi } from '@/api/zao/people'
import { canvas_draw } from '@/api/zao/people_canvas'

const props = defineProps({
  currentRow: {
    type: Object as PropType<Nullable<ZaoPeopleType>>,
    default: () => null
  },
  detailSchema: {
    type: Array as PropType<DescriptionsSchema[]>,
    default: () => []
  }
})
const treeRef = ref<ZaoPeopleType>()
const canvasRef = ref<HTMLCanvasElement | null>(null)

const query_tree = async () => {
  const res = await getPeopleTreeApi(props.currentRow?.id || 999999)
  if (res) {
    treeRef.value = res.data
  }
}

onMounted(async () => {
  await query_tree()
  if (!canvasRef.value || !treeRef.value) {
    return
  }
  const ctx = canvasRef.value?.getContext('2d')
  if (ctx) {
    canvas_draw(ctx, treeRef.value)
  }
})
</script>

<template>
  <Descriptions :schema="detailSchema" :data="currentRow || {}" />
  <div>
    <span>{{ currentRow?.last }}{{ currentRow?.first }}</span>
    <span>{{ currentRow?.nick }}</span>
  </div>
  <canvas ref="canvasRef" width="800" height="600"></canvas>
</template>
