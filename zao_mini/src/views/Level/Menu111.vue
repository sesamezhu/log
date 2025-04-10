<script setup lang="ts">
import { ContentWrap } from '@/components/ContentWrap'
import { ref } from 'vue'
import { ZaoLogType } from '@/api/zao/types'
import { logPostApi, zao_format_dt } from '@/api/zao'
import { ElInput, ElText, ElButton, ElDatePicker } from 'element-plus'

defineOptions({
  name: 'Menu111'
})

const data = ref<ZaoLogType>({
  happened: zao_format_dt(new Date()),
  text: '',
  place: '',
  loggee: '',
  type: '',
  minutes: 0,
  logging: zao_format_dt(new Date())
})
</script>

<template>
  <ContentWrap>
    <div class="flex items-center mb-4">
      <ElText class="w-24 text-right pr-4">happened</ElText>
      <ElDatePicker
        v-model="data.happened"
        type="datetime"
        format="YYYY-MM-DD HH:mm:ss"
        value-format="YYYY-MM-DDTHH:mm:ss"
        placeholder="选择日期时间"
        class="ml-4"
      />
    </div>
    <div class="flex items-center mb-4">
      <ElText class="w-24 text-right pr-4">place</ElText>
      <ElInput v-model="data.place" type="text" placeholder="Enter place" class="w-full ml-4" />
    </div>
    <div class="flex items-center mb-4">
      <ElText class="w-24 text-right pr-4">loggee</ElText>
      <ElInput v-model="data.loggee" type="text" placeholder="Enter loggee" class="w-full ml-4" />
    </div>
    <div class="flex items-center mb-4">
      <ElText class="w-24 text-right pr-4">type</ElText>
      <ElInput v-model="data.type" type="text" placeholder="Enter type" class="w-full ml-4" />
    </div>
    <div class="flex items-center mb-4">
      <ElText class="w-24 text-right pr-4">text</ElText>
      <ElInput
        v-model="data.text"
        type="textarea"
        :autosize="{ minRows: 4, maxRows: 8 }"
        class="w-full ml-4"
      />
    </div>
    <div class="flex items-center mb-4">
      <ElText class="w-24 text-right pr-4">minutes</ElText>
      <ElInput
        v-model="data.minutes"
        type="number"
        placeholder="Enter minutes"
        class="w-full ml-4"
      />
    </div>
    <div class="flex items-center mb-4">
      <ElButton @click="logPostApi(data)" class="ml-28">Log</ElButton>
    </div>
  </ContentWrap>
  <ContentWrap />
</template>
