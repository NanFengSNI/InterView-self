<template>
  <div class="pdf-preview">
    <div ref="pdfContainer" class="pdf-container"></div>
  </div>
</template>

<script setup>
import { onMounted, watch, ref, nextTick } from 'vue'
import * as pdfjsLib from 'pdfjs-dist'

// ✅ 使用 CDN 的 worker 路径
pdfjsLib.GlobalWorkerOptions.workerSrc = `https://cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjsLib.version}/pdf.worker.min.js`

const props = defineProps({
  fileUrl: String
})

const pdfContainer = ref(null)

watch(() => props.fileUrl, (newUrl) => {
  if (newUrl) {
    renderPDF(newUrl)
  }
})

async function renderPDF(url) {
  // 清空之前的内容
  pdfContainer.value.innerHTML = ''

  let data
  if (url.startsWith('blob:')) {
    const response = await fetch(url)
    data = await response.arrayBuffer()
  } else {
    data = url // 网络 PDF 地址
  }

  const loadingTask = pdfjsLib.getDocument({ data })
  const pdf = await loadingTask.promise
  const totalPages = pdf.numPages

  for (let pageNumber = 1; pageNumber <= totalPages; pageNumber++) {
    const page = await pdf.getPage(pageNumber)
    const viewport = page.getViewport({ scale: 1.5 })

    await nextTick()
    const canvas = document.createElement('canvas')
    const context = canvas.getContext('2d')

    canvas.height = viewport.height
    canvas.width = viewport.width
    canvas.style.marginBottom = '20px'

    pdfContainer.value.appendChild(canvas)

    await page.render({
      canvasContext: context,
      viewport: viewport
    }).promise
  }
}

onMounted(() => {
  if (props.fileUrl) {
    renderPDF(props.fileUrl)
  }
})
</script>


<style scoped>
.pdf-preview {
  width: 100%;
  height: 100%;
  overflow: auto;
  display: flex;
  justify-content: center;
  padding: 10px 1px 10px 10px; /* 内边距：上右下左 */
  background-color: #f8f8f8;
}

canvas {
  border: 1px solid #ccc;
}
</style>
