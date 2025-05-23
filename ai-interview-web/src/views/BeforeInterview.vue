<template>
  <div class="layout-wrapper">
    <!-- 蒙版 -->
    <div
      v-if="showLeftSidebar || showRightSidebar"
      class="overlay"
      @click="closeSidebars"
    ></div>

    <!-- 顶部导航栏 -->
    <el-header class="header">
      <div class="header-left">
        <el-icon class="collapse-icon" @click.stop="showLeftSidebar = true"><Fold /></el-icon>
        <img src="../assets/pic/logo.jpg" class="logo-icon" />
        <span class="app-title">{{ currentTitle }}</span>
      </div>
      <div class="header-right">
        <el-icon><Bell /></el-icon>
        <el-icon><Setting /></el-icon>
        <div class="avatar-container" @click.stop="showRightSidebar = true">
          <el-avatar class="avatar-circle">{{ userInitial }}</el-avatar>
        </div>
      </div>
    </el-header>

    <!-- 主显示区域 -->
    <el-main class="main-content">
      <router-view />
    </el-main>

    <!-- 左侧悬浮侧边栏 -->
    <transition name="slide-left">
      <div
        v-if="showLeftSidebar"
        class="floating-sidebar left"
        @click.stop
      >
        <div class="sidebar-header left-header">
            <img src="../assets/pic/logo.jpg" class="sidebar-logo" />
            <el-tooltip content="关闭" placement="bottom">
              <el-button icon="Close" circle size="small" @click="showLeftSidebar = false" />
            </el-tooltip>
        </div>

        <!-- 功能列表 -->
        <div class="sidebar-menu">
          <div class="sidebar-item" v-for="item in menuItems" :key="item.name" :class="['sidebar-item', { 'with-divider': item.divider }]" @click="navigateTo(item.route)">
            <el-icon :size="21"><component :is="item.icon" /></el-icon>
            <span class="sidebar-text">{{ item.name }}</span>
          </div>
        </div>

        <div class="sidebar-footer-text">
          <small>© 2025 SSS AI</small>
        </div>

      </div>
    </transition>

    <!-- 右侧悬浮侧边栏 -->
    <transition name="slide-right">
      <div
        v-if="showRightSidebar"
        class="floating-sidebar right"
        @click.stop
      >
        <div class="sidebar-header right-header">
          <div class="right-sidebar-userinfo">
            <el-avatar class="sidebar-avatar">{{ userInitial }}</el-avatar>
            <span class="username">{{ username }}</span>
          </div>
          <div class="right-sidebar-controls">
            <el-tooltip content="切换账号" placement="bottom">
              <el-button icon="UserFilled" circle size="small" />
            </el-tooltip>
            <el-tooltip content="关闭" placement="bottom">
              <el-button icon="Close" circle size="small" @click="showRightSidebar = false" />
            </el-tooltip>
          </div>
        </div>
        <!-- 可添加更多内容 -->
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, watch} from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { Fold, Bell, Setting, User, Close, UserFilled, Notebook,  Files, Document, Suitcase, DataAnalysis } from '@element-plus/icons-vue'

const username = 'NanFengSNI'
const userInitial = username.charAt(0).toUpperCase()

const showLeftSidebar = ref(false)
const showRightSidebar = ref(false)

const closeSidebars = () => {
  showLeftSidebar.value = false
  showRightSidebar.value = false
}

const router = useRouter()
const route = useRoute()

const currentTitle = ref('SSS AI')
// 路由路径到标题的映射
const routeTitleMap = {
  '/before-interview/detail': '个人信息',
  '/before-interview/resume': '简历文档',
  '/before-interview/analysis': '能力分析',
  '/before-interview/jobs': '岗位推荐',
  '/before-interview/questions': '题库展示',
  '/before-interview/test': '学习训练'
}

// 初始化设置标题
currentTitle.value = routeTitleMap[route.path] || 'SSS AI'

// 监听路由变化，动态更新标题
watch(() => route.path, (newPath) => {
  currentTitle.value = routeTitleMap[newPath] || 'SSS AI'
})

const navigateTo = (route) => {
  router.push(route)
  showLeftSidebar.value = false // 点击后自动关闭侧边栏
}

// 监听侧边栏的变化，自动禁用滑动条
watch([showLeftSidebar, showRightSidebar], ([left, right]) => {
  const anyOpen = left || right
  document.body.style.overflow = anyOpen ? 'hidden' : 'auto'
})

const menuItems = [
  { name: '个人信息', icon: User , route: '/before-interview/detail'},
  { name: '简历文档', icon: Document , route: '/before-interview/resume'},
  { name: '能力分析', icon: DataAnalysis , route: '/before-interview/analysis'},
  { name: '岗位推荐', icon: Suitcase , route: '/before-interview/jobs'},
  { name: '题库展示', icon: Files , route: '/before-interview/questions'},
  { name: '学习训练', icon: Notebook , route: '/before-interview/test'}
]

