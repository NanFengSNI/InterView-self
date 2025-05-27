<template>
  <div class="app-container">
  <!-- 顶部导航栏 -->
    <header class="header">
      <div class="logo">SmartSenseSystem<span class="highlight">AI</span></div>
      <nav class="nav-links">
        <a href="#">产品</a>
        <a href="#">特性</a>
        <a href="#">团队</a>
        <a href="#">联系我们</a>
      </nav>
    </header>
    <!-- 顶部 Hero 区 -->
    <section class="hero">
      <h1>欢迎来到 <span class="highlight">SSS AI InterView
      </span></h1>
      <p>你的 AI 面试助理，助你决胜终面</p>
      <router-link to="/login">
        <el-button type="primary" size="large">🚀 开始模拟面试</el-button>
      </router-link>

    </section>

    <!-- 功能 1 -->
    <section class="feature">
      <div class="text">
        <h2>🎯 AI 智能面试官</h2>
        <p>基于大模型驱动的对话模拟，精准评估回答内容。</p>
      </div>
      <div class="image">
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHBlbWNud2ZnZXIxN2dxeHhsYWJxaWxoZHF5OWZybm05NmpvbmMxMyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/FMnR1XZnRpaY4jGC3n/giphy.gif" alt="AI Interview Bot">
      </div>
    </section>

    <!-- 功能 2 -->
    <section class="feature reverse">
      <div class="text">
        <h2>🎥 表情与情绪分析</h2>
        <p>通过视频分析你的紧张度、眼神交流与微表情变化。</p>
      </div>
      <div class="image">
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGZobDdhbGE5djBjcHNua3gxZ3Vvd3hscHFuZnZ6ZHFna2ZmcHRybCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/5xtDarIN81PtxfYiPE8/giphy.gif" alt="Emotion Analysis">
      </div>
    </section>

    <!-- 功能 3 -->
    <section class="feature">
      <div class="text">
        <h2>🧠 GPT 助教引导</h2>
        <p>通过 GPT 智能提示与评分机制，获得实时反馈与优化建议。</p>
      </div>
      <div class="image">
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGV4cWQ1YTR5OHNpdjQ4eXo5eDQweG9iM2UwMGN1ZnY5YmJjZWg3bSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/jUwpNzg9IcyrK/giphy.gif" alt="GPT Assistant">
      </div>
    </section>

    <!-- 底部开发者展示 -->
    <section class="team">
      <h2>👨‍💻 开发团队</h2>
      <div class="avatars">
        <div class="dev">
          <img src="https://i.pravatar.cc/100?img=3" alt="Dev1">
          <p>张伟</p>
        </div>
        <div class="dev">
          <img src="https://i.pravatar.cc/100?img=5" alt="Dev2">
          <p>李娜</p>
        </div>
        <div class="dev">
          <img src="https://i.pravatar.cc/100?img=7" alt="Dev3">
          <p>王强</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>

</script>

<style scoped>
.app-container {
  font-family: 'Inter', sans-serif;
  scroll-behavior: smooth;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.2rem 2rem;
  background-color: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.logo {
  font-size: 1.6rem;
  font-weight: bold;
  color: #333;
}

.highlight {
  color: #409EFF; /* Element Plus 主色 */
}

.nav-links a {
  margin-left: 1.5rem;
  text-decoration: none;
  color: #555;
  font-weight: 500;
}

.nav-links a:hover {
  color: #409EFF;
}

section {
  padding: 5rem 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}

/* 顶部 hero */
.hero {
  flex-direction: column;
  text-align: center;
  background: linear-gradient(135deg, #eef4ff, #ffffff);
}

.hero h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.hero p {
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
  color: #666;
}

.highlight {
  color: #409EFF;
}

/* 功能模块 */
.feature {
  flex-direction: row;
  gap: 2rem;
}

.feature.reverse {
  flex-direction: row-reverse;
}

.feature .text {
  flex: 1;
  min-width: 250px;
}

.feature h2 {
  font-size: 1.6rem;
  margin-bottom: 0.5rem;
}

.feature p {
  font-size: 1rem;
  color: #444;
}

.feature .image {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.feature .image img {
  max-width: 100%;
  max-height: 300px;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0,0,0,0.08);
}

/* 开发者区 */
.team {
  flex-direction: column;
  text-align: center;
  background: #f8f9fb;
}

.avatars {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-top: 2rem;
}

.dev {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.dev img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.dev p {
  margin-top: 0.5rem;
  font-weight: 500;
}
</style>
