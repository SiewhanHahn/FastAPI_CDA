import axios from 'axios';

// 创建 axios 实例
const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
  timeout: 5000,
});

// 请求拦截器：自动注入 JWT
api.interceptors.request.use(
  (config) => {
    // 从 localStorage 获取 Token
    // 安全说明：生产环境中为防御 XSS，更推荐 HttpOnly Cookie。
    // 此处作为课设演示，使用 localStorage 并配合严格的内容安全策略(CSP)
    const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// 响应拦截器：统一处理 401 未授权异常
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      // 捕获到 Token 失效，清理本地存储并重定向至登录页
      if (typeof window !== 'undefined') {
        localStorage.removeItem('access_token');
        window.location.href = '/login';
      }
    }
    return Promise.reject(error);
  }
);

export default api;