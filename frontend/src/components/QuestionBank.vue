<template>
  <div class="app-container">
    <main class="main-container container mx-auto py-6">
      <div class="flex flex-col lg:flex-row gap-6">
        <!-- 左侧分类导航 -->
        <div class="left-nav w-full lg:w-1/4 fixed-width-nav">
          <div class="bg-white rounded-lg shadow-sm p-4 sticky top-6">
            <h3 class="text-lg font-bold mb-4 text-dark">岗位分类</h3>
            <el-menu
              mode="vertical"
              :default-active="activeCategory"
              @select="handleCategorySelect"
              class="border-none"
            >
              <!-- 人工智能领域 -->
              <el-sub-menu index="ai">
                <template #title>
                  <el-icon><Menu /></el-icon>
                  <span>人工智能</span>
                </template>
                <el-menu-item index="ai-algorithm" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>人工智能算法工程师</span>
                </el-menu-item>
                <el-menu-item index="ai-data" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>人工智能数据工程师</span>
                </el-menu-item>
                <el-menu-item index="ai-dev" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>人工智能开发工程师</span>
                </el-menu-item>
                <el-menu-item index="ai-research" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>人工智能研究员</span>
                </el-menu-item>
                <el-menu-item index="ai-product" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>人工智能产品经理</span>
                </el-menu-item>
              </el-sub-menu>

              <!-- 大数据领域 -->
              <el-sub-menu index="big-data">
                <template #title>
                  <el-icon><Menu /></el-icon>
                  <span>大数据</span>
                </template>
                <el-menu-item index="big-data-analyst" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>大数据分析师</span>
                </el-menu-item>
                <el-menu-item index="big-data-engineer" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>大数据工程师</span>
                </el-menu-item>
                <el-menu-item index="big-data-architect" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>大数据架构师</span>
                </el-menu-item>
                <el-menu-item index="big-data-mining" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>大数据挖掘工程师</span>
                </el-menu-item>
              </el-sub-menu>

              <!-- 物联网领域 -->
              <el-sub-menu index="iot">
                <template #title>
                  <el-icon><Menu /></el-icon>
                  <span>物联网</span>
                </template>
                <el-menu-item index="iot-dev" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>物联网开发工程师</span>
                </el-menu-item>
                <el-menu-item index="iot-sensor" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>物联网传感器工程师</span>
                </el-menu-item>
                <el-menu-item index="iot-security" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>物联网安全工程师</span>
                </el-menu-item>
                <el-menu-item index="iot-product" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>物联网产品经理</span>
                </el-menu-item>
              </el-sub-menu>

              <!-- 软件开发领域 -->
              <el-sub-menu index="software-dev">
                <template #title>
                  <el-icon><Menu /></el-icon>
                  <span>软件开发</span>
                </template>
                <el-menu-item index="web-dev" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>Web开发工程师</span>
                </el-menu-item>
                <el-menu-item index="mobile-dev" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>移动开发工程师</span>
                </el-menu-item>
                <el-menu-item index="game-dev" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>游戏开发工程师</span>
                </el-menu-item>
                <el-menu-item index="software-test" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>软件测试工程师</span>
                </el-menu-item>
                <el-menu-item index="software-architect" class="px-3 py-2 rounded-md cursor-pointer flex items-center">
                  <el-icon><Menu /></el-icon>
                  <span>软件架构师</span>
                </el-menu-item>
              </el-sub-menu>
            </el-menu>
          </div>
        </div>

        <!-- 右侧题目列表 -->
        <div class="question-list w-full lg:w-3/4">
          <div class="bg-white rounded-lg shadow-sm p-6">
            <!-- 题目列表内容 -->
            <div class="flex flex-col md:flex-row md:items-center justify-between mb-6">
              <h2 class="text-xl font-bold text-dark">{{ titleText }}</h2>
              <div class="mt-2 md:mt-0 flex items-center space-x-3">
                <span class="count text-sm text-gray-500">共120道题</span>
                <el-select v-model="sortOption" placeholder="排序方式" class="w-36">
                  <el-option label="默认排序" value="default"></el-option>
                  <el-option label="题库难度" value="difficulty"></el-option>
                  <el-option label="最新添加" value="latest"></el-option>
                  <el-option label="题目数量" value="questionCount"></el-option>
                </el-select>
              </div>
            </div>

            <!-- 技术分类标签 -->
            <div class="mb-6">
              <div class="flex flex-wrap gap-2">
                <el-tag 
                  v-for="tech in techTags" 
                  :key="tech.id" 
                  :type="tech.type" 
                  class="cursor-pointer hover:opacity-90"
                  @click="scrollToTechSection(tech.id)"
                >
                  {{ tech.name }}
                </el-tag>
              </div>
            </div>

            <!-- 技术领域题库展示 -->
            <div class="space-y-8">
              <!-- 技术领域区域 -->
              <div 
                v-for="tech in techSections" 
                :key="tech.id" 
                :id="tech.id"
                class="tech-section"
              >
                <!-- 技术领域标题 -->
                <div class="flex items-center justify-between mb-4">
                  <h3 class="text-lg font-bold text-dark flex items-center">
                    <el-icon :class="tech.iconClass"></el-icon>
                    {{ tech.name }}
                  </h3>
                  <span class="text-sm text-gray-500">{{ tech.examCount }}套题</span>
                </div>

                <div class="relative">
                  <!-- 滚动控制按钮 -->
                  <el-button 
                    type="default" 
                    size="mini"
                    circle
                    class="absolute left-0 top-1/2 -translate-y-1/2 -translate-x-1/2 z-10 shadow-lg"
                    @click="scrollLeft(tech.id)"
                    :disabled="tech.scrollPosition <= 0"
                  >
                    <el-icon><ArrowLeft /></el-icon>
                  </el-button>

                  <!-- 题库卡片滚动区域 -->
                  <div class="overflow-x-auto hide-scrollbar pb-2">
                    <div 
                      :class="'flex space-x-4 min-w-max transition-transform duration-300'" 
                      :style="{ transform: `translateX(-${tech.scrollPosition}px)` }"
                      :ref="el => tech.scrollContainer = el"
                    >
                      <!-- 题库卡片 -->
                      <div 
                        v-for="(exam, index) in tech.exams" 
                        :key="index"
                        class="exam-card bg-white border border-gray-200 rounded-lg overflow-hidden hover:shadow-lg hover:-translate-y-1 transition-all duration-300 w-64"
                      >
                        <div class="p-5">
                          <h4 class="font-medium text-dark mb-3">{{ exam.title }}</h4>
                          <div class="flex items-center text-sm text-gray-500 mb-3">
                            <el-icon><Rank /></el-icon>
                            <span>{{ exam.questionCount }}题</span>
                          </div>
                          <div class="flex items-center text-sm text-gray-500">
                            <el-icon><Rank /></el-icon>
                            <span>{{ exam.updateDate }}</span>
                          </div>
                        </div>
                        <div class="bg-gray-50 p-3 border-t border-gray-100">
                          <div class="flex justify-between items-center">
                            <!-- 根据难度级别设置不同的背景颜色 -->
                            <span 
                              class="text-xs px-2 py-0.5 rounded-full text-white font-medium"
                               :class="{
                                  'bg-green-500': exam.difficulty === '初级',
                                  'bg-yellow-500': exam.difficulty === '中级',
                                  'bg-red-500': exam.difficulty === '高级'
                                }"
                            >
                              {{ exam.difficulty }}
                            </span>
                            <el-button 
                              type="text" 
                              size="mini"
                              class="text-primary hover:text-primary/80 p-0"
                              @click="viewExamDetails(exam)"
                            >
                              查看详情
                            </el-button>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- 滚动控制按钮 -->
                  <el-button 
                    type="default" 
                    size="mini"
                    circle
                    class="absolute right-0 top-1/2 -translate-y-1/2 translate-x-1/2 z-10 shadow-lg"
                    @click="scrollRight(tech.id)"
                    :disabled="tech.scrollPosition >= getMaxScroll(tech.id)"
                  >
                    <el-icon><ArrowRight /></el-icon>
                  </el-button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 右侧统计卡片 -->
        <div class="statistics-cards w-full lg:w-1/4">
          <div class="bg-white rounded-lg shadow-sm p-4 sticky top-6">
            <div class="statistic-card mb-4">
              <h4 class="text-lg font-bold text-dark">总题数</h4>
              <p class="text-xl text-gray-500">120</p>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, watch } from 'vue';
