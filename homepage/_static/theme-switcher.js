document.addEventListener("DOMContentLoaded", function () {
    const themes = {
        light: "浅色",
        dark: "深色",
    };

    // 获取当前主题（从 localStorage）
    const savedTheme = localStorage.getItem("doc-theme") || "light";

    // 应用主题
    function applyTheme(themeKey) {
        document.body.className = document.body.className.replace(/theme-\w+/g, "");
        document.body.classList.add(`theme-${themeKey}`);
        updateButtonLabel(themeKey);
    }

    // 更新按钮文字
    function updateButtonLabel(themeKey) {
        const btn = document.getElementById("theme-switcher-btn");
        if (btn) btn.textContent = `🎨 ${themes[themeKey]}`;
    }

    // 创建下拉菜单
    function createDropdown() {
        const container = document.createElement("div");
        container.id = "theme-switcher";
        container.style.cssText = `
            position: fixed;
            top: 10px;
            right: 10px;
            z-index: 9999;
            font-size: 14px;
        `;

        const btn = document.createElement("button");
        btn.id = "theme-switcher-btn";
        btn.textContent = `🎨 ${themes[savedTheme]}`;
        btn.style.cssText = `
            padding: 6px 10px;
            background: var(--theme-btn-bg);
            color: var(--theme-btn-fg);
            border: 1px solid var(--theme-border);
            border-radius: 4px;
            cursor: pointer;
        `;

        const dropdown = document.createElement("div");
        dropdown.id = "theme-dropdown";

        Object.keys(themes).forEach(key => {
            const item = document.createElement("div");
            item.textContent = themes[key];
            item.style.cssText = `
                padding: 8px 12px;
                cursor: pointer;
            `;
            item.onmouseover = () => item.style.backgroundColor = "var(--theme-link)";
            item.onmouseout = () => item.style.backgroundColor = "transparent";
            item.onclick = () => {
                localStorage.setItem("doc-theme", key);
                applyTheme(key);
                dropdown.style.display = "none";
            };
            dropdown.appendChild(item);
        });

        container.appendChild(btn);
        container.appendChild(dropdown);

        // 切换下拉
        btn.onclick = () => {
            dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
        };

        // 点击外部关闭
        document.addEventListener("click", (e) => {
            if (!container.contains(e.target)) {
                dropdown.style.display = "none";
            }
        });

        document.body.appendChild(container);
    }

    // 初始化
    applyTheme(savedTheme);
    createDropdown();
});