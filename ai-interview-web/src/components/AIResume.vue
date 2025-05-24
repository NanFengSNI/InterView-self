<template>
  <div style="display: flex; height: 100vh;">
    <!-- 左侧卡片容器 -->
    <div class="card-container">
      <div class="card-wrapper">

        <!--基础信息 -->
        <experience-section
          title="🏢 USER INFO"
          :list="infoList"
          :margin-top="'0px'"
          :showHeader="false"
          :show-add-button="false"
        >
        <template #default="{ item }">
          <div v-if="!item.hidden" class="experience-form">
            <div class="form-group">
              <label>姓名</label>
              <el-input v-model="item.name" />
            </div>

            <div class="form-row">
              <div class="form-group">
                <label>电话号码</label>
                <el-input v-model="item.phone" />
              </div>
              <div class="form-group">
                <label>邮箱</label>
                <el-input v-model="item.email" />
              </div>
            </div>
          </div>
        </template>
        </experience-section>

        <!-- 教育经历 -->
        <experience-section
          title="🎓 EDUCATION"
          :list="educationList"
          @add="addEducation"
          @remove="removeEducation"
          @move-up="moveUpEducation"
        >
          <template #default="{ item }">
            <div v-if="!item.hidden" class="experience-form">
              <div class="form-group">
                <label>学校</label>
                <el-input v-model="item.school" />
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label>学位 & 专业</label>
                  <el-input v-model="item.degree" />
                </div>
                <div class="form-group">
                  <label>日期</label>
                  <el-input v-model="item.date" />
                </div>
              </div>

              <div class="form-group">
                <label>GPA</label>
                <el-input v-model="item.gpa" />
              </div>
            </div>
          </template>
        </experience-section>

        <!-- 项目经历 -->
        <experience-section
          title="💡 PROJECT EXPERIENCE"
          :list="projectList"
          @add="addProject"
          @remove="removeProject"
          @move-up="moveUpProject"
        >
          <template #default="{ item }">
            <div v-if="!item.hidden" class="experience-form">
              <div class="form-group">
                <label>项目名称</label>
                <el-input v-model="item.name" />
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label>角色</label>
                  <el-input v-model="item.role" />
                </div>
                <div class="form-group">
                  <label>日期</label>
                  <el-input v-model="item.date" />
                </div>
              </div>

              <div class="form-group">
                <label>描述</label>
                <el-input :autosize="true" type="textarea" v-model="item.description" />
              </div>
            </div>
          </template>
        </experience-section>

        <!-- 工作经历 -->
        <experience-section
          title="🏢 WORK EXPERIENCE"
          :list="workList"
          @add="addWork"
          @remove="removeWork"
          @move-up="moveUpWork"
        >
        <template #default="{ item }">
          <div v-if="!item.hidden" class="experience-form">
            <div class="form-group">
              <label>公司</label>
              <el-input v-model="item.company" />
            </div>

            <div class="form-row">
              <div class="form-group">
                <label>职位</label>
                <el-input v-model="item.jobTitle" />
              </div>
              <div class="form-group">
                <label>日期</label>
                <el-input v-model="item.date" />
              </div>
            </div>

            <div class="form-group">
              <label>描述</label>
              <el-input :autosize="true" type="textarea" v-model="item.description" />
            </div>
          </div>
        </template>
        </experience-section>
      </div>
    </div>

    <!-- 页面右半 -->
    <div class="right-placeholder">
      <!-- 右上角按钮区域 -->
      <div class="top-button-bar">
        <el-button type="primary" @click="handleSave">保存</el-button>
        <el-button type="success" @click="handleDownload">下载 PDF</el-button>
      </div>
      <!-- PDF 预览区域 -->
      <div class="pdf-preview">
        <iframe
          :src="pdfUrl"
          width="100%"
          height="100%"
          frameborder="0"
        ></iframe>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ExperienceSection from '../components/ExperienceSection.vue'

// 用户信息
const infoList = ref([
  { id: 1, name: '', phone: '', email: '', description: '', hidden: false },
])

// 教育经历
const educationList = ref([
  { id: 1, school: '', degree: '', date: '', gpa: '', hidden: false },
])
const addEducation = () => {
  educationList.value.push({
    id: Date.now(),
    school: '',
    degree: '',
    date: '',
    gpa: '',
    hidden: false,
  })
}
const removeEducation = (index) => educationList.value.splice(index, 1)
const moveUpEducation = (index) => {
  if (index > 0) {
    const temp = educationList.value[index]
    educationList.value.splice(index, 1)
    educationList.value.splice(index - 1, 0, temp)
  }
}

// 工作经历
const workList = ref([
  { id: 1, company: '', title: '', date: '', description: '', hidden: false },
])
const addWork = () => {
  workList.value.push({
    id: Date.now(),
    company: '',
    title: '',
    date: '',
    description: '',
    hidden: false,
  })
}
const removeWork = (index) => workList.value.splice(index, 1)
const moveUpWork = (index) => {
  if (index > 0) {
    const temp = workList.value[index]
    workList.value.splice(index, 1)
    workList.value.splice(index - 1, 0, temp)
  }
}

// 项目经历
const projectList = ref([
  { id: 1, name: '', role: '', date: '', description: '', hidden: false },
])
const addProject = () => {
  projectList.value.push({
    id: Date.now(),
    name: '',
    role: '',
    date: '',
    description: '',
    hidden: false,
  })
}
const removeProject = (index) => projectList.value.splice(index, 1)
const moveUpProject = (index) => {
  if (index > 0) {
    const temp = projectList.value[index]
    projectList.value.splice(index, 1)
    projectList.value.splice(index - 1, 0, temp)
  }
}
</script>

<style>
.card-container {
  width: 40%;
  padding: 5px 5px; /* 上下20，左右16像素 */
  margin-left: 50px;   /* 页面左边界距离 */
  margin-right: 100px;  /* 与右侧区域的间距 */
  margin-top: 20px; /* 页面顶部距离 */
  margin-bottom: 80px; /* 页面底部距离 */
  overflow-y: auto;
  border-right: 1px solid #eee;
  background-color: #ffffff;
}

.card-wrapper {
  width: 100%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.right-placeholder {
  width: 50%;
  background-color: #fff;
}
.delete-icon {
  color: #999;
  cursor: pointer;
  margin-left: 8px;
}

.experience-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 16px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  font-family: 'Microsoft YaHei', sans-serif;
  margin-bottom: 5px;
  font-weight: 600;
  font-size: 16px;
}

.form-group .el-input:not(.el-textarea) .el-input__inner {
  height: 40px;
  padding: 5px 5px;
  font-size: 16px;
  font-weight: 400;
}

/* 设置 textarea 的样式，模拟接近 40px 高度的初始展示效果 */
.form-group .el-textarea__inner {
  padding: 5px 16px;
  font-size: 16px;
  font-weight: 400;
  line-height: 1.5;
  min-height: 40px !important; /* 初始高度一致 */
  resize: vertical; /* 可根据需要允许拉伸 */
}

.form-row {
  display: flex;
  gap: 20px;
}

.form-row .form-group {
  flex: 1;
}

.right-placeholder {
  width: 50%;
  background-color: #fff;
  padding: 10px 10px 10px 10px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.top-button-bar {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}

.pdf-preview {
  flex: 1;
  border: 1px solid #eee;
  margin-bottom: 70px;
  border-radius: 8px;
  overflow: auto;
}

</style>