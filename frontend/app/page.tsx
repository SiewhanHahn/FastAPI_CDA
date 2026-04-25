'use client';

import { useEffect, useState } from 'react';
import api from '@/utils/api';

// 定义与后端 Schema 对应的数据结构
interface Article {
  id: number;
  title: string;
  summary: string;
  gmt_create: string;
}

export default function Home() {
  const [articles, setArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await api.get('/articles/');
        setArticles(response.data);
      } catch (error) {
        console.error('获取文章失败:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchArticles();
  }, []);

  if (loading) return <div className="text-center mt-20">加载中...</div>;

  return (
    <main className="max-w-4xl mx-auto p-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-gray-900">技术博客</h1>
        <a href="/login" className="text-blue-600 hover:underline">去控制台发布</a>
      </div>

      <div className="space-y-6">
        {articles.length === 0 ? (
          <p className="text-gray-500">暂无文章</p>
        ) : (
          articles.map((article) => (
            <article key={article.id} className="p-6 bg-white rounded-lg shadow-sm border">
              <h2 className="text-xl font-semibold mb-2">{article.title}</h2>
              <p className="text-gray-600 mb-4">{article.summary || '暂无摘要...'}</p>
              <div className="text-sm text-gray-400">
                发布时间: {new Date(article.gmt_create).toLocaleDateString()}
              </div>
            </article>
          ))
        )}
      </div>
    </main>
  );
}