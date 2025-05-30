<template>
  <div class="app-container">
    <!-- 主内容区 -->
    <main class="main-container container mx-auto py-6">
      <div class="flex flex-col lg:flex-row gap-6">
        <!-- 左侧分类导航 -->
        <div class="left-nav w-full lg:w-1/4 fixed-width-nav" :class="{ 'fixed-nav': isNavFixed, 'collapsed-nav': isNavCollapsed }">
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
              <h2 class="text-xl font-bold text-dark">开发岗题库</h2>
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
                            <span class="text-xs text-gray-500">难度：{{ exam.difficulty }}</span>
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

            <!-- 分页控件 -->
            <div class="pagination mt-8 flex items-center justify-between">
              <div class="text-sm text-gray-500">
                显示 1-3 个技术领域 / 共 {{ techSections.length }} 个技术领域
              </div>
              <el-pagination
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page="currentPage"
                :page-sizes="[3, 6, 9]"
                :page-size="pageSize"
                layout="prev, pager, next, sizes"
                :total="techSections.length"
              >
              </el-pagination>
            </div>
          </div>
        </div>

        <!-- 右侧统计卡片 -->
        <div class="statistics-cards w-full lg:w-1/4" :class="{ 'fixed-cards': isCardsFixed, 'collapsed-cards': isCardsCollapsed }">
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
import { ref, reactive, onMounted, computed, onUnmounted } from 'vue';
import { 
  Search, Coffee, User as UsersIcon, Rank, ArrowLeft, ArrowRight, Briefcase as BriefcaseIcon, Menu
} from '@element-plus/icons-vue';

// 状态管理
const activeCategory = ref('dev');
const sortOption = ref('default');
const currentPage = ref(1);
const pageSize = ref(3);

// 新增状态
const isNavFixed = ref(false);
const isNavCollapsed = ref(false);
const isCardsFixed = ref(false);
const isCardsCollapsed = ref(false);

// 技术标签数据
const techTags = reactive([
  { id: 'java', name: 'Java', type: 'danger' },
  { id: 'python', name: 'Python', type: 'warning' },
  { id: 'javascript', name: 'JavaScript', type: 'primary' },
  { id: 'database', name: '数据库', type: 'success' },
  { id: 'network', name: '计算机网络', type: 'info' },
  { id: 'os', name: '操作系统', type: 'warning' },
  { id: 'algorithm', name: '算法', type: 'danger' },
  { id: 'frontend', name: '前端', type: 'primary' }
]);

// 技术领域数据
const techSections = reactive([
  {
    id: 'java',
    name: 'Java',
    iconClass: Coffee,
    examCount: 24,
    scrollPosition: 0,
    scrollContainer: null,
    exams: [
      { title: 'Java基础面试题', questionCount: 30, updateDate: '2023-05-10', difficulty: '中等' },
      { title: 'Java集合框架', questionCount: 25, updateDate: '2023-05-08', difficulty: '中等' },
      { title: '多线程与并发', questionCount: 28, updateDate: '2023-05-05', difficulty: '较难' },
      { title: 'JVM内存模型', questionCount: 22, updateDate: '2023-05-03', difficulty: '较难' },
      { title: '设计模式', questionCount: 20, updateDate: '2023-04-30', difficulty: '中等' }
    ]
  },
  {
    id: 'database',
    name: '数据库',
    iconClass: Menu,
    examCount: 18,
    scrollPosition: 0,
    scrollContainer: null,
    exams: [
      { title: 'SQL基础', questionCount: 25, updateDate: '2023-05-08', difficulty: '简单' },
      { title: '索引优化', questionCount: 20, updateDate: '2023-05-05', difficulty: '中等' },
      { title: '事务与锁', questionCount: 22, updateDate: '2023-05-03', difficulty: '较难' },
      { title: '数据库设计', questionCount: 18, updateDate: '2023-04-30', difficulty: '中等' }
    ]
  },
  {
    id: 'network',
    name: '计算机网络',
    iconClass: Menu,
    examCount: 15,
    scrollPosition: 0,
    scrollContainer: null,
    exams: [
      { title: 'TCP/IP协议', questionCount: 22, updateDate: '2023-05-05', difficulty: '中等' },
      { title: 'HTTP协议', questionCount: 20, updateDate: '2023-05-03', difficulty: '简单' },
      { title: '网络安全', questionCount: 18, updateDate: '2023-04-30', difficulty: '较难' }
    ]
  },
  {
    id: 'algorithm',
    name: '算法',
    iconClass: Menu,
    examCount: 22,
    scrollPosition: 0,
    scrollContainer: null,
    exams: [
      { title: '数据结构', questionCount: 25, updateDate: '2023-05-10', difficulty: '较难' },
      { title: '排序算法', questionCount: 20, updateDate: '2023-05-08', difficulty: '中等' },
      { title: '递归与回溯', questionCount: 22, updateDate: '2023-05-05', difficulty: '较难' },
      { title: '动态规划', questionCount: 28, updateDate: '2023-05-03', difficulty: '较难' },
      { title: '贪心算法', questionCount: 18, updateDate: '2023-04-30', difficulty: '中等' }
    ]
  },
  {
    id: 'javascript',
    name: 'JavaScript',
    iconClass: Menu,
    examCount: 20,
    scrollPosition: 0,
    scrollContainer: null,
    exams: [
      { title: 'JavaScript基础', questionCount: 25, updateDate: '2023-05-08', difficulty: '中等' },
      { title: 'ES6+新特性', questionCount: 22, updateDate: '2023-05-05', difficulty: '中等' },
      { title: '异步编程', questionCount: 20, updateDate: '2023-05-03', difficulty: '较难' },
      { title: '设计模式', questionCount: 18, updateDate: '2023-04-30', difficulty: '中等' }
    ]
  },
  {
    id: 'python',
    name: 'Python',
    iconClass: Menu,
    examCount: 18,
    scrollPosition: 0,
    scrollContainer: null,
    exams: [
      { title: 'Python基础', questionCount: 25, updateDate: '2023-05-10', difficulty: '中等' },
      { title: '数据分析', questionCount: 20, updateDate: '2023-05-08', difficulty: '中等' },
      { title: 'Web开发', questionCount: 22, updateDate: '2023-05-05', difficulty: '中等' },
      { title: '机器学习', questionCount: 18, updateDate: '2023-05-03', difficulty: '较难' }
    ]
  },
  {
    id: 'frontend',
    name: '前端',
    iconClass: Menu,
    examCount: 16,
    scrollPosition: 0,
    scrollContainer: null,
    exams: [
      { title: 'HTML/CSS基础', questionCount: 20, updateDate: '2023-05-08', difficulty: '简单' },
      { title: '响应式设计', questionCount: 18, updateDate: '2023-05-05', difficulty: '中等' },
      { title: '性能优化', questionCount: 15, updateDate: '2023-05-03', difficulty: '中等' },
      { title: '工程化', questionCount: 12, updateDate: '2023-04-30', difficulty: '较难' }
    ]
  },
  {
    id: 'os',
    name: '操作系统',
    iconClass: Menu,
    examCount: 12,
    scrollPosition: 0,
    scrollContainer: null,
    exams: [
      { title: '进程与线程', questionCount: 20, updateDate: '2023-05-05', difficulty: '中等' },
      { title: '内存管理', questionCount: 18, updateDate: '2023-05-03', difficulty: '较难' },
      { title: '文件系统', questionCount: 15, updateDate: '2023-04-30', difficulty: '中等' }
    ]
  }
]);

