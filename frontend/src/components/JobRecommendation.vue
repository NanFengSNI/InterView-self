<template>
  <div class="job-recommend-container">
    <!-- 筛选区域 -->
    <div class="filters">
      <el-select
        v-model="selectedCity"
        placeholder="选择城市"
        filterable
        style="width: 200px"
      >
        <el-option
          v-for="city in allCities"
          :key="city"
          :label="city"
          :value="city"
        />
      </el-select>

      <el-input-number
        v-model="salaryFilter.min"
        :min="0"
        :step="500"
        placeholder="最低薪资"
        style="width: 160px"
      />
      <el-input-number
        v-model="salaryFilter.max"
        :min="0"
        :step="500"
        placeholder="最高薪资"
        style="width: 160px"
      />
    </div>

    <div class="job-main">
      <!-- 岗位列表 -->
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

          <!-- 推荐值标签，卡片右下角 -->
          <div class="recommend-tag">
            <el-tag :style="getTagColorStyle(job.recommendScore)" effect="plain">
              推荐值：{{ job.recommendScore }}
            </el-tag>
          </div>
        </el-card>
      </div>

      <!-- 岗位详情 -->
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
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

const allCities = [/* 原城市数组保持不变 */]

const getTagColorStyle = (score) => {
  if (score >= 90) return { backgroundColor: '#3CB371', color: '#fff' }
  if (score >= 75) return { backgroundColor: '#20B2AA', color: '#fff' }
  if (score >= 60) return { backgroundColor: '#F6C343', color: '#fff' }
  if (score >= 45) return { backgroundColor: '#F56C6C', color: '#fff' }
  return { backgroundColor: '#909399', color: '#fff' }
}

const selectedCity = ref('')
const salaryFilter = ref({ min: null, max: null })
const jobList = ref([])
const selectedIndex = ref(0)

const selectedJob = computed(() => filteredJobs.value[selectedIndex.value])

const filteredJobs = computed(() => {
  return jobList.value
    .filter((job) => {
      const matchCity = selectedCity.value ? job.location.includes(selectedCity.value) : true
      const matchSalary =
        (!salaryFilter.value.min || job.salaryMax >= salaryFilter.value.min) &&
        (!salaryFilter.value.max || job.salaryMin <= salaryFilter.value.max)
      return matchCity && matchSalary
    })
    .sort((a, b) => b.recommendScore - a.recommendScore)
})

const selectJob = (index) => {
  selectedIndex.value = index
}

onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/api/job-recommendations')
    jobList.value = res.data
  } catch (err) {
    console.error('加载岗位列表失败:', err)
  }
})
</script>


<style scoped>
.recommend-tag {
  display: flex;
  justify-content: flex-end;
  margin-top: 0px;
}
.job-recommend-container {
  padding: 20px;
}
.filters {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-bottom: 16px;
  align-items: center;
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
  transition: all 0.3s ease;
  border-radius: 10px;
  border: 1px solid #e4e7ed;
}
.job-card:hover {
  transform: scale(1.02);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
}
.job-card.active {
  border: 2px solid #409eff;
  background-color: #f0f9ff;
}
.job-header {
  display: flex;
  justify-content: space-between;
  font-weight: 600;
  font-size: 16px;
}
.job-recommend-score {
  font-size: 13px;
  color: #f56c6c;
  margin-top: 4px;
}
.job-info,
.job-company {
  font-size: 13px;
  color: #666;
}
.job-detail {
  flex: 1;
  background: #fff;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
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
