<!-- BeforeInterview.vue -->
<template>
  <div class="profile-page">
    <main class="main-content">
      <el-tabs v-model="activeTab">
        <!-- 简历资料 -->
        <el-tab-pane name="resume">
          <template #label>
            <el-icon style="margin-right: 5px;"><Document /></el-icon>
            简历资料
          </template>
          <ResumeSection />
        </el-tab-pane>

        <el-tab-pane name="analysis">
          <template #label>
            <el-icon style="margin-right: 5px;"><DataAnalysis /></el-icon>
            能力分析
          </template>
          <SkillAnalysis />
        </el-tab-pane>

        <el-tab-pane name="jobs">
        <template #label>
          <el-icon style="margin-right: 5px;"><Briefcase /></el-icon>
          岗位推荐
        </template>
           <JobRecommendation />
        </el-tab-pane>

        <el-tab-pane name="questions">
        <template #label>
          <el-icon style="margin-right: 5px;"><EditPen /></el-icon>
          题库展示
        </template>
            <QuestionBank />
        </el-tab-pane>

        <el-tab-pane name="test">
        <template #label>
          <el-icon style="margin-right: 5px;"><Notebook /></el-icon>
          学习测试
        </template>
            <LearningTest />
        </el-tab-pane>
      </el-tabs>

    </main>
  </div>
</template>

<script setup>

import { ref } from 'vue'
import ResumeSection from '../components/ResumeSection.vue'
import SkillAnalysis from '../components/SkillAnalysis.vue'
import QuestionBank from '../components/QuestionBank.vue'
import JobRecommendation from '../components/JobRecommendation.vue'
import LearningTest from '../components/LearningTest.vue'

//图标导入
import { Document, DataAnalysis, Briefcase, EditPen, Notebook } from '@element-plus/icons-vue'

const dialogVisible = ref(false)
const activeTab = ref('resume') // 当前选中的
</script>

<style scoped>
/* 页面整体布局：使用 flex 实现左右结构，全高，设置背景和字体 */
.profile-page {
  height: 100vh; /* 视口高度 100% */
  background: #f0f2f5; /* 整体背景色 */
  font-family: 'Helvetica Neue', sans-serif; /* 使用 Helvetica 字体 */
}

/* 主内容区域样式 */
.main-content {
  flex: 1; /* 占据剩余所有空间 */
  padding: 24px; /* 内边距 */
  background: #f9fafc; /* 背景色与侧边栏一致 */
  min-width: 0; /* 允许 flex 子项收缩防止溢出 */
}

/* Tabs 区域样式 */
.el-tabs {
  background: #fff;
  border-radius: 12px; /* 圆角 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04); /* 阴影 */
  padding: 16px; /* 内边距 */
}

/* 深度选择器：Tab 项通用样式 */
::v-deep(.el-tabs__item) {
  font-family: 'Microsoft YaHei', sans-serif;
  font-size: 18px;
  font-weight: 600;
  color: #333;
  padding: 10px 20px;
  transition: all 0.3s ease;
}

/* 深度选择器：激活状态的 Tab 项 */
::v-deep(.el-tabs__item.is-active) {
  color: #409EFF; /* 激活色 */
  border-bottom: 2px solid #409EFF; /* 激活下划线 */
}
</style>

