document.addEventListener('DOMContentLoaded', function() {
    // 1) Logo 兜底跳转
    var imgs = document.querySelectorAll('img[src*="forlinx-logo"]');
    imgs.forEach(function(img) {
        var a = img.closest('a');
        if (a) a.href = 'https://hellotangle.github.io/forlinx-docs-HT/';
    });

    // 2) 延迟恢复展开状态（等 RTD 初始化完毕）
    setTimeout(() => {
        const expanded = JSON.parse(localStorage.getItem('forlinx-expanded') || '[]');

        expanded.forEach(href => {
            const link = document.querySelector(`.wy-menu-vertical a[href="${href}"]`);
            if (link) {
                const li = link.closest('li.toctree-l1, li.toctree-l2');
                if (li) li.classList.add('current');
            }
        });

        // 点击事件绑定
        document.querySelectorAll('.wy-menu-vertical li.toctree-l1 > a, .wy-menu-vertical li.toctree-l2 > a').forEach(link => {
            const subMenu = link.parentElement.querySelector('ul');
            const href = link.getAttribute('href');

            if (subMenu) {
                link.addEventListener('click', function(e) {
                    e.preventDefault();
                    const li = this.parentElement;
                    li.classList.toggle('current');

                    let list = JSON.parse(localStorage.getItem('forlinx-expanded') || '[]');
                    if (li.classList.contains('current')) {
                        if (!list.includes(href)) list.push(href);
                    } else {
                        list = list.filter(i => i !== href);
                    }
                    localStorage.setItem('forlinx-expanded', JSON.stringify(list));
                });
            }
        });
    }, 400); // 延迟 400ms，等 RTD 自带脚本执行完
});
