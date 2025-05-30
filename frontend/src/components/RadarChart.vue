<template>
  <div ref="chartContainer" class="chart-container"></div>
</template>

<script setup>
import * as echarts from 'echarts'
import { onMounted, ref, onBeforeUnmount, nextTick } from 'vue'

const chartContainer = ref(null)
let chartInstance = null

// 示例数据
const scores = [98, 98, 67, 95, 85]
const labels = ['沟通能力', '技术能力', '学习能力', '创新能力', '应变能力']

// 动态设置字体大小和颜色
const getFontSize = (value) => 12 + (value / 100) * 10 // 基础大小 + 比例增量
const getColor = (value) => {
  if (value > 85) return '#67C23A'   // 绿色
  if (value > 70) return '#E6A23C'   // 橙色
  return '#F56C6C'                   // 红色
}

const initChart = () => {
  if (!chartContainer.value) return
  chartInstance = echarts.init(chartContainer.value)

  chartInstance.setOption({
    //  // 图表标题配置
    // title: {
    //   text: '综合能力雷达图',
    //   left: 'center',
    //   top: 10,
    //   textStyle: {
    //     fontSize: 24,
    //     fontWeight: 'bold',
    //     color: '#333'
    //   }
    // },
    // 提示框（鼠标悬浮时显示）
    tooltip: {
      trigger: 'item',
      formatter: function (params) {
      const values = params.value
      const name = params.seriesName || '能力评分'
      let html = `<strong>${name}</strong><br/>`
      labels.forEach((label, index) => {
        html += `${label}：<span style="color:#409EFF;font-weight:bold;">${values[index]}</span><br/>`
      })
      return html
      }
    },
    radar: {
      radius: '75%', // 雷达比例
      center: ['50%', '50%'], // 雷达显示位置
      splitNumber: 5,    // 分割圈数
      shape: 'circle',
      indicator: labels.map((label, i) => ({
        name: `{a${i}|${label}}`,
        max: 100
      })),
      name: {
        rich: labels.reduce((acc, label, i) => {
          acc[`a${i}`] = {
            color: getColor(scores[i]),
            fontSize: '21px',
            fontWeight: 'bold',
            align: 'center',
            fontFamily: 'KaiTi' // 使用楷体
          }
          return acc
        }, {})
      }
    },
    series: [{
      type: 'radar',
      name: '能力评分',
      areaStyle: {
        // color: 'rgba(102, 177, 255, 0.3)' // 纯色填充
        // 或者使用渐变色
        color: {
          type: 'linear',
          x: 0, y: 0, x2: 0, y2: 1,
          colorStops: [
            { offset: 0, color: 'rgba(102, 177, 255, 0.5)' },
            { offset: 1, color: 'rgba(102, 177, 255, 0.1)' }
          ]
        }
      },
      data: [{
        value: scores,
        name: '能力评分'
      }]
    }]
  })
}

let resizeObserver = null

const resizeChart = () => {
  chartInstance?.resize()
}

onMounted(() => {
 nextTick(() => {
    initChart()
    resizeObserver = new ResizeObserver(() => {
      chartInstance?.resize()
    })
    if (chartContainer.value) {
      resizeObserver.observe(chartContainer.value)
    }
  })
})

onBeforeUnmount(() => {
  resizeObserver?.disconnect()
  chartInstance?.dispose()
})
</script>

<style scoped>
.chart-container {
  width: 100%;
  height: 400px;
  /* margin-top: 20px; 给图表顶部加一点空隙 */
}
</style>
