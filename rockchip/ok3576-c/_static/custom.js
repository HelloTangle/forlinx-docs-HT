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
    // 2) 左侧目录：保持用户手动展开状态
    // ---------------------------

    const expanded = JSON.parse(localStorage.getItem('forlinx-expanded') || '[]');

    // 恢复展开状态
    expanded.forEach(href => {
        const link = document.querySelector(`.wy-menu-vertical a[href="${href}"]`);
        if (link) {
            const li = link.closest('li.toctree-l1, li.toctree-l2');
            if (li) li.classList.add('current');
        }
    });

    // 绑定点击事件
    document.querySelectorAll('.wy-menu-vertical li.toctree-l1 > a, .wy-menu-vertical li.toctree-l2 > a').forEach(link => {
        const subMenu = link.parentElement.querySelector('ul');
        const href = link.getAttribute('href');

        if (subMenu) {
            link.addEventListener('click', function(e) {
                // 若链接为空或为锚点，则只展开折叠，不跳转
                if (!href || href === '#' || href === '') {
                    e.preventDefault();
                } else {
                    // 链接正常的情况下仍允许跳转（让用户能进该页）
                    // 但加一个轻微延迟，以确保点击时仍能记录展开状态
                    setTimeout(() => { window.location = href; }, 80);
                }

                // 切换展开状态
                const li = this.parentElement;
                li.classList.toggle('current');

                // 更新 localStorage
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
});
