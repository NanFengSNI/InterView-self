import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/LoginPage.vue'
import BeforeInterview from '../views/BeforeInterview.vue'
import UserDetail from '../components/UserDetail.vue'
import ResumeSection from '../components/ResumeSection.vue'
import SkillAnalysis from '../components/SkillAnalysis.vue'
import JobRecommendation from '../components/JobRecommendation.vue'
import QuestionBank from '../components/QuestionBank.vue'
import LearningTest from '../components/LearningTest.vue'
import AIResume from '../components/AIResume.vue'

const routes = [
    { path: '/', component: BeforeInterview },
    { path: '/login', component: Login },
    {
        path: '/before-interview',
        component: BeforeInterview,
        redirect: '/before-interview/detail',
        children: [
        { path: 'detail', component: UserDetail },
        { path: 'resume', component: ResumeSection },
        { path: 'airesume', component: AIResume },
        { path: 'analysis', component: SkillAnalysis },
        { path: 'jobs', component: JobRecommendation },
        { path: 'questions', component: QuestionBank },
        { path: 'test', component: LearningTest }
        ]
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