</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  overflow: hidden;
  height: 100%;
}
</style>

<style scoped>
/* * { outline: 1px solid red;}  /* 高亮每个元素边界 */

/* 页面最外层容器，使用纵向布局，撑满视口高度 */
.layout-wrapper {
  height: 100vh; /* 设置高度为视口高度 */
  overflow: hidden; /* 隐藏溢出部分 */
  display: flex; /* 启用 flex 布局 */
  flex-direction: column; /* 子元素垂直排列 */
  position: relative; /* 相对定位 */
}

/* 顶部导航栏样式 */
.header {
  height: 64px; /* 固定高度为 64px */
  background-color: #5d9ad649; /* 背景色为浅灰色 */
  display: flex; /* 使用 flex 布局 */
  justify-content: space-between; /* 子元素两端对齐 */
  align-items: center; /* 子元素垂直居中 */
  padding: 0 20px; /* 左右内边距各 20px */
  color: rgb(34, 32, 32); /* 字体颜色为黑色 */
  position: fixed; /* 固定定位在页面顶部 */
  top: 0; /* 顶部对齐 */
  left: 0; /* 左侧对齐 */
  right: 0; /* 右侧对齐 */
  z-index: 1000; /* 设置层级高于普通内容 */
  border-top: 1px solid rgba(0, 0, 0, 0.1); /* 顶部线条 */
  border-bottom: 1px solid rgba(0, 0, 0, 0.1); /* 添加底部线条 */
}

/* 顶栏左侧容器（Logo、标题、折叠按钮） */
.header-left {
  display: flex; /* 启用 flex 布局 */
  align-items: center; /* 垂直居中对齐 */
  gap: 20px; /* 子项之间间距为 20px */
}

/* Logo 图标样式 */
.logo-icon {
  height: 35px; /* 高度为 35px */
}

/* 应用标题文字样式 */
.app-title {
  font-family: 'Microsoft YaHei', sans-serif; /* 字体为微软雅黑 */
  font-size: 20px; /* 字体大小为 20px */
  font-weight: bold; /* 加粗字体 */
}

/* 折叠菜单图标样式 */
.collapse-icon {
  cursor: pointer; /* 鼠标悬浮变为指针 */
  font-size: 20px; /* 图标字体大小为 20px */
  color: #201f1f; /* 字体颜色为浅灰色 */
}

/* 顶栏右侧用户信息区域 */
.header-right {
  display: flex; /* 使用 flex 布局 */
  align-items: center; /* 垂直居中对齐 */
  gap: 20px; /* 子项之间间距为 16px */
}

/* 头像容器，包含点击效果 */
.avatar-container {
  display: flex; /* 启用 flex 布局 */
  align-items: center; /* 垂直居中 */
  cursor: pointer; /* 鼠标悬停变为指针 */
}

/* 圆形头像样式 */
.avatar-circle {
  width: 36px; /* 宽度为 36px */
  height: 36px; /* 高度为 36px */
  font-size: 16px; /* 字体大小为 16px */
  background-color: #409eff; /* 背景蓝色 */
  color: white; /* 字体白色 */
}

/* 主体内容区域样式 */
.main-content {
  flex-grow: 1; /* 填满剩余空间 */
  padding: 64px 1px 1px 1px; 
  overflow-y: hidden; 
  background-color: #fcfcfc; /* 白色背景 */
}

/* 遮罩层样式，用于弹出侧边栏时 */
.overlay {
  position: fixed; /* 固定定位 */
  top: 0px; /* 顶部对齐 */
  left: 0; /* 左对齐 */
  right: 0; /* 右对齐 */
  bottom: 0; /* 底对齐 */
  background-color: rgba(0, 0, 0, 0.3); /* 半透明黑色背景 */
  z-index: 1500; /* 层级高于主内容 */
  backdrop-filter: blur(2px); /* 背景模糊处理 */
}

/* 浮动侧边栏的基础样式 */
.floating-sidebar {
  position: fixed; /* 固定定位 */
  top: 0px; /* 顶部对齐 */
  width: 260px; /* 固定宽度 */
  height: calc(100vh); /* 高度为视口高度 */
  background: white; /* 背景白色 */
  box-shadow: 0 0 10px rgba(0,0,0,0.1); /* 阴影效果 */
  z-index: 2000; /* 层级高于遮罩层 */
  padding: 16px; /* 内边距 16px */
  display: flex; /* 使用 flex 布局 */
  flex-direction: column; /* 子元素垂直排列 */
  justify-content:  flex-start; /* 顶部对齐 */
}

/* 左侧浮动侧边栏圆角处理 */
.floating-sidebar.left {
  left: 0; /* 靠左显示 */
  border-top-right-radius: 12px; /* 顶部右圆角 */
  border-bottom-right-radius: 12px; /* 底部右圆角 */
}

