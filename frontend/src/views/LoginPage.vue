<!-- src/views/LoginPage.vue -->
<template>
  <div class="login-page">
    <el-card class="login-card" shadow="always">
      <h2>登录 / 注册</h2>
      <el-form :model="loginForm" label-width="80px">
        <el-form-item label="用户名">
          <el-input v-model="loginForm.username" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="loginForm.password" type="password" />
        </el-form-item>
        <el-form-item>
          <el-checkbox v-model="loginForm.isRegister">注册模式</el-checkbox>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleLogin">
            {{ loginForm.isRegister ? '注册' : '登录' }}
          </el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import axios from 'axios'

const router = useRouter()
const loginForm = reactive({
  username: '',
  password: '',
  isRegister: false
})

const handleLogin = async () => {
  try {
    const url = loginForm.isRegister ? '/api/register' : '/api/login'
    const res = await axios.post(url, {
      username: loginForm.username,
      password: loginForm.password
    })

    if (res.data.success) {
      localStorage.setItem('isLoggedIn', 'true')
      localStorage.setItem('username', loginForm.username)
      ElMessage.success('登录成功')
      router.push('/') // 跳转主页
    } else {
      ElMessage.error(res.data.message || '登录失败')
    }
  } catch {
    ElMessage.error('请求失败，请检查网络')
  }
}
</script>

<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #f4f4f4;
}
.login-card {
  width: 400px;
}
</style>
