
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
    document.querySelectorAll('.wy-menu-vertical li.toctree-l1, .wy-menu-vertical li.toctree-l2').forEach(function(li){
        li.classList.add('current'); // 强制全部展开
    });
    
});
