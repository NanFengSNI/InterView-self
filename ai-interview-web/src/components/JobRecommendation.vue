<template>
  <div class="job-recommend-container">
    <!-- 顶部筛选区域 -->
    <div class="filters">
      <el-select v-model="selectedCity" placeholder="选择城市" style="width: 150px">
        <el-option v-for="city in cityOptions" :key="city" :label="city" :value="city === '默认' ? '' : city" />
      </el-select>

      <el-select v-model="selectedSalaryRange" placeholder="薪资范围" style="width: 150px">
        <el-option v-for="range in salaryOptions" :key="range" :label="range" :value="range === '默认' ? '' : range" />
      </el-select>
    </div>

    <div class="job-main">
      <!-- 左侧岗位列表 -->
      <div class="job-list">
        <el-card
          v-for="(job, index) in filteredJobs"
          :key="index"
          class="job-card"
          @click="selectJob(index)"
          :class="{ active: selectedIndex === index }"
        >
          <div class="job-header">
            <div class="job-title">{{ job.title }}</div>
            <div class="job-salary">{{ job.salary }}</div>
          </div>
          <div class="job-info">
            <span>{{ job.experience }}</span> ·
            <span>{{ job.education }}</span> ·
            <span>{{ job.type }}</span>
          </div>
          <div class="job-company">{{ job.company }} · {{ job.location }}</div>
        </el-card>
      </div>

      <!-- 右侧详细信息 -->
      <div class="job-detail" v-if="selectedJob">
        <div class="detail-header">
          <h2>{{ selectedJob.title }} <span class="salary">{{ selectedJob.salary }}</span></h2>
          <p>{{ selectedJob.location }} · {{ selectedJob.experience }} · {{ selectedJob.education }}</p>
          <div class="tags">
            <el-tag v-for="tag in selectedJob.tags" :key="tag">{{ tag }}</el-tag>
          </div>
        </div>

        <div class="description">
          <h3>职位描述</h3>
          <p v-for="(d, i) in selectedJob.description" :key="i">{{ d }}</p>
          <h3>任职要求</h3>
          <p v-for="(r, i) in selectedJob.requirements" :key="i">{{ r }}</p>
        </div>

        <div class="recruiter">
          <el-avatar :src="selectedJob.recruiter.avatar" />
          <span>{{ selectedJob.recruiter.name }} · {{ selectedJob.recruiter.company }}</span>
        </div>

        <div class="location">
          <h3>工作地址</h3>
          <p>{{ selectedJob.address }}</p>
          <img :src="selectedJob.mapUrl" alt="map" class="map" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const selectedCity = ref('')
const selectedSalaryRange = ref('')

const cityOptions = ['默认', '成都', '北京', '上海']
const salaryOptions = ['默认', '8-12K', '15-30K', '18-35K']

const jobList = ref([
  {
    title: '二级水利建造师',
    salary: '18-19K',
    experience: '1-3年',
    education: '大专',
    type: '不限长期出差',
    company: '四川伟业建筑工程',
    location: '成都',
    tags: ['不限长期出差', '接受无水利工程师经验', '水利相关专业'],
    description: [
      '参与建筑工程项目的规划与执行，确保工程质量和进度；',
      '协调项目团队成员，解决工程过程中的技术问题；',
      '完成上级交办的其他相关工作。'
    ],
    requirements: [
      '持有二级建造师资格证书；',
      '具有良好的团队合作能力和沟通技巧；',
      '能够承担工作压力，具较强的责任心。'
    ],
    recruiter: {
      name: '廖先生',
      company: '四川伟业建筑工程',
      avatar: 'https://example.com/avatar.png'
    },
    address: '成都市华区北虫索府(动物园内)3',
    mapUrl: 'https://example.com/map.png'
  },
  {
    title: '软件开发工程师',
    salary: '18-35K',
    experience: '经验不限',
    education: '本科',
    type: '全职',
    company: '合见科技',
    location: '成都',
    tags: ['C++', '不限学历', '弹性工作'],
    description: [
      '参与公司软件产品的设计与开发；',
      '编写清晰、易维护的代码；',
      '协助产品团队实现业务功能。'
    ],
    requirements: [
      '计算机相关专业优先；',
      '熟练掌握 C++ 或 Python；',
      '有良好的团队沟通能力。'
    ],
    recruiter: {
      name: '李女士',
      company: '合见科技',
      avatar: 'https://example.com/avatar2.png'
    },
    address: '成都双流区',
    mapUrl: 'https://example.com/map2.png'
  },
  {
    title: '销售总监',
    salary: '15-30K',
    experience: '5-10年',
    education: '本科',
    type: '全职',
    company: '佳都科技',
    location: '北京',
    tags: ['销售管理', '商务谈判能力', '客户资源'],
    description: [
      '负责公司销售战略的制定与执行；',
      '带领销售团队完成季度目标；',
      '维护并拓展大客户资源。'
    ],
    requirements: [
      '具备5年以上销售管理经验；',
      '有行业客户资源者优先；',
      '沟通能力强，抗压能力好。'
    ],
    recruiter: {
      name: '王总',
      company: '佳都科技',
      avatar: 'https://example.com/avatar3.png'
    },
    address: '北京市海淀区',
    mapUrl: 'https://example.com/map3.png'
  }
])

const selectedIndex = ref(0)
const selectedJob = computed(() => filteredJobs.value[selectedIndex.value])

const filteredJobs = computed(() => {
  return jobList.value.filter((job) => {
    const matchCity = selectedCity.value ? job.location.includes(selectedCity.value) : true
    const matchSalary = selectedSalaryRange.value ? job.salary.includes(selectedSalaryRange.value) : true
    return matchCity && matchSalary
  })
})

const selectJob = (index) => {
  selectedIndex.value = index
}
</script>

<style scoped>
.job-recommend-container {
  padding: 20px;
}
.filters {
  display: flex;
  gap: 20px;
  margin-bottom: 16px;
}
.job-main {
  display: flex;
  gap: 24px;
}
.job-list {
  width: 35%;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.job-card {
  cursor: pointer;
  transition: 0.3s;
}
.job-card.active {
  border: 2px solid #409eff;
}
.job-detail {
  flex: 1;
  background: #fff;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.detail-header h2 {
  font-size: 20px;
}
.salary {
  color: #f56c6c;
  margin-left: 12px;
}
.tags {
  margin: 10px 0;
}
.description p {
  margin: 4px 0;
}
.recruiter {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 20px;
}
.map {
  width: 100%;
  max-width: 400px;
  margin-top: 12px;
  border-radius: 8px;
}
</style>
