// nav_index.js

// === 1. EDIT YOUR ARTICLES & CATEGORIES HERE ===
const siteTitle = ""; // Leave as "" if you don't want a title above the tabs

// Add or edit the "description" field on any item below to show a hover box.
// Leave description as "" (or omit it) if you don't want a hover box on that tab.
const menuData = [
    {
        title: "主页",
        url: "index.html",
        description: "返回网站首页"
    },
    {
        title: "社会/民主",
        url: "society.html",
        description: "激发思考的文章，专家的意见很多时候和一般人直观相反，例如民主，言论自由等等"
    },
    {
        title: "明辨是非",
        url: "debate.html",
        description: "通过辩论了解对方观点，明白真理"
    },
    {
        title: "文革",
        url: "wenge.html",
        description: "近代中国最沉重的一章，本栏加入外国类似事例，帮助读者明白学习文革的意义"
    },
    {
        title: "毛泽东年代",
        url: "mao.html",
        description: "文革意外发生在毛年代的事"
    },
    {
        title: "人物",
        url: "people.html",
        description: "关于历史人物"
    },
    {
        title: "外国历史",
        url: "foreign_history.html",
        description: "发生于外国，值得我们学习的事情"
    },
    {
        title: "其他",
        url: "mis.html",
        description: "其他类型文章"
    },
    {
        title: "我的文章",
        description: "短日记关于我平时看的新闻，长文章是我一些观察或记录，历史游记是我去过一些历史地方的记录",
        subItems: [
            { title: "短日记", url: "short_diary.html" },
            { title: "长文章", url: "long_diary.html"},
            { title: "历史游记", url: "history_journal.html" },
    
        ]
    },
    {
        title: "有用资料",
        url: "links.html",
        description: "学习中国近代史的资源，还有炎黄春秋epub"
    }
];

