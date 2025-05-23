<template>
  <!-- <div class="document-center"> -->
            <p class="description" style="font-size: 18px; color: #606266; line-height: 1.6; font-weight: 600;">
              上传您的简历、求职信或其他求职材料，AI 将帮助您优化文档结构、突出亮点，在求职过程中脱颖而出
            </p>
            
            <div class="action-buttons">
              <el-button type="primary">
                <el-icon :size="18" style="margin-right: 6px;">
                  <Upload/>
                </el-icon>
                上传文件</el-button>
                
              <el-button plain>
                <el-icon :size="18" style="margin-right: 6px;">
                  <DocumentAdd/>
                </el-icon>
                使用 AI 简历生成器创建</el-button>
            </div>

            <el-table :data="documents" class="doc-table" style="width: 100%">
              <el-table-column type="selection" />
              <el-table-column label="文件名" prop="name" />
              <el-table-column label="职位" prop="job" />
              <el-table-column label="职位详情" prop="jobdetail" />
              <el-table-column label="公司" prop="company" />
              <el-table-column label="公司详情" prop="companydetail" />
              <el-table-column label="文档类型" prop="type" />
              <el-table-column label="上传日期" prop="uploadDate" />
              <el-table-column label="">
                <template #default="scope">
                  <el-button icon= "MagicStick" size="small" @click="edit(scope.row)">AI 编辑</el-button>
                  <el-button icon="Download" size="small" @click="download(scope.row)" />
                  <el-button icon="Delete" type="danger" size="small" @click="remove(scope.row)" />
                </template>
              </el-table-column>
            </el-table>

            <el-pagination layout="prev, pager, next" :total="1" :page-size="10" class="mt-4" />
          <!-- </div> -->
</template>

<script setup>
import { MagicStick, Download, Delete, DocumentAdd, Upload } from '@element-plus/icons-vue'

const documents = [
  {
    name: '1.pdf',
    job: '算法工程师',
    jobdetail: '负责算法模型的设计',
    company: '某科技公司',
    companydetail: '国内领先的人工智能公司',
    type: '简历',
    uploadDate: '2025-05-15',
  },
  {
    name: '2.pdf',
    job: '全栈工程师',
    jobdetail: '负责全栈开发与系统设计',
    company: '某互联网公司',
    companydetail: '国内知名互联网公司',
    type: '简历',
    uploadDate: '2025-05-15',
  },
]
const edit = (row) => {
  console.log('AI 编辑：', row)
}
const download = (row) => {
  console.log('下载：', row)
}
const remove = (row) => {
  console.log('删除：', row)
}
</script>
