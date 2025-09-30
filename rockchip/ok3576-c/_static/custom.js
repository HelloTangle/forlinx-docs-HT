

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
        var lis = document.querySelectorAll('.wy-menu-vertical li.toctree-l1, .wy-menu-vertical li.toctree-l2');
    
        // 克隆节点，去掉主题原事件绑定
        lis.forEach(function(li) {
            var newLi = li.cloneNode(true);
            li.parentNode.replaceChild(newLi, li);
        });
    
        // 重新绑定点击事件
        var toctreeLinks = document.querySelectorAll('.wy-menu-vertical li.toctree-l1 > a, .wy-menu-vertical li.toctree-l2 > a');
        toctreeLinks.forEach(function(link) {
            link.addEventListener('click', function(e){
                var parentLi = link.parentElement;
                parentLi.classList.toggle('current'); // 切换当前目录展开/折叠
                e.stopPropagation(); // 阻止冒泡
            });
        });
    }, 500);
    
});
