<template>
  <div class="document-page">
    <!-- 左侧区域 -->
    <div class="left-panel">
      <!-- 操作按钮和搜索栏 -->
      <div class="action-section">
        <div class="action-buttons">
          <el-button class= 'upload-btn' size="large" plain @click="uploadDialogVisible = true">
            <el-icon :size="18" style="margin-right: 6px;"><Upload /></el-icon>
            上传文件
          </el-button>
          <el-button class="create-btn" size="large" plain @click="openAIResume()">
            <el-icon :size="18" style="margin-right: 6px;"><DocumentAdd /></el-icon>
            使用 AI 简历生成器创建
          </el-button>
        </div>
        <div class="filter-bar">
          <el-select v-model="selectedType" placeholder="筛选类型" clearable style="width: 140px;">
            <el-option label="简历" value="简历" />
            <el-option label="求职信" value="求职信" />
          </el-select>
          <el-date-picker
            v-model="selectedDate"
            type="date"
            placeholder="上传日期"
            clearable
            style="width: 160px;"
          />
          <el-button size="small" type="text" class="clear-filters-btn" @click="clearFilters" style="margin-left:auto;">
            清除筛选
          </el-button>
        </div>
      </div>

      <!-- 文件卡片列表 -->
      <div class="card-list">
        <el-card
          v-for="doc in filteredDocuments"
          :key="doc.name"
          shadow="hover"
          class="file-card"
        >
          <div class="card-header">
            <div class="file-name">{{ doc.name }}</div>
            <el-tag type="info" size="small">{{ doc.type }}</el-tag>
          </div>
          <div class="file-date">上传日期：{{ doc.uploadDate }}</div>
          <div class="card-actions">
            <el-tooltip content="预览" placement="bottom">
              <el-button icon="FullScreen" size="small" @click="preview(doc)"/>
            </el-tooltip>
            <el-tooltip content="AI编辑" placement="bottom">
              <el-button icon="MagicStick" size="small" @click="openAIResume()" />
            </el-tooltip>
            <el-tooltip content="下载" placement="bottom">
              <el-button icon="Download" size="small" @click="download(doc)" />
            </el-tooltip>
            <el-tooltip content="删除" placement="bottom">
              <el-button icon="Delete" type="danger" size="small" @click="remove(doc)" />
            </el-tooltip>
          </div>
        </el-card>
      </div>
    </div>

    <!-- 右侧区域：PDF 预览 -->
    <div class="right-panel">
      <template v-if="previewUrl">
        <!-- 清除预览按钮 -->
        <el-tooltip content="清除预览" placement="right">
          <el-button
            type="danger"
            :icon="Close"
            class="clear-preview-btn"
            circle
            @click="previewUrl = ''"
          />
        </el-tooltip>

        <!-- PDF 预览组件 -->
        <PdfPreview :fileUrl="previewUrl" />
      </template>
      
      <div v-else class="pdf-preview-placeholder">
        <p>这里是 PDF 文件预览区域</p>
      </div>
    </div>

    <!-- 上传文件弹窗 -->
    <el-dialog
  v-model="uploadDialogVisible"
  title="上传文件"
  width="480px"
  :close-on-click-modal="false"
  @close="resetUploadDialog"
>
  <div style="margin-bottom: 20px;">
    <el-radio-group v-model="uploadForm.type" size="medium">
      <el-radio-button label="简历" />
      <el-radio-button label="求职信" />
      <el-radio-button label="其他" />
    </el-radio-group>
  </div>

  <!-- 拖拽上传框 -->
  <el-upload
    drag
    :before-upload="handleBeforeUpload"
    :show-file-list="false"
    accept=".pdf"
    class="upload-area"
  >
    <el-icon><UploadFilled /></el-icon>
    <div class="el-upload__text">
      将文件拖到此处，或 <em>点击上传</em>
    </div>
    <div class="el-upload__tip">仅支持 PDF 文件，大小不超过 5MB</div>
  </el-upload>

  <div v-if="uploadForm.fileName" style="margin-top: 16px;">
    <el-alert :title="'选中文件：' + uploadForm.fileName" type="info" show-icon />
  </div>

  <template #footer>
    <el-button @click="uploadDialogVisible = false">取消</el-button>
    <el-button
      type="primary"
      :disabled="!uploadForm.file"
      @click="submitUpload"
    >
      上传
    </el-button>
  </template>
</el-dialog>
  </div>
</template>

<script setup>
import { MagicStick, Download, Delete, DocumentAdd, Upload, FullScreen, Close  } from '@element-plus/icons-vue'
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import PdfPreview from '../components/PdfPreview.vue'
import { ElMessage, ElMessageBox, ElButton, ElTooltip } from 'element-plus'

