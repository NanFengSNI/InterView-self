<template>
  <el-card class="user-profile" shadow="hover" v-if="user">
    <!-- 基本信息 -->
    <section class="section">
      <h2>基本信息</h2>
      <el-descriptions :column="2" border>
        <el-descriptions-item label="姓名">{{ user.name }}</el-descriptions-item>
        <el-descriptions-item label="性别">{{ user.gender }}</el-descriptions-item>
        <el-descriptions-item label="电话">{{ user.phone }}</el-descriptions-item>
        <el-descriptions-item label="邮箱">{{ user.email }}</el-descriptions-item>
        <el-descriptions-item label="意向岗位">{{ user.wannajob }}</el-descriptions-item>
        <el-descriptions-item label="意向公司">{{ user.wannafirm }}</el-descriptions-item>
        <el-descriptions-item label="技能">
          <el-tag v-for="(skill, i) in user.skills" :key="i" type="success" class="tag">{{ skill }}</el-tag>
        </el-descriptions-item>
      </el-descriptions>
    </section>

    <!-- 教育经历 -->
    <section class="section">
      <h2>教育经历</h2>
      <el-timeline>
        <el-timeline-item
          v-for="(edu, index) in user.education"
          :key="index"
          :timestamp="edu.date"
          placement="top"
        >
          <p><strong>{{ edu.school }}</strong> - {{ edu.degree }}（{{ edu.major }}）</p>
          <p>GPA: {{ edu.gpa }}</p>
        </el-timeline-item>
      </el-timeline>
    </section>

    <!-- 项目经历 -->
    <section class="section">
      <h2>项目经历</h2>
      <el-collapse>
        <el-collapse-item
          v-for="(proj, index) in user.projects"
          :key="index"
          :title="proj.name + '（' + proj.role + '）'"
        >
          <p><strong>时间：</strong>{{ proj.date }}</p>
          <p><strong>描述：</strong>{{ proj.description }}</p>
        </el-collapse-item>
      </el-collapse>
    </section>

    <!-- 工作经历 -->
    <section class="section">
      <h2>工作经历</h2>
      <el-collapse>
        <el-collapse-item
          v-for="(job, index) in user.experience"
          :key="index"
          :title="job.company + '（' + job.position + '）'"
        >
          <p><strong>时间：</strong>{{ job.date }}</p>
          <p><strong>描述：</strong>{{ job.description }}</p>
        </el-collapse-item>
      </el-collapse>
    </section>

    <!-- 其他信息 -->
    <section class="section">
      <h2>其他信息</h2>
      <el-descriptions :column="1" border>
        <el-descriptions-item label="语言能力">
          {{ user.languages }}
        </el-descriptions-item>
        <el-descriptions-item label="自我评价">
          {{ user.bio }}
        </el-descriptions-item>
      </el-descriptions>
    </section>
  </el-card>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const user = ref(null)

onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/api/user-profile')
    user.value = res.data
  } catch (error) {
    console.error('获取用户信息失败:', error)
  }
})
</script>


<style scoped>
.user-profile {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

.section {
  margin-bottom: 40px;
}

.tag {
  margin: 5px 5px 0 0;
}
</style>
