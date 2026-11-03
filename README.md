# 🚀 Apprise-MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io/)

> **The Universal Multi-Channel Notification Infrastructure for AI Agents.**  
> Powered by [caronc/apprise](https://github.com/caronc/apprise) and [FastMCP](https://github.com/jlowin/fastmcp).

Empower your AI Agents (**Claude Desktop, Cowork, Cursor, DeepSeek, VS Code, AutoGPT**) to push real-time alerts, trading execution logs, reports, and incident alerts to **80+ platforms** (Telegram, Discord, Slack, Email, WeCom, DingTalk, Pushover, SMS) via a single unified Model Context Protocol (MCP) tool call.

---

## ⚡ Quick Start

### Run with `uvx` (Zero Installation)
```bash
uvx apprise-mcp
```

### Or Install via Pip
```bash
pip install apprise fastmcp pydantic
python server.py
```

---

## 🔌 One-Click Integration into AI Clients

### 1. Claude Desktop / Cowork
Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "apprise-mcp": {
      "command": "python",
      "args": [
        "path/to/apprise-mcp/server.py"
      ]
    }
  }
}
```

### 2. Cursor IDE
Go to **Cursor Settings** -> **Features** -> **MCP** -> **+ Add New MCP Server**:
- **Name**: `apprise-mcp`
- **Type**: `command`
- **Command**: `python path/to/apprise-mcp/server.py`

---

## 🛠️ Supported Channels (90+ Services, 161 Formats)

| Platform | URL Format Example |
| :--- | :--- |
| **Telegram** | `tgram://BOT_TOKEN/CHAT_ID` |
| **Discord** | `discord://WEBHOOK_ID/WEBHOOK_TOKEN` |
| **Slack** | `slack://TokenA/TokenB/TokenC` |
| **Email (SMTP)** | `mailto://user:pass@smtp.gmail.com?to=target@domain.com` |
| **Pushover** | `pover://USER_KEY@TOKEN` |
| **DingTalk (钉钉)** | `dingtalk://access_token` |
| **WeCom (企业微信)** | `wxwork://corp_id/corp_secret/agent_id` |

---

## 📄 License
MIT License. Inspired by [caronc/apprise](https://github.com/caronc/apprise).
