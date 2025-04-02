<script setup lang="ts">
import { ContentWrap } from '@/components/ContentWrap'
import { ref } from 'vue'
import { ZaoLogType } from '@/api/zao/types'
import { logPostApi } from '@/api/zao'
import { ElInput, ElText, ElButton } from 'element-plus'

defineOptions({
  name: 'Menu111'
})

const data = ref<ZaoLogType>({ logTime: new Date().toISOString(), text: 'haha' })
</script>

<template>
  <ContentWrap>
    <div class="flex items-center">
      <ElText>logTime {{ data.logTime }}</ElText>
    </div>
    <div class="flex items-center">
      <ElText>text</ElText>
      <ElInput v-model="data.text" class="pl-20px" />
    </div>
    <div class="flex items-center">
      <ElButton @click="logPostApi(data)">Log</ElButton>
    </div>
  </ContentWrap>
</template>
