

document.addEventListener('DOMContentLoaded', function() {
    // ---------------------------
    // 1) Logo 强制跳转（兜底）
    // ---------------------------
    var imgs = document.querySelectorAll('img[src*="forlinx-logo"]');
    imgs.forEach(function(img) {
        var a = img.closest('a');
        if(a) a.href = 'https://hellotangle.github.io/forlinx-docs-HT/';
    });

    // ---------------------------
    // 2) 左侧目录折叠逻辑
    // ---------------------------
    setTimeout(function() {
        var toctreeLinks = document.querySelectorAll(
            '.wy-menu-vertical li.toctree-l1 > a, .wy-menu-vertical li.toctree-l2 > a'
        );

        toctreeLinks.forEach(function(link){
            link.addEventListener('click', function(e){
                var parentLi = link.parentElement;
                parentLi.classList.toggle('current'); // 切换当前目录展开/折叠
                e.stopPropagation(); // 阻止主题 JS 自动折叠其他目录
            }, true);
        });
    }, 500); // 延迟绑定确保覆盖主题内部 JS
});
