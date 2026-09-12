# DSC5003 Group Project

## 技术栈
- 后端：FastAPI（Python 3.12）
- 数据库：（待定）

## 如何运行

1. 克隆仓库：
   ```bash
   git clone <repo-url>
   cd <repo-name>
   ```

2. 建虚拟环境：
   ```bash
   python -m venv .venv
   ```

3. 激活虚拟环境：
   - Windows PowerShell：
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - Mac / Linux：
     ```bash
     source .venv/bin/activate
     ```

4. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

5. 启动服务：
   ```bash
   uvicorn main:app --reload
   ```

6. 浏览器打开 http://127.0.0.1:8000