// === 2. INJECT TAB MENU & STYLES AUTOMATICALLY ===
function renderHeader() {
    // Support either <header id="site-header"> or <div id="site-index-container">
    const headerEl = document.getElementById("site-header") || document.getElementById("site-index-container");
    if (!headerEl) return;

    // Detect current page filename to highlight the active tab automatically
    const currentPage = window.location.pathname.split("/").pop() || "index.html";

    const tabsHtml = menuData.map((item) => {
        const tooltipHtml = item.description
            ? `<span class="tab-tooltip">${item.description}</span>`
            : "";

        // Case A: Category tab with dropdown articles
        if (item.subItems && item.subItems.length > 0) {
            const isParentActive = item.subItems.some(sub => sub.url === currentPage);
            const subLinks = item.subItems.map(sub => {
                const isSubActive = (sub.url === currentPage) ? 'class="active-sub"' : '';
                const subTitleAttr = sub.description ? `title="${sub.description}"` : '';
                return `<li><a href="${sub.url}" ${isSubActive} ${subTitleAttr}>${sub.title}</a></li>`;
            }).join("");

            return `
                <li class="has-dropdown ${isParentActive ? 'active' : ''}">
                    <a href="javascript:void(0)" onclick="toggleTabDropdown(event, this)">
                        ${item.title} <span class="tab-arrow">▾</span>
                    </a>
                    ${tooltipHtml}
                    <ul class="tab-dropdown">${subLinks}</ul>
                </li>`;
        }
        // Case B: Direct single link tab
        else {
            const isActive = (item.url === currentPage) ? 'class="active"' : '';
            return `
                <li ${isActive}>
                    <a href="${item.url}">${item.title}</a>
                    ${tooltipHtml}
                </li>`;
        }
    }).join("");

    headerEl.innerHTML = `
        <style>
            .tab-nav-wrapper {
                font-family: 'Roboto', 'Helvetica Neue', Helvetica, Arial, sans-serif;
                margin-bottom: 20px;
            }
            .site-title-bar {
                text-align: center;
                padding: 12px 0 8px 0;
            }
            .site-title-bar a {
                text-decoration: none;
                color: #0069A3;
                font-size: 1.5rem;
                font-weight: bold;
                font-family: Georgia, serif;
            }

            /* === SEARCH AREA === */
            .container-search {
                text-align: right;
                padding: 10px 24px;
                background-color: #ffffff;
                border: none;
            }
            #search-box {
                width: 260px;
                padding: 8px 12px;
                font-size: 16px;
                background-color: #ffffff;
                border: 1px solid #cbd5e1;
                border-radius: 4px;
                vertical-align: middle;
                font-family: inherit;
            }
            #search-button {
                padding: 8px 16px;
                font-size: 16px;
                font-weight: bold;
                color: #ffffff;
                background-color: #0069A3;
                border: 1px solid #0069A3;
                border-radius: 4px;
                cursor: pointer;
                vertical-align: middle;
                margin-left: 4px;
                font-family: inherit;
                transition: background-color 0.2s;
            }
            #search-button:hover {
                background-color: #cc3600;
                border-color: #cc3600;
            }
            #search-results {
                text-align: left;
            }

            /* === THE MENU BAR (Matching yhcqw.github.io/yhcq/) === */
            .botmenu-bar {
                background-color: #0069A3;
                border-top: none;
                border-bottom: 3px solid #005080;
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                padding: 0;
                margin: 0;
                list-style: none;
            }
            .botmenu-bar > li {
                margin: 0;
                position: relative;
            }
            .botmenu-bar > li > a {
                display: inline-block;
                padding: 10px 16px;
                color: #ffffff;
                text-decoration: none;
                font-size: 16px;           /* Keeping original font size */
                font-family: 'Roboto', 'Helvetica Neue', Helvetica, Arial, sans-serif;
                font-weight: normal;
                border-right: 1px solid rgba(255, 255, 255, 0.15);
                transition: background-color 0.2s, color 0.2s;
            }
            .botmenu-bar > li:first-child > a {
                border-left: 1px solid rgba(255, 255, 255, 0.15);
            }
            /* Hover & Active States */
            .botmenu-bar > li > a:hover {
                background-color: #005585;
                color: #ffffff;
            }
            .botmenu-bar > li.active > a {
                background-color: #cc3600;
                color: #ffffff;
            }
            .tab-arrow {
                font-size: 11px;
                margin-left: 3px;
            }

            /* === HOVER DESCRIPTION TOOLTIP BOX === */
            .tab-tooltip {
                display: none;
                position: absolute;
                bottom: calc(100% + 6px);
                left: 50%;
                transform: translateX(-50%);
                width: max-content;
                max-width: 220px;
                padding: 6px 10px;
                background-color: #1e293b;
                color: #ffffff;
                font-size: 13px;
                font-weight: normal;
                line-height: 1.4;
                border-radius: 5px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.25);
                z-index: 1001;
                pointer-events: none;
                text-align: center;
                white-space: normal;
            }
            .tab-tooltip::after {
                content: "";
                position: absolute;
                top: 100%;
                left: 50%;
                transform: translateX(-50%);
                border-width: 5px;
                border-style: solid;
                border-color: #1e293b transparent transparent transparent;
            }
            .botmenu-bar > li:hover > .tab-tooltip {
                display: block;
            }

            /* === DROPDOWN MENU FOR SUB-ITEMS === */
            .tab-dropdown {
                display: none;
                position: absolute;
                top: 100%;
                left: 0;
                min-width: 190px;
                background-color: #ffffff;
                border: 1px solid #cbd5e1;
                border-radius: 0 0 4px 4px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
                list-style: none;
                padding: 4px 0;
                margin: 0;
                z-index: 1000;
                text-align: left;
            }
            .botmenu-bar > li.has-dropdown:hover .tab-dropdown,
            .botmenu-bar > li.has-dropdown.open .tab-dropdown {
                display: block;
            }
            .tab-dropdown li a {
                display: block;
                padding: 9px 16px;
                color: #333333;
                text-decoration: none;
                font-size: 13.5px;
                border-bottom: 1px solid #f1f5f9;
            }
            .tab-dropdown li:last-child a {
                border-bottom: none;
            }
            .tab-dropdown li a:hover,
            .tab-dropdown li a.active-sub {
                background-color: #f0f7fb;
                color: #0069A3;
                font-weight: bold;
            }
        </style>

        <div class="tab-nav-wrapper">
            ${siteTitle ? `<div class="site-title-bar"><a href="index.html">${siteTitle}</a></div>` : ''}
            
            <div class="container-search">
                <input type="text" id="search-box" placeholder="输入关键词..." />
                <button id="search-button">搜索</button>
                <div id="search-results"></div>
            </div>

            <ul class="botmenu-bar" id="menuTabs">
                ${tabsHtml}
            </ul>
        </div>
    `;
}

// Allows tapping a category tab on mobile/touchscreens to open its dropdown
function toggleTabDropdown(event, linkEl) {
    event.stopPropagation();
    const parentLi = linkEl.parentElement;
    const isAlreadyOpen = parentLi.classList.contains("open");
    
    document.querySelectorAll(".botmenu-bar > li.has-dropdown").forEach(li => {
        li.classList.remove("open");
    });

    if (!isAlreadyOpen) {
        parentLi.classList.add("open");
    }
}

// Close dropdown if clicking anywhere outside on the page
document.addEventListener("click", () => {
    document.querySelectorAll(".botmenu-bar > li.has-dropdown").forEach(li => {
        li.classList.remove("open");
    });
});

// Run immediately
renderHeader();