/* 左侧边栏 Logo 样式 */
.sidebar-logo {
  height: 40px;
  margin-right: auto; /* 自动占据空间，将关闭按钮推到右边 */
}

/* 功能列表整体容器样式 */
.sidebar-menu {
  margin-top: 50px;              /* 距离上方内容（如 logo 和关闭按钮）50px */
  display: flex;                 /* 使用 Flexbox 布局 */
  flex-direction: column;       /* 子项垂直排列 */
  gap: 12px;                     /* 每个功能项之间垂直间距为 12px */
  padding: 0.5 18px;               /* 左右内边距为 16px，避免内容贴边 */
  border-bottom: 1px solid rgba(0, 0, 0, 0.1); /* 添加底部线条 */
}

/* 每个功能项的样式 */
.sidebar-item {
  display: flex;                /* 使用 Flexbox 布局 */
  align-items: center;         /* 图标与文字垂直居中对齐 */
  gap: 14px;                   /* 图标和文字之间间距为 14px */
  color: #5e6061;              /* 图标颜色为浅灰色 */
  cursor: pointer;             /* 鼠标悬停时显示手形光标，表示可点击 */
  padding: 6px 11px;            /* 上下内边距 6px，左右 11px，增加点击区域 */
  border-radius: 6px;          /* 圆角边框，提升视觉友好度 */
  transition: background-color 0.2s; /* 背景色变换添加动画过渡，增强交互感 */
}

.sidebar-item.with-divider {
  border-top: 1px solid rgba(0, 0, 0, 0.1); /* 加一条细的分隔线 */
}

.sidebar-footer-text{
  margin-top: 50px;   
  font-size: 14px;
  color: #4b4c4d; /* 字体颜色为浅灰色 */
}

/* 鼠标悬停时的高亮效果 */
.sidebar-item:hover {
  background-color: rgba(93, 154, 214, 0.1); /* 鼠标悬停时背景变淡蓝色 */
}

/* 功能名称文字样式 */
.sidebar-text {
  font-size: 16px;             /* 字体大小为 16px，适中清晰 */
  color: #3f3d3d;                 /* 字体颜色为深灰，易于阅读 */
}

/* 右侧浮动侧边栏圆角处理 */
.floating-sidebar.right {
  right: 0; /* 靠右显示 */
  border-top-left-radius: 12px; /* 顶部左圆角 */
  border-bottom-left-radius: 12px; /* 底部左圆角 */
}

/* 侧边栏头部内容容器 */
.sidebar-header {
  display: flex; /* 启用 flex 布局 */
  justify-content: space-between; /* 子项两端对齐 */
  align-items: center; /* 垂直居中 */
}

/* 右侧栏标题区域采用垂直布局 */
.right-header {
  flex-direction: row; /* 水平排列 */
  align-items: flex-start; /* 顶部对齐 */
  gap: 15px; /* 子项间距 15px */
}

/* 用户信息区域（头像 + 名字） */
.right-sidebar-userinfo {
  display: flex; /* 启用 flex 布局 */
  align-items: center; /* 垂直居中 */
  gap: 10px; /* 子项间距 10px */
}

/* 用户名样式 */
.username {
  font-weight: bold; /* 加粗字体 */
  font-size: 14px; /* 字体大小 14px */
  white-space: nowrap; /* 不换行 */
  overflow: hidden; /* 超出隐藏 */
  text-overflow: ellipsis; /* 溢出显示省略号 */
}

/* 侧边栏中的头像样式 */
.sidebar-avatar {
  background-color: #409eff; /* 背景蓝色 */
  color: white; /* 字体颜色白色 */
  width: 36px; /* 宽度 36px */
  height: 36px; /* 高度 36px */
  font-size: 16px; /* 字体大小 16px */
}

/* 右侧栏操作按钮容器 */
.right-sidebar-controls {
  display: flex; /* 启用 flex 布局 */
  gap: 10px; /* 子项间距 10px */
  align-self: center; /* 中对齐 */
}

/* 左侧侧边栏显示动画：进入 & 离开过程过渡 */
.slide-left-enter-active,
.slide-left-leave-active {
  transition: transform 0.3s ease; /* 平滑过渡效果 */
}

/* 左侧侧边栏显示动画：初始状态和结束状态 */
.slide-left-enter-from,
.slide-left-leave-to {
  transform: translateX(-100%); /* 从左侧滑入或滑出 */
}

/* 右侧侧边栏显示动画：进入 & 离开过程过渡 */
.slide-right-enter-active,
.slide-right-leave-active {
  transition: transform 0.3s ease; /* 平滑过渡效果 */
}

/* 右侧侧边栏显示动画：初始状态和结束状态 */
.slide-right-enter-from,
.slide-right-leave-to {
  transform: translateX(100%); /* 从右侧滑入或滑出 */
}
</style>