const router = useRouter()
const documents = ref([])
const previewUrl = ref('')
const selectedType = ref(null)
const selectedDate = ref(null)

const filteredDocuments = computed(() => {
  return documents.value.filter(doc => {
    const matchType = selectedType.value ? doc.type === selectedType.value : true
    const matchDate = selectedDate.value
      ? doc.uploadDate === selectedDate.value.toISOString().slice(0, 10)
      : true
    return matchType && matchDate
  })
})

const openAIResume = () => {
  router.push('/before-interview/airesume')
}

function clearFilters() {
  selectedType.value = null
  selectedDate.value = null
}

function preview(doc) {
  console.log('预览：', doc)
  if (doc.fileBlobUrl) {
    previewUrl.value = doc.fileBlobUrl
  } else {
    ElMessage.warning('文件读取错误，无法预览')
  }
}

function download(doc) {
  const link = document.createElement('a')
  link.href = doc.fileBlobUrl || doc.fileUrl
  link.download = doc.name
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

async function remove(doc) {
  try {
      await ElMessageBox.confirm(
            `确定删除「${doc.name}」吗？`,
        {
          confirmButtonText: '彻底删除',
          cancelButtonText: '取消',
          type: 'warning',
        }
      )

    await axios.delete(`/api/delete/${doc.name}`)

    // 重新拉取文档列表
    await fetchDocuments()

    if (previewUrl.value === doc.fileBlobUrl) {
      previewUrl.value = ''
    }

    ElMessage.success('文件已删除')
  } catch (error) {
    if (error !== 'cancel') {
      console.error('删除失败:', error)
      ElMessage.error('删除失败')
    }
  }
}

// 弹窗相关
const uploadDialogVisible = ref(false)
const uploadForm = ref({
  file: null,
  fileName: '',
  type: '简历',
})

const fileInput = ref(null)

function handleBeforeUpload(file) {
  const isAllowed = file.type === 'application/pdf';
  const isLt5M = file.size / 1024 / 1024 < 5;

  if (!isAllowed) {
    ElMessage.error('仅支持 PDF 文件');
    return false;
  }
  if (!isLt5M) {
    ElMessage.error('文件大小不能超过 5MB');
    return false;
  }

  uploadForm.value.file = file;
  uploadForm.value.fileName = file.name;
  return false;
}

function resetUploadDialog() {
   uploadForm.value = {
    file: null,
    fileName: '',
    type: '简历',
  }
  if (fileInput.value) fileInput.value.value = ''
}

async function submitUpload() {
  if (!uploadForm.value.file) return

  const formData = new FormData()
  formData.append('file', uploadForm.value.file)
  formData.append('type', uploadForm.value.type)

  try {
    const response = await axios.post('/api/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })

    const today = new Date().toISOString().slice(0, 10)
    const blobUrl = URL.createObjectURL(uploadForm.value.file)

    const newDoc = {
      id: response.data.id, // 从后端返回的数据中获取
      name: uploadForm.value.fileName,
      type: uploadForm.value.type,
      uploadDate: today,
      fileBlobUrl: blobUrl,
      fileUrl: response.data.url || null // 可用于后续下载
    }

    documents.value.push(newDoc)
    previewUrl.value = blobUrl

    ElMessage.success('上传成功')
    uploadDialogVisible.value = false
    resetUploadDialog()
  } catch (error) {
    ElMessage.error('上传失败')
  }
}

async function fetchDocuments() {
  try {
    const response = await axios.get('/api/files')
    const files = response.data  // [{ id, name, type, uploadDate, fileUrl }]

    // 对每个文件拉取 blob 生成本地预览地址
    const processed = await Promise.all(
      files.map(async file => {
        try {
          const res = await axios.get(file.fileUrl, { responseType: 'blob' })
          const blobUrl = URL.createObjectURL(res.data)
          return { ...file, fileBlobUrl: blobUrl }
        } catch (e) {
          return { ...file, fileBlobUrl: null }
        }
      })
    )

    documents.value = processed
  } catch (error) {
    ElMessage.error('加载文件失败')
  }
}

// 页面加载时从后端加载文件
onMounted(async () => {
  await fetchDocuments()
})

</script>

<style scoped>
.document-page {
  display: flex; /* 整体使用 Flexbox 实现左右分栏布局 */
  height: 100%; /* 高度撑满父容器，确保全屏显示 */
  background: #fcfcfc; /* 页面背景颜色，浅灰白，保持整体统一 */
  border-radius: 16px; /* 页面整体圆角，提升视觉柔和感 */
  box-shadow: 0 4px 16px rgba(0,0,0,0.06); /* 轻微投影，增加层次感 */
  overflow: hidden; /* 防止子元素内容溢出，保持圆角效果 */
}

/* 左侧面板：主要内容区域，宽度稍大 */
.left-panel {
  flex: 1.2; /* 弹性比例，略宽于右侧面板 */
  display: flex; /* 内部也使用 flex 方便纵向排列 */
  flex-direction: column; /* 子元素垂直排列 */
  padding: 32px 24px 32px 32px; /* 内边距：上右下左 */
  box-sizing: border-box; /* 让 padding 和 border 计入宽高计算 */
  border-right: 1px solid #e4e7ed; /* 右侧边框分割线，浅灰色 */
  background: #fff; /* 背景白色，突显卡片内容 */
}

/* 右侧面板：PDF 预览区域 */
.right-panel {
  position: relative; /* 相对定位，方便子元素绝对定位 */
  flex: 1; /* 弹性比例，宽度稍窄 */
  padding: 10px 20px 24px 24px; /* 内边距，上右下左 */
  box-sizing: border-box; /* 同上，包含 padding 和 border */
  background: #fff; /* 背景白色 */
  display: flex; /* 使用 flexbox 让内容居中显示 */
  flex-direction: column; /* 改为纵向排列 */
}
.clear-preview-btn {
  position: absolute;
  top: 16px;
  left: 16px;
  z-index: 100;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  background-color: #f56c6c !important;
  color: white !important;
  font-size: 18px;
  transition: all 0.3s ease;
}

.clear-preview-btn:hover {
  background-color: #dd6161 !important;
  transform: scale(1.1);
}

/* 操作区块：按钮和筛选区域整体背景和间距 */
.action-section {
  padding: 1px 4px; /* 内边距，上右下左 */
  margin-bottom: 14px; /* 底部间距，和下方内容分开 */
}

/* 按钮组横向排列 */
.action-buttons {
  display: flex; /* 横向排列按钮 */
  gap: 12px; /* 按钮之间间距 */
  margin-bottom: 30px; /* 按钮组与筛选栏的间距 */
}

.upload-btn {
  background-color: #000000; /* 黑底 */
  color: #ffffff !important; /* 白字，important防止被element-plus覆盖 */
  font-weight: 600; /* 字体稍微粗一点 */
  border-radius: 6px; /* 圆角 */
  font-family:
    "Microsoft YaHei",
    "微软雅黑",
    "PingFang SC",
    "苹方",
    "Helvetica Neue",
    Helvetica,
    Arial,
    sans-serif; /* 字体 */
  border: none; /* 去掉边框 */
}

.upload-btn:hover {
  background-color: #222222; /* 悬浮时变深点 */
  color: #ffffff !important;
}


/* 遮罩层加深 */
::deep(.el-overlay) {
  background-color: rgba(0, 0, 0, 0.8) !important;
}

/* 弹窗容器 */
::v-deep(.el-dialog) {
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
  padding: 16px;
}
::v-deep(.el-dialog__header) {
  font-weight: 700; /* 加粗 */
}

::v-deep(.upload-area) {
  border: 2px dashed #dcdfe6;
  border-radius: 8px;
  background-color: #f5f7fa;
  padding: 40px 20px;
  text-align: center;
  transition: all 0.3s;
  cursor: pointer;
}

::v-deep(.upload-area:hover) {
  border-color: #409EFF;
  background-color: #ecf5ff;
}

/* 上传区域样式 */
.file-input {
  display: block;
  width: 90%;
  padding: 20px;
  border: 2px dashed #dcdfe6;
  border-radius: 10px;
  text-align: center;
  font-size: 14px;
  color: #909399;
  cursor: pointer;
  background-color: #fafafa;
  transition: border-color 0.3s ease;
}

.file-input:hover {
  border-color: #409eff;
  background-color: #f4faff;
}

/* 上传提示文字 */
.upload-tip {
  margin-top: 8px;
  font-size: 13px;
  color: #409eff;
}

/* 弹窗底部按钮样式优化 */
::v-deep(.el-dialog__footer .el-button) {
  border-radius: 8px;
  min-width: 80px;
}

/* 主按钮强调 */
::v-deep(.el-dialog__footer .el-button--primary) {
  background-color: #000000;
  color: #ffffff;
  border: none;
}

::v-deep(.el-dialog__footer .el-button--primary:hover) {
  background-color: #222222;
}

/* 取消按钮轻量化 */
::v-deep(.el-dialog__footer .el-button:not(.el-button--primary)) {
  background-color: transparent;
  color: #606266;
}

.create-btn {
  background-color: #ffffff; /* 白底 */
  color: #000000 !important; /* 黑字 */
  font-weight: 400; /* 常规字体粗细 */
  border: 1.5px solid #000000; /* 黑色边框 */
  border-radius: 6px; /* 圆角 */
  font-family:
    "Microsoft YaHei",
    "微软雅黑",
    "PingFang SC",
    "苹方",
    "Helvetica Neue",
    Helvetica,
    Arial,
    sans-serif; /* 字体 */
}

.create-btn:hover {
  background-color: #f0f0f0; /* 悬浮时浅灰 */
  color: #000000 !important;
}

/* 操作按钮默认样式 */
.action-buttons .el-button {
  border: 1.5px solid #dcdfe6; /* 边框颜色浅，视觉轻盈 */
  box-shadow: 0 2px 6px rgb(0 0 0 / 0.12); /* 轻微阴影，增加浮雕感 */
  transition: box-shadow 0.3s ease, transform 0.2s ease; /* 平滑过渡动画 */
}

/* 按钮悬浮时效果 */
.action-buttons .el-button:hover {
  box-shadow: 0 6px 12px rgb(0 0 0 / 0.2); /* 阴影加深，突出按钮 */
  transform: translateY(-2px); /* 轻微上移，产生悬浮感 */
}

/* 筛选栏：包含选择控件 */
.filter-bar {
  display: flex; /* 横向排列控件 */
  align-items: center; /* 垂直居中 */
  gap: 16px; /* 控件之间间距 */
  padding-bottom: 12px; /* 底部内边距，增加呼吸感 */
  margin-bottom: 24px; /* 下方间距 */
  border-bottom: 1px solid #eaeaea; /* 底部分隔线，区分筛选栏和内容 */
}

/* 选择框和日期选择器统一宽度 */
.el-select {
  width: 180px !important; /* 强制宽度，确保布局统一 */
}
.el-date-picker {
  width: 180px !important; /* 同上 */
}

/* 鼠标悬停时边框颜色高亮 */
.el-select:hover, .el-date-picker:hover {
  border-color: #121213; /* Element Plus 主题蓝色 */
}

/* 清除筛选按钮样式 */
.clear-filters-btn {
  margin-left: auto; /* 自动左外边距，推至右侧 */
  cursor: pointer; /* 鼠标样式为手指 */
  color: #4c89a5; /* 默认字体颜色，灰色 */
  font-size: 12px; /* 字体较小 */
  user-select: none; /* 禁止文本选中 */
}

/* 文件卡片列表：使用 CSS Grid 自适应排列 */
.card-list {
  display: grid; /* 网格布局 */
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); /* 最小280px自适应，多列自动填充 */
  gap: 16px; /* 卡片之间间距 */
  overflow-y: auto; /* 内容超出时纵向滚动 */
  padding-right: 10px; /* 防止滚动条遮挡内容 */
  padding-top: 12px; /* 顶部内边距，防止遮挡 */
  padding-bottom: 12px; /* 顶部内边距，防止遮挡 */
}

/* 文件卡片整体样式 */
.file-card {
  border-radius: 12px; /* 卡片圆角 */
  border: 1px solid #e4e7ed; /* 边框颜色淡雅 */
  box-shadow: 0 1px 4px rgb(0 0 0 / 0.2); /* 初始阴影，增强层次 */
  transition: transform 0.2s ease, box-shadow 0.2s ease; /* 悬浮过渡动画 */
}

/* 文件卡片悬浮效果 */
.file-card:hover {
  transform: translateY(-2px); /* 轻微上移 */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08); /* 阴影加深，更加突出 */
}