// 计算当前页显示的技术领域
const displayedTechSections = computed(() => {
  const startIndex = (currentPage.value - 1) * pageSize.value;
  const endIndex = startIndex + pageSize.value;
  return techSections.slice(startIndex, endIndex);
});

// 处理岗位选择
const handleCategorySelect = (value) => {
  activeCategory.value = value;
  
  // 更新题库标题
  const positionNames = {
    'dev': '开发岗',
    'ops': '运营岗',
    'design': '设计岗',
    'sales': '销售岗',
    'hr': '人力资源',
    'education': '教育岗'
  };
  
  const positionName = positionNames[value] || '开发岗';
  document.querySelector('.question-list h2').textContent = `${positionName}题库`;
  
  // 更新题量统计
  const counts = {
    'dev': '120',
    'ops': '85',
    'design': '72',
    'sales': '90',
    'hr': '65',
    'education': '58'
  };
  document.querySelector('.count').textContent = `共${counts[value] || '120'}道题`;
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

// 分页大小变化
const handleSizeChange = (newSize) => {
  pageSize.value = newSize;
  currentPage.value = 1;
};

// 当前页变化
const handleCurrentChange = (newPage) => {
  currentPage.value = newPage;
};

// 监听滚动事件
const handleScroll = () => {
  const navElement = document.querySelector('.left-nav');
  const cardsElement = document.querySelector('.statistics-cards');
  const navOffsetTop = navElement.offsetTop;
  const cardsOffsetTop = cardsElement.offsetTop;
  const scrollTop = window.scrollY;

  if (scrollTop > navOffsetTop) {
    isNavFixed.value = true;
    if (scrollTop > navOffsetTop + navElement.offsetHeight) {
      isNavCollapsed.value = true;
    } else {
      isNavCollapsed.value = false;
    }
  } else {
    isNavFixed.value = false;
    isNavCollapsed.value = false;
  }

  if (scrollTop > cardsOffsetTop) {
    isCardsFixed.value = true;
    if (scrollTop > cardsOffsetTop + cardsElement.offsetHeight) {
      isCardsCollapsed.value = true;
    } else {
      isCardsCollapsed.value = false;
    }
  } else {
    isCardsFixed.value = false;
    isCardsCollapsed.value = false;
  }
};

// 生命周期钩子
onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

// 清理事件监听器
onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
/* 全局样式 */
:root {
  --primary-color: #1989FA;
  --secondary-color: #FFC107;
  --success-color: #25C482;
  --warning-color: #FF7D00;
  --danger-color: #F56C6C;
  --info-color: #909399;
  --light-color: #F8F9FA;
  --dark-color: #333333;
}

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

/* 固定导航宽度 */
.fixed-width-nav {
  width: 700px; /* 设置固定宽度，可以根据实际情况调整 */
}

/* 菜单项超出省略号显示 */
.fixed-width-nav .el-menu-item span {
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* 固定导航样式 */
.fixed-nav {
  position: fixed;
  top: 0;
  z-index: 100;
  transition: all 0.3s ease;
}

/* 折叠导航样式 */
.collapsed-nav {
  width: auto;
  transform: scale(0.8);
  transform-origin: top left;
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

/* 固定统计卡片样式 */
.fixed-cards {
  position: fixed;
  top: 0;
  z-index: 100;
}

/* 折叠统计卡片样式 */
.collapsed-cards {
  width: auto;
  transform: scale(0.8);
  transform-origin: top right;
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