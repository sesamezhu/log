<script setup lang="ts">
import { PropType, onMounted, ref } from 'vue'
import type { ZaoPeopleType } from '@/api/zao/types'
import { getPeopleTreeApi } from '@/api/zao/people'
import { canvas_draw } from '@/api/zao/people_canvas'
import { ElScrollbar } from 'element-plus'

const props = defineProps({
  currentRow: {
    type: Object as PropType<Nullable<ZaoPeopleType>>,
    default: () => null
  }
})
const treeRef = ref<ZaoPeopleType>()
const canvasRef = ref<HTMLCanvasElement | null>(null)
// 垂直滚动偏移量
const scrollOffset = ref(0)
// 横向滚动偏移量
const horizontalScrollOffset = ref(0)

const query_tree = async () => {
  const res = await getPeopleTreeApi(props.currentRow?.id || 999999)
  if (res) {
    treeRef.value = res.data
  }
}

const redrawCanvas = () => {
  if (!canvasRef.value || !treeRef.value) {
    return
  }
  const ctx = canvasRef.value.getContext('2d')
  if (ctx) {
    ctx.clearRect(0, 0, canvasRef.value.width, canvasRef.value.height)
    ctx.save()
    ctx.translate(-horizontalScrollOffset.value, -scrollOffset.value)
    canvas_draw(ctx, treeRef.value)
    ctx.restore()
  }
}

const handleVerticalScroll = (scrollTop: number) => {
  scrollOffset.value = scrollTop
  redrawCanvas()
}

const handleHorizontalScroll = (scrollLeft: number) => {
  horizontalScrollOffset.value = scrollLeft
  redrawCanvas()
}

onMounted(async () => {
  await query_tree()
  if (!canvasRef.value || !treeRef.value) {
    return
  }
  const ctx = canvasRef.value.getContext('2d')
  if (ctx) {
    canvas_draw(ctx, treeRef.value)
  }
})
</script>

<template>
  <div>
    <span>{{ currentRow?.last }}{{ currentRow?.first }}</span>
    <span>{{ currentRow?.nick }}</span>
  </div>
  <div style="width: 98%">
    <ElScrollbar
      height="400px"
      width="800px"
      @scroll-y="handleVerticalScroll"
      @scroll-x="handleHorizontalScroll"
    >
      <div style="width: 1600px; height: 1200px; position: relative">
        <canvas ref="canvasRef" width="1600" height="1200"></canvas>
      </div>
    </ElScrollbar>
  </div>
</template>
