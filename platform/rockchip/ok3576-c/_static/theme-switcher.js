document.addEventListener("DOMContentLoaded", function () {
    let currentTheme = localStorage.getItem("doc-theme") || "light";

    function applyTheme(theme) {
        document.body.className = document.body.className.replace(/theme-\w+/g, "");
        document.body.classList.add(`theme-${theme}`);
        updateButtonLabel();
        document.body.style.transition = "background-color 0.3s, color 0.3s";
    }

    function updateButtonLabel() {
        const btn = document.getElementById("theme-switcher-btn");
        if (!btn) return;

        if (currentTheme === "light") {
            btn.textContent = "🌙 Dark Mode"; // 当前是 light，按钮显示切换到暗色
        } else {
            btn.textContent = "🌞 Light Mode"; // 当前是 dark，按钮显示切换到亮色
        }
    }

    function createButton() {
        const container = document.createElement("div");
        container.id = "theme-switcher";

        const btn = document.createElement("button");
        btn.id = "theme-switcher-btn";
        btn.style.cssText = `
            padding: 6px 10px;
            background: var(--theme-btn-bg);
            color: var(--theme-btn-fg);
            border: 1px solid var(--theme-border);
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            transition: background 0.3s, color 0.3s;
        `;

        btn.onclick = () => {
            currentTheme = currentTheme === "light" ? "dark" : "light";
            localStorage.setItem("doc-theme", currentTheme);
            applyTheme(currentTheme);
        };

        container.appendChild(btn);
        document.body.appendChild(container);

        updateButtonLabel();
    }

    applyTheme(currentTheme);
    createButton();
});
