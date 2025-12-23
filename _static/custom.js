document.addEventListener('DOMContentLoaded', function() {
    // 1. 获取相关的 DOM 元素
    var navButton = document.querySelector('[data-toggle="wy-nav-top"]');
    var navSide = document.querySelector('.wy-nav-side');
    var contentWrap = document.querySelector('.wy-nav-content-wrap');

    if (navButton) {
        // 使用更高级别的拦截，防止 RTD 原生 theme.js 的干扰
        navButton.addEventListener('click', function(e) {
            e.preventDefault(); // 核心：阻止 href="#" 跳转
            e.stopImmediatePropagation(); // 核心：阻止其他 JS 脚本（如原主题脚本）运行

            // 模拟 RTD 的标准切换行为
            document.body.classList.toggle('shift');
            navSide.classList.toggle('shift');
            if (contentWrap) contentWrap.classList.toggle('shift');
        }, true); // 注意这里的 true，使用事件捕获优先拦截
    }

    // 2. 手势滑动收回逻辑
    var touchStartX = 0;
    document.addEventListener('touchstart', function(e) {
        touchStartX = e.changedTouches[0].screenX;
    }, {passive: true});

    document.addEventListener('touchend', function(e) {
        var touchEndX = e.changedTouches[0].screenX;
        // 如果向左滑动超过 80px，且菜单当前是打开状态
        if (touchStartX - touchEndX > 80 && document.body.classList.contains('shift')) {
            document.body.classList.remove('shift');
            navSide.classList.remove('shift');
            if (contentWrap) contentWrap.classList.remove('shift');
        }
    }, {passive: true});
});