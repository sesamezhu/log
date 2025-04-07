<script setup lang="ts">
import { ContentWrap } from '@/components/ContentWrap'
import { ref } from 'vue'
import { ZaoLogType } from '@/api/zao/types'
import { logPostApi } from '@/api/zao'
import { ElInput, ElText, ElButton, ElSelect, ElOption } from 'element-plus'

defineOptions({
  name: 'Menu111'
})

const data = ref<ZaoLogType>({happened: new Date().toISOString(), text: 'haha' })

const options = ref([
  { value: '0', label: 'UNKNOWN' },
  { value: 'option2', label: 'Option 2' },
  { value: 'option3', label: 'Option 3' }
])
const selectedOption = ref(options.value[0].value)
</script>

<template>
  <ContentWrap>
    <div class="flex items-center">
      <ElText>happend {{ data.happened }}</ElText>
    </div>
    <div class="flex items-center">
      <ElText>text</ElText>
      <ElInput
        v-model="data.text"
        type="textarea"
        :autosize="{ minRows: 4, maxRows: 8 }"
        class="pl-20px w-full"
      />
    </div>
    <div class="flex items-center">
      <ElText>Select Option</ElText>
      <ElSelect v-model="selectedOption" placeholder="Select an option">
        <ElOption
          v-for="option in options"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        />
      </ElSelect>
    </div>
    <div class="flex items-center">
      <ElButton @click="logPostApi(data)">Log</ElButton>
    </div>
  </ContentWrap>
</template>