import { Rank, ArrowLeft, ArrowRight, Menu } from '@element-plus/icons-vue';
import axios from 'axios';

// 状态管理
const activeCategory = ref('dev');
const sortOption = ref('default');
const techTags = reactive([]);
const titleText = ref('');
const techSections = reactive([]);


// 监听排序选项变化
watch(sortOption, (newValue) => {
  techSections.forEach(section => {
    let sortedExams = [...section.exams];
    const difficultyMap = { '初级': 1, '中级': 2, '高级': 3 };
    switch (newValue) {
      case 'difficulty':
        sortedExams.sort((a, b) => difficultyMap[a.difficulty] - difficultyMap[b.difficulty]);
        break;
      case 'latest':
        sortedExams.sort((a, b) => new Date(b.updateDate) - new Date(a.updateDate));
        break;
      case 'questionCount':
        sortedExams.sort((a, b) => b.questionCount - a.questionCount);
        break;
      case 'default':
      default:
        sortedExams.sort((a, b) => a.title.localeCompare(b.title, 'zh-Hans'));
        break;
    }

    section.exams = sortedExams;
  });
});

const positionTitleMap = {
  'ai-algorithm': '人工智能算法工程师',
  'ai-data': '人工智能数据工程师',
  'ai-dev': '人工智能开发工程师',
  'ai-research': '人工智能研究员',
  'ai-product': '人工智能产品经理',
  'big-data-analyst': '大数据分析师',
  'big-data-engineer': '大数据工程师',
  'big-data-architect': '大数据架构师',
  'big-data-mining': '大数据挖掘工程师',
  'iot-dev': '物联网开发工程师',
  'iot-sensor': '物联网传感器工程师',
  'iot-security': '物联网安全工程师',
  'iot-product': '物联网产品经理',
  'web-dev': 'Web开发工程师',
  'mobile-dev': '移动开发工程师',
  'game-dev': '游戏开发工程师',
  'software-test': '软件测试工程师',
  'software-architect': '软件架构师'
};

