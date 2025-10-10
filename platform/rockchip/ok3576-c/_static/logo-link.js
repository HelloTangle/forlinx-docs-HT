// _static/logo-link.js

document.addEventListener("DOMContentLoaded", function () {
    const logoImg = document.querySelector("img.logo");
    if (logoImg) {
        // 检查父元素是否已经是链接
        if (logoImg.parentElement.tagName == 'A') {
            const link = logoImg.parentElement;
            link.href = "https://hellotangle.github.io/forlinx-docs-HT/";  // 你要跳转的地址
            link.target = "_self";
        }
    }
});