/* 卡片头部：文件名和类型标签 */
.card-header {
  display: flex; /* 横向排列 */
  justify-content: space-between; /* 两端对齐 */
  margin-bottom: 8px; /* 底部间距 */
}

/* 文件名样式 */
.file-name {
  font-weight: 600; /* 字体加粗 */
  max-width: 180px; /* 可根据需要调整 */
  overflow: hidden; /* 超出部分隐藏 */
  text-overflow: ellipsis; /* 超出部分用省略号表示 */
  font-size: 15px; /* 字体大小 */
  white-space: nowrap; /* 不换行 */
  color: #181717; /* 深色，突出 */
}

/* 上传日期样式 */
.file-date {
  font-size: 12px; /* 字体较小 */
  color: #999; /* 浅灰色 */
  margin-bottom: 12px; /* 下方间距 */
}

/* 卡片操作按钮区域 */
.card-actions {
  display: flex; /* 横向排列按钮 */
  justify-content: flex-end; /* 靠右对齐 */
  gap: 1px; /* 按钮间距 */
}

/* PDF 预览占位符样式 */
.pdf-preview-placeholder {
  width: 100%; /* 宽度充满容器 */
  height: 100%; /* 高度充满容器 */
  border: 1px dashed #ccc; /* 虚线边框，提示用户这是预览区域 */
  display: flex; /* flex布局居中内容 */
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  color: #999; /* 文本颜色，浅灰 */
  font-size: 16px; /* 文本字号 */
  background: #f9f9fb; /* 浅灰背景，增强提示效果 */
  border-radius: 10px; /* 圆角 */
}
</style>
