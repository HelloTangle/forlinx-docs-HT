document.addEventListener('DOMContentLoaded', function() {

    // ---------------------------
    // 1) Logo 强制跳转
    // ---------------------------
    var imgs = document.querySelectorAll('img[src*="forlinx-logo"]');
    imgs.forEach(function(img) {
        var a = img.closest('a');
        if(a) a.href = 'https://hellotangle.github.io/forlinx-docs-HT/';
    });

    // ---------------------------
    // 2) 左侧目录多项保持展开
    // ---------------------------
    var toctreeLinks = document.querySelectorAll('.wy-menu-vertical li.toctree-l1 > a, .wy-menu-vertical li.toctree-l2 > a');

    toctreeLinks.forEach(function(link){
        link.addEventListener('click', function(e){
            var parentLi = link.parentElement;
            parentLi.classList.toggle('current');
            e.stopPropagation();
        }, true);
    });

});
