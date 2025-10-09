document.addEventListener('DOMContentLoaded', function() {
    // ---------------------------
    // 1) Logo 强制跳转（兜底）
    // ---------------------------
    var imgs = document.querySelectorAll('img[src*="forlinx-logo"]');
    imgs.forEach(function(img) {
        var a = img.closest('a');
        if (a) a.href = 'https://hellotangle.github.io/forlinx-docs-HT/';
    });

    // ---------------------------
    // 2) 左侧目录：支持多项展开 + 状态记忆
    // ---------------------------

    // 从 localStorage 读取上次展开的目录项
    const expandedSet = new Set(JSON.parse(localStorage.getItem('forlinx-expanded') || '[]'));

    // 初始化展开状态
    document.querySelectorAll('.wy-menu-vertical li.toctree-l1, .wy-menu-vertical li.toctree-l2').forEach(function(li) {
        const id = li.querySelector('a')?.getAttribute('href');
        if (id && expandedSet.has(id)) {
            li.classList.add('current'); // 展开之前展开过的
        }
    });

    // 点击目录时切换展开状态
    document.querySelectorAll('.wy-menu-vertical li.toctree-l1 > a, .wy-menu-vertical li.toctree-l2 > a').forEach(function(link) {
        link.addEventListener('click', function(event) {
            const parentLi = this.parentElement;
            const subMenu = parentLi.querySelector('ul');
            const id = this.getAttribute('href');

            if (subMenu) {
                event.preventDefault(); // 阻止默认跳转
                parentLi.classList.toggle('current'); // 切换展开状态

                // 更新 localStorage 中的记录
                if (id) {
                    if (parentLi.classList.contains('current')) {
                        expandedSet.add(id);
                    } else {
                        expandedSet.delete(id);
                    }
                    localStorage.setItem('forlinx-expanded', JSON.stringify([...expandedSet]));
                }
            }
        });
    });
});
