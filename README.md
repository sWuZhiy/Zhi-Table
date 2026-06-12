# 🧠 AI 智能科研排程舱 — WeekUp 风格增强版 v8.0

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Deploy with Vercel](https://img.shields.io/badge/Deploy-Vercel-black?logo=vercel)](https://vercel.com/import)
[![Live Demo](https://img.shields.io/badge/Live-Demo-blue?logo=vercel)](https://your-domain.com/ai-planner)

一个纯前端实现的**智能课表管理 + AI 排程助手**，专为高校学生和科研人员设计。  
🎯 整合教务课表导入、日历拖拽操作、自然语言排程、多格式导出，并利用**大语言模型思维链（CoT）** 自动安排科研任务，彻底告别时间冲突。

![界面总览](https://your-image-host.com/screenshot-main.png)  
*（主界面：右侧周历 + 左侧 AI 排程）*


## ✨ 核心亮点

| 功能 | 描述 |
|------|------|
| 📥 **教务课表导入** | 支持 `.xlsx`、`.ics`、`.csv` 文件，自动识别课程名、星期、节次/时间，内置高校节次映射表。|
| 🧠 **AI 智能排程** | 用自然语言描述任务，AI 分析已有课表空闲时段，输出推演过程并生成不冲突的日程。|
| 📅 **拖拽式日历** | 基于 FullCalendar 的周视图，支持框选新建、拖拽移动/伸缩、点击编辑，操作直观。|
| 📤 **多格式导出** | 导出 JSON 完整备份，或导出标准 ICS 文件同步到 Google 日历、Outlook。|
| 💾 **本地存储** | 所有数据（课表、API 密钥）保存在浏览器 LocalStorage，无需后端数据库。|
| 🎨 **精致 UI** | WeekUp 风格现代化设计，动画过渡、彩带庆祝效果、响应式布局。|

## 🚀 快速开始

### 在线使用
👉 **[立即体验](https://your-domain.com/ai-planner)**（请替换为你的部署地址）

### 本地运行
无需构建工具，打开即用：
```bash
# 克隆仓库
git clone https://github.com/your-username/ai-schedule-planner.git
cd ai-schedule-planner

# 使用本地服务器打开（推荐）
python3 -m http.server 8000
# 或使用 Node.js http-server
npx http-server
```
浏览器访问 `http://localhost:8000` 即可。

> **推荐使用本地服务器**，否则可能因 CORS 限制影响部分 API 测试（真实调用不受影响）。

## 📖 使用详解

### 1. ⚙️ 配置 AI 模型
点击右上角 **配置网关**，填写兼容 OpenAI 格式的 API 信息：
- **Base URL**：如 `https://api.deepseek.com/chat/completions`
- **Model ID**：如 `deepseek-chat`、`gpt-3.5-turbo`
- **API Key**：你的密钥

信息仅保存在你的浏览器中，绝对安全。

### 2. 📥 导入课表
支持从教务系统或日历软件导出的文件：
- **Excel**（`.xlsx`/`.xls`）
- **iCalendar**（`.ics`）
- **CSV**（逗号分隔）

操作路径：**导入/导出 → 导入课表文件**  
系统会自动解析表头，预览数据后您可选择 **合并** 或 **替换** 现有课表。

#### 自动节次转换
内置了多数高校的节次时间表，如：
| 节次写法 | 自动转换为 |
|----------|------------|
| `1-2节` | 08:00 - 09:35 |
| `3,4节` | 09:50 - 11:25 |
| `第5节` | 11:30 - 12:15 |

如果文件中是直接的时间格式（如 `08:00-09:35`），也会被正确识别。

### 3. ✍️ 手动管理课程
- **框选建课**：在日历上拖拽空白区域即可快速创建课程。
- **拖拽调整**：直接拖动或伸缩课程块，时间自动同步。
- **点击编辑**：点击日历或左侧清单中的课程，弹出编辑窗，可修改名称、地点、颜色等。

### 4. 🤖 AI 排程
在左侧 **CoT 强约束智能排程** 文本框中，用自然语言描述需求，例如：
- “安排 3 小时深度学习代码调试，下午课后，避开周三组会”
- “每天 1 小时论文阅读，放在早上 8-9 点”
- “安排 2 次 1.5 小时实验，周二和周四晚上”

点击按钮后，AI 会：
1. 扫描当前周课表的所有空闲时段
2. 匹配时长、偏好、睡眠禁区等约束
3. 输出推理过程及排程结果

所有 AI 创建的课程都会带有 ✨ 标记，方便区分。

### 5. 📤 导出备份
通过右上角菜单可导出：
- **JSON**：包含所有课程数据，可用于完整备份和迁移。
- **ICS**：标准日历文件，可导入 Google Calendar、Outlook、Apple 日历等。

## ⌨️ 快捷键

| 操作 | 快捷键 |
|------|--------|
| 新建课程 | `Ctrl + N` |
| 跳回本周 | `Ctrl + T` |
| 关闭弹窗/面板 | `Esc` |

## 📁 项目结构

```
.
├── index.html          # 单文件应用（所有HTML/CSS/JS）
├── sample_schedule.csv # 示例课表（用于测试导入）
└── README.md
```

所有依赖均通过 CDN 加载，无需安装额外包。

## 🛠️ 技术栈

| 类别 | 技术 |
|------|------|
| 前端框架 | 原生 JavaScript + [Tailwind CSS](https://tailwindcss.com/) |
| 日历组件 | [FullCalendar v6](https://fullcalendar.io/) |
| 图标库 | [Lucide Icons](https://lucide.dev/) |
| HTTP 请求 | [Axios](https://axios-http.com/) |
| Excel 解析 | [SheetJS (xlsx)](https://github.com/SheetJS/sheetjs) |
| 动画特效 | [canvas-confetti](https://github.com/catdad/canvas-confetti) |
| AI 接口 | 任意 OpenAI Chat Completions 兼容 API |

## 🌐 部署

本项目为纯静态页面，可部署至任何静态托管平台：

### GitHub Pages
```bash
git checkout -b gh-pages
git push origin gh-pages
# 在仓库 Settings > Pages 中选择 gh-pages 分支
```

### Vercel / Netlify
直接导入 Git 仓库，或拖拽 `index.html` 文件夹上传，无需额外配置。

### 自托管
将文件放置于 Nginx、Apache 的 Web 根目录下即可。

## 🧪 测试课表

仓库中提供了 `sample_schedule.csv` 用于测试导入功能，内容如下：
```csv
课程名称,星期,上课时间,地点
高等数学,周一,08:00-09:35,教1-201
大学英语,周二,10:00-11:35,外语楼304
数据结构,周三,14:00-15:35,计算机楼101
马克思主义原理,周四,08:00-09:35,教2-105
体育,周五,16:00-17:30,体育馆
线性代数,周一,10:00-11:35,教1-301
模拟电子技术,周二,14:00-15:35,电子楼202
信号与系统,周三,08:00-09:35,教3-102
软件工程,周四,14:00-15:35,软件楼501
数字电路,周五,10:00-11:35,电子楼101
```

## 📝 自定义配置

### 修改学期起始日期
编辑 `index.html` 中的 `SEMESTER_START` 变量：
```javascript
const SEMESTER_START = new Date(2026, 1, 23); // 2026年2月23日（周一）
```

### 调整节次时间映射
在 `PERIOD_TIME_MAP` 数组中按需修改：
```javascript
const PERIOD_TIME_MAP = [
  { period: 1, start: '08:00', end: '08:45' },
  { period: 2, start: '08:50', end: '09:35' },
  // ...
];
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！  
发现问题或有新功能建议，请在 [Issues](https://github.com/your-username/ai-schedule-planner/issues) 中提出。

## 📄 许可

[MIT License](LICENSE) © 2025 Your Name

---

⭐ 如果这个项目对你有帮助，请点亮 Star 支持我们！
```

---

