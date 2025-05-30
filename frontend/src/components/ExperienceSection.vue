<template>
  <el-card class="box-card" :style="{ marginTop }">
    <template #header>
        <span class="card-title">{{ title }}</span>
    </template>
    <div v-for="(item, index) in list" :key="item.id" class="experience-block">
      <!-- Header -->
      <div class="experience-header" v-if="showHeader">
        <div class="experience-title">
          {{ getOrdinal(index) }} 经历
        </div>
        <div>
          <el-button icon="ArrowUp" @click="$emit('move-up', index)" text circle />
          <el-button icon="View" @click="item.hidden = !item.hidden" text circle />
          <el-button icon="Delete" @click="$emit('remove', index)" text circle />
        </div>
      </div>

      <!-- 内容插槽 -->
      <slot :item="item"></slot>

      <div class="divider" v-if="index < list.length - 1"></div>
    </div>

    <el-button v-if="showAddButton" @click="$emit('add')" icon="Plus" class ="add-button">
      添加一段经历
    </el-button>
  </el-card>
</template>

<script setup>
import { Plus, ArrowUp, View, Delete } from '@element-plus/icons-vue'
defineProps({
  title: String,
  list: Array,
  showAddButton: {
    type: Boolean,
    default: true
  },
  showHeader: {
    type: Boolean,
    default: true
  },
   marginTop: {
    type: String,
    default: '20px'
  }
})
defineEmits(['add', 'remove', 'move-up'])

const getOrdinal = (i) => {
  const suffix = ['st', 'nd', 'rd']
  return `${i + 1}${suffix[i] || 'th'}`
}
</script>

<style scoped>
.box-card {
  border-radius: 8px;
}
.card-title {
  font-weight: bold;
  font-size: 18px;
}
.experience-block {
  margin-bottom: 20px;
}
.experience-header {
  display: flex;
  height: 15px;
  justify-content: space-between;
  align-items: center;
  background-color: #e4e8ec;
  padding: 8px 12px;
  margin-bottom: 15px;
  border-left: 4px solid #539cf0;
  font-weight: bold;
  font-size: 14px;
  border-radius: 4px;
}
.divider {
  border-top: 1px dashed #ccc;
  margin: 16px 0;
}
.add-button {
  margin-top: 10px;
  font-weight: bold;
  color:black
}
</style>
