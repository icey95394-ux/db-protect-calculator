# 等保合规计算器 - GitHub Pages 部署指南

## 🚀 小主只需 3 步！

### 第 1 步：创建 GitHub 仓库

1. 登录 GitHub（如果没有账号，先注册一个）
2. 点击右上角 **"+"** → **"New repository"**
3. 填写：
   - **Repository name**: `db-protect-calculator`
   - **Description**: `阿里云等保合规计算器 - 小笨出品`
   - ✅ 选择 **"Public"**（公开仓库才能用 Pages）
   - ❌ 不要勾选 "Initialize this repository with a README"
4. 点击 **"Create repository"**

### 第 2 步：上传代码

在刚创建的仓库页面，找到 **"uploading an existing file"** 链接，然后：

1. 把以下文件拖拽上传：
   - `index.html`（计算器主文件）
   - `README.md`（说明文档）
2. 在下方填写提交信息：`Initial commit - 等保计算器上线`
3. 点击 **"Commit changes"**

**或者用命令行（如果小主熟悉 git）：**
```bash
cd /app/323645/working/db-protect-calculator
git init
git add .
git commit -m "Initial commit - 等保计算器上线"
git branch -M main
git remote add origin https://github.com/你的用户名/db-protect-calculator.git
git push -u origin main
```

### 第 3 步：开启 GitHub Pages

1. 在仓库页面，点击 **"Settings"**（设置）
2. 左侧菜单找到 **"Pages"**
3. 在 **"Build and deployment"** 部分：
   - **Source**: 选择 "Deploy from a branch"
   - **Branch**: 选择 `main`，文件夹选 `/ (root)`
4. 点击 **"Save"**

等待 1-2 分钟，页面会自动部署！

## 🎉 访问地址

部署完成后，访问：
```
https://你的用户名.github.io/db-protect-calculator/
```

例如：`https://xiaobai.github.io/db-protect-calculator/`

## 📱 分享方式

- 直接复制链接发给客户
- 放到个人/团队博客
- 嵌入到 PPT 方案中
- 添加到浏览器书签

## ⚡ 后续更新

如果小主需要更新计算器（比如调整价格）：
1. 修改本地 `index.html`
2. 重新上传到仓库覆盖原文件
3. GitHub Pages 会自动重新部署（约 1 分钟生效）

---

**需要小笨帮忙执行 git 命令吗？** 告诉我小主的 GitHub 用户名，小笨可以帮小主配置好 git 并生成完整的推送命令！🐾