// 处理岗位选择
const handleCategorySelect = async (value) => {
  activeCategory.value = value;
  titleText.value = positionTitleMap[value] + '题库';
  // 定义领域和岗位的映射
  const domainPositionMap = {
    'ai-algorithm': { domain: 'AI', position: 'AIAlgorithmEngineer' },
    'ai-data': { domain: 'AI', position: 'AIDataEngineer' },
    'ai-dev': { domain: 'AI', position: 'AIDevelopmentEngineer' },
    'ai-research': { domain: 'AI', position: 'AIResearcher' },
    'ai-product': { domain: 'AI', position: 'AIProductManager' },
    'big-data-analyst': { domain: 'BigData', position: 'BigDataAnalyst' },
    'big-data-engineer': { domain: 'BigData', position: 'BigDataEngineer' },
    'big-data-architect': { domain: 'BigData', position: 'BigDataArchitect' },
    'big-data-mining': { domain: 'BigData', position: 'BigDataMiningEngineer' },
    'iot-dev': { domain: 'IoT', position: 'IoTDevelopmentEngineer' },
    'iot-sensor': { domain: 'IoT', position: 'IoTSensorEngineer' },
    'iot-security': { domain: 'IoT', position: 'IoTSecurityEngineer' },
    'iot-product': { domain: 'IoT', position: 'IoTProductManager' },
    'web-dev': { domain: 'SoftwareDev', position: 'WebDevelopmentEngineer' },
    'mobile-dev': { domain: 'SoftwareDev', position: 'MobileDevelopmentEngineer' },
    'game-dev': { domain: 'SoftwareDev', position: 'GameDevelopmentEngineer' },
    'software-test': { domain: 'SoftwareDev', position: 'SoftwareTestEngineer' },
    'software-architect': { domain: 'SoftwareDev', position: 'SoftwareArchitect' }
  };

  const { domain, position } = domainPositionMap[value];
  if (!domain || !position) return;

  try {
    const response = await axios.get('/question-data/', {
      params: {
        domain,
        position
      }
    });
    const data = response.data;

    // 更新题量统计
    document.querySelector('.count').textContent = `共${data.totalQuestions}道题`;

    // 转换数据结构
    techSections.length = 0;
    data.sections.forEach(section => {
      techSections.push({
        id: section.id,
        name: section.name,
        iconClass: () => section.icon,
        examCount: section.exams.length,
        scrollPosition: 0,
        scrollContainer: null,
        exams: section.exams
        .slice() // 拷贝副本避免原数组被修改
        .sort((a, b) => a.title.localeCompare(b.title, 'zh-Hans')) // 中文拼音首字母排序
        .map(exam => ({
          title: exam.title,
          questionCount: exam.questionCount,
          updateDate: exam.updateDate,  // 返回格式2025-01-01
          difficulty: exam.difficulty  // 返回格式初级，中级，高级
        }))
      });
    });

    // 更新技术标签 - 从sections数据中提取
    updateTechTagsFromSections();
  } catch (error) {
    console.error('获取题库数据失败:', error);
  }
};

// 从sections数据中提取并更新技术标签
const updateTechTagsFromSections = () => {
  // 清空当前技术标签
  techTags.length = 0;
  
  // 从sections中提取技术标签
  techSections.forEach(section => {
    // 随机分配标签类型
    const tagTypes = ['primary', 'success', 'warning', 'danger', 'info'];
    const randomIndex = Math.floor(Math.random() * tagTypes.length);
    const type = tagTypes[randomIndex];
    
    techTags.push({
      id: section.id,
      name: section.name,
      type: type
    });
  });
};

