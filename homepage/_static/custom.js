document.addEventListener("DOMContentLoaded", function() {
    const menuBtn = document.querySelector(".wy-nav-top .fa-bars");
    const body = document.body;

    if (menuBtn) {
        menuBtn.addEventListener("click", function(e) {
            e.preventDefault(); // 阻止跳到顶部
            body.classList.toggle("wy-nav-side-shift");
        });
    }
});
