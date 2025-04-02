<script setup lang="ts">
import { ContentWrap } from '@/components/ContentWrap'
import { useI18n } from '@/hooks/web/useI18n'
import { ref } from 'vue'
import { ZaoLogType } from '@/api/zao/types'
import { logPostApi } from '@/api/zao'
import { ElButton, ElInput, ElText } from 'element-plus'

defineOptions({
  name: 'Menu111'
})

const { t } = useI18n()

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