// 滚动到指定技术领域
const scrollToTechSection = (techId) => {
  const section = document.getElementById(techId);
  if (section) {
    section.scrollIntoView({ behavior: 'smooth' });
  }
};

// 计算最大滚动距离
const getMaxScroll = (techId) => {
  const tech = techSections.find(t => t.id === techId);
  if (!tech || !tech.scrollContainer) return 0;
  
  const containerWidth = tech.scrollContainer.offsetWidth;
  const parentWidth = tech.scrollContainer.parentElement.offsetWidth;
  return Math.max(0, containerWidth - parentWidth);
};

// 向左滚动
const scrollLeft = (techId) => {
  const tech = techSections.find(t => t.id === techId);
  if (!tech) return;
  
  const scrollStep = 272; // 卡片宽度 + 间距
  tech.scrollPosition = Math.max(0, tech.scrollPosition - scrollStep);
};

// 向右滚动
const scrollRight = (techId) => {
  const tech = techSections.find(t => t.id === techId);
  if (!tech) return;
  
  const scrollStep = 272; // 卡片宽度 + 间距
  const maxScroll = getMaxScroll(techId);
  tech.scrollPosition = Math.min(maxScroll, tech.scrollPosition + scrollStep);
};

// 查看题库详情
const viewExamDetails = (exam) => {
  console.log('查看题库详情:', exam);
  // 实际应用中这里应该跳转到题库详情页
};

// 生命周期钩子
onMounted(() => {
  // 初始加载第一个分类的数据
  handleCategorySelect('ai-algorithm');
});

</script>

<style scoped>
.app-container {
  font-family: 'Inter', system-ui, sans-serif;
  background-color: #f8f9fa;
  color: var(--dark-color);
}

.container {
  max-width: 1690px; /* 增加最大宽度 */
  padding: 0 0.75rem; /* 减小左右内边距 */
}

/* 左侧导航样式 */
.left-nav {
  .el-menu {
    border-right: none;
  }
  
  .el-menu-item {
    padding: 0 1rem !important;
    margin: 0.25rem 0;
    border-radius: 0.375rem;
    transition: all 0.2s ease;
    
    &:hover {
      background-color: rgba(0, 0, 0, 0.03);
    }
    
    &.is-active {
      background-color: rgba(25, 137, 250, 0.1);
      color: var(--primary-color);
      font-weight: 500;
    }
  }
}

/* 题库卡片样式 */
.exam-card {
  border: 1px solid #e5e7eb;
  transition: all 0.3s ease;
  
  &:hover {
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    transform: translateY(-2px);
  }
}

/* 技术标签样式 */
.el-tag {
  padding: 0 0.75rem;
  height: 1.75rem;
  line-height: 1.75rem;
  font-size: 0.875rem;
  
  &.danger {
    background-color: rgba(245, 108, 108, 0.1);
    color: var(--danger-color);
    border-color: rgba(245, 108, 108, 0.2);
  }
  
  &.warning {
    background-color: rgba(255, 125, 0, 0.1);
    color: var(--warning-color);
    border-color: rgba(255, 125, 0, 0.2);
  }
  
  &.primary {
    background-color: rgba(25, 137, 250, 0.1);
    color: var(--primary-color);
    border-color: rgba(25, 137, 250, 0.2);
  }
  
  &.success {
    background-color: rgba(37, 196, 130, 0.1);
    color: var(--success-color);
    border-color: rgba(37, 196, 130, 0.2);
  }
  
  &.info {
    background-color: rgba(144, 147, 153, 0.1);
    color: var(--info-color);
    border-color: rgba(144, 147, 153, 0.2);
  }
}

/* 隐藏滚动条 */
.hide-scrollbar::-webkit-scrollbar {
  display: none;
}

.hide-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

/* 响应式设计 */  
@media (max-width: 768px) {
  .left-nav {
    margin-bottom: 1.5rem;
  }
  
  .container {
    padding: 0 0.5rem; /* 在小屏幕上进一步减小内边距 */
  }
}

/* 统计卡片样式 */
.statistics-cards {
  transition: all 0.3s ease;
}

/* 统计卡片内容样式 */
.statistic-card {
  border-bottom: 1px solid #e5e7eb;
  padding-bottom: 1rem;
  margin-bottom: 1rem;
}

.statistic-card:last-child {
  border-bottom: none;
  padding-bottom: 0;
  margin-bottom: 0;
}
</style>