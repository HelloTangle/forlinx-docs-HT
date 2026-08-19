Welcome to EmbedSBC
====================

.. raw:: html

  <!-- 🌟 顶部头条 Banner (Hero Section) -->
  <section class="banner-news">
    <div class="banner-content">
      <span class="category-tag">Welcome</span>
      <h1>Master Your Embedded Hardware Design</h1>
      <p>Delivering hardcore engineering insights, hardware architecture analysis, and cross-platform migration strategies for the global embedded community.</p>
      <a href="https://www.embedsbc.com/" class="btn-read-more" target="_blank">Discover embedSBC</a>
    </div>
  </section>

----


Latest Tech Insights
=====================

.. raw:: html

   <!-- 创建一个空的容器用于放置动态加载的文章卡片 -->
   <div class="news-grid-container" id="dynamic-news-container">
     <!-- 这里的初始内容作为骨架屏或加载提示，数据返回后会被覆盖 -->
     <div style="text-align: center; padding: 40px; color: #888; width: 100%;">
        Loading latest insights from embedsbc.com...
     </div>
   </div>

   <script>
   document.addEventListener("DOMContentLoaded", function() {
       // WordPress REST API 地址：获取最新9篇文章，_embed 用于获取特色图片(缩略图)数据
       const apiUrl = 'https://embedsbc.com/wp-json/wp/v2/posts?_embed&per_page=9';
       
       fetch(apiUrl)
           .then(response => {
               if (!response.ok) {
                   throw new Error('Network response was not ok');
               }
               return response.json();
           })
           .then(posts => {
               const container = document.getElementById('dynamic-news-container');
               container.innerHTML = ''; // 清空加载提示
               
               posts.forEach(post => {
                   // 获取标题和链接
                   const title = post.title.rendered;
                   const link = post.link;
                   
                   // 格式化日期 (例如：August 05, 2026)
                   const dateObj = new Date(post.date);
                   const dateOptions = { year: 'numeric', month: 'long', day: '2-digit' };
                   const formattedDate = dateObj.toLocaleDateString('en-US', dateOptions);
                   
                   // 获取摘要，并去除自带的HTML标签，截断字符保持卡片整洁
                   let excerpt = post.excerpt.rendered.replace(/<[^>]+>/g, '').trim();
                   if(excerpt.length > 100) excerpt = excerpt.substring(0, 100) + '...';
                   
                   // 获取缩略图，如果没有则使用默认占位图
                   let imageUrl = '_static/images/news/default_thumbnail.jpg'; // 请确保准备一张默认图
                   if (post._embedded && post._embedded['wp:featuredmedia'] && post._embedded['wp:featuredmedia'][0].source_url) {
                       imageUrl = post._embedded['wp:featuredmedia'][0].source_url;
                   }
                   
                   // 构建单个卡片的 HTML 结构
                   const cardHtml = `
                     <div class="news-card">
                       <a href="${link}" target="_blank">
                         <img src="${imageUrl}" alt="${title}" class="news-thumbnail" />
                       </a>
                       <div class="news-content">
                         <span class="news-date">${formattedDate}</span>
                         <h3 class="news-title">${title}</h3>
                         <p class="news-excerpt">${excerpt}</p>
                         <a href="${link}" target="_blank" class="link-more">Read More &rarr;</a>
                       </div>
                     </div>
                   `;
                   
                   // 将卡片插入容器
                   container.insertAdjacentHTML('beforeend', cardHtml);
               });
           })
           .catch(error => {
               console.error('Error fetching latest posts:', error);
               document.getElementById('dynamic-news-container').innerHTML = 
                   '<div style="text-align:center; width:100%; color:#888;">Unable to load latest insights at this time. Please visit <a href="https://embedsbc.com" target="_blank">embedsbc.com</a> directly.</div>';
           });
   });
   </script>





----

About embedSBC
===============

Delivering hardcore engineering insights, cross-platform migration strategies, and technical documentation for the global embedded community. 

- **Contact Us**: `jason@embedsbc.com <mailto:jason@embedsbc.com>`_
