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
        description: "文革以外发生在毛年代的事"
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
            { title: "历史游记", url: "history_journal.html" }
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
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
                margin-bottom: 24px;
            }
            .site-title-bar {
                text-align: center;
                padding: 16px 0 10px 0;
            }
            .site-title-bar a {
                text-decoration: none;
                color: #1e3a5f;
                font-size: 1.6rem;
                font-weight: 700;
                font-family: "Noto Serif SC", Georgia, "Songti SC", serif;
                letter-spacing: 0.5px;
            }

            /* === SEARCH AREA === */
            .container-search {
                text-align: right;
                padding: 10px 16px;
                background-color: transparent;
                display: flex;
                justify-content: flex-end;
                align-items: center;
            }
            #search-box {
                width: 240px;
                padding: 7px 14px;
                font-size: 14px;
                background-color: #ffffff;
                border: 1px solid #d1d5db;
                border-radius: 20px;
                color: #334155;
                outline: none;
                transition: all 0.25s ease;
                box-sizing: border-box;
            }
            #search-box:focus {
                border-color: #1e3a5f;
                box-shadow: 0 0 0 3px rgba(30, 58, 95, 0.12);
                background-color: #ffffff;
            }
            #search-button {
                padding: 7px 18px;
                font-size: 14px;
                font-weight: 500;
                color: #ffffff;
                background-color: #1e3a5f;
                border: none;
                border-radius: 20px;
                cursor: pointer;
                margin-left: 6px;
                transition: all 0.2s ease;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            }
            #search-button:hover {
                background-color: #2b4f7e;
                transform: translateY(-1px);
                box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
            }
            #search-results {
                text-align: left;
            }

            /* === THE MENU BAR (Modern Scholar Navy) === */
            .botmenu-bar {
                background: #1e3a5f;
                border-radius: 8px;
                box-shadow: 0 3px 10px rgba(15, 23, 42, 0.08);
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                padding: 0 8px;
                margin: 0;
                list-style: none;
            }
            .botmenu-bar > li {
                margin: 0;
                position: relative;
            }
            .botmenu-bar > li > a {
                display: inline-block;
                padding: 11px 16px;
                color: #f1f5f9;
                text-decoration: none;
                font-size: 15px;
                font-weight: 500;
                letter-spacing: 0.3px;
                border-right: 1px solid rgba(255, 255, 255, 0.1);
                transition: background-color 0.2s, color 0.2s;
            }
            .botmenu-bar > li:first-child > a {
                border-left: 1px solid rgba(255, 255, 255, 0.1);
            }
            /* Hover & Active States */
            .botmenu-bar > li > a:hover {
                background-color: rgba(255, 255, 255, 0.12);
                color: #ffffff;
            }
            .botmenu-bar > li.active > a {
                background-color: #8b1e2f; /* 典雅暗绛红 */
                color: #ffffff;
                font-weight: 600;
            }
            .tab-arrow {
                font-size: 11px;
                margin-left: 4px;
                opacity: 0.8;
            }

            /* === HOVER DESCRIPTION TOOLTIP BOX === */
            .tab-tooltip {
                display: none;
                position: absolute;
                bottom: calc(100% + 8px);
                left: 50%;
                transform: translateX(-50%);
                width: max-content;
                max-width: 240px;
                padding: 8px 12px;
                background-color: #1e293b;
                color: #f8fafc;
                font-size: 12.5px;
                font-weight: normal;
                line-height: 1.5;
                border-radius: 6px;
                box-shadow: 0 6px 16px rgba(0, 0, 0, 0.25);
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
                animation: fadeInTooltip 0.15s ease-in-out;
            }
            @keyframes fadeInTooltip {
                from { opacity: 0; transform: translate(-50%, 4px); }
                to { opacity: 1; transform: translate(-50%, 0); }
            }

            /* === DROPDOWN MENU FOR SUB-ITEMS === */
            .tab-dropdown {
                display: none;
                position: absolute;
                top: calc(100% + 2px);
                left: 0;
                min-width: 180px;
                background-color: #ffffff;
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
                list-style: none;
                padding: 6px 0;
                margin: 0;
                z-index: 1000;
                text-align: left;
            }
            .botmenu-bar > li.has-dropdown:hover .tab-dropdown,
            .botmenu-bar > li.has-dropdown.open .tab-dropdown {
                display: block;
                animation: fadeInDropdown 0.2s ease-out;
            }
            @keyframes fadeInDropdown {
                from { opacity: 0; transform: translateY(-4px); }
                to { opacity: 1; transform: translateY(0); }
            }
            .tab-dropdown li a {
                display: block;
                padding: 10px 18px;
                color: #334155;
                text-decoration: none;
                font-size: 14px;
                transition: background-color 0.15s, color 0.15s;
            }
            .tab-dropdown li a:hover,
            .tab-dropdown li a.active-sub {
                background-color: #f1f5f9;
                color: #1e3a5f;
                font-weight: 600;
            }

            /* === MOBILE HORIZONTAL SCROLL NAV === */
            @media (max-width: 768px) {
                .botmenu-bar {
                    flex-wrap: nowrap;
                    overflow-x: auto;
                    justify-content: flex-start;
                    -webkit-overflow-scrolling: touch;
                    scrollbar-width: none; /* Firefox */
                    padding: 0 4px;
                    border-radius: 6px;
                }
                .botmenu-bar::-webkit-scrollbar {
                    display: none; /* Safari and Chrome */
                }
                .botmenu-bar > li > a {
                    white-space: nowrap;
                    padding: 10px 14px;
                    font-size: 14px;
                }
                .container-search {
                    padding: 8px 10px;
                    justify-content: center;
                }
                #search-box {
                    width: 100%;
                    max-width: 260px;
                }
            }
        </style>

        <div class="tab-nav-wrapper">
            ${siteTitle ? `<div class="site-title-bar"><a href="index.html">${siteTitle}</a></div>` : ''}
            
            <div class="container-search">
                <input type="text" id="search-box" placeholder="输入关键词搜索..." />
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
