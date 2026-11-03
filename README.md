<div align="center">

# 🚀 Apprise-MCP
### Give Your AI Agent Hands to Ping Your Phone, Discord & Slack

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-brightgreen.svg)](https://modelcontextprotocol.io/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Powered by Apprise](https://img.shields.io/badge/Powered%20by-Apprise%20(80%2B%20Services)-orange.svg)](https://github.com/caronc/apprise)

**Never stare at your terminal waiting for Claude or Cursor again.**  
Let your AI text your phone the second it finishes a long task, encounters an error, or spots a market opportunity.

[Features](#-why-do-you-need-this) • [Quick Start](#-quick-start-30-seconds) • [Client Setup](#-connect-to-your-ai-client) • [Supported Channels](#-popular-supported-channels) • [License](#-license)

---

### 📱 Live Demo (Claude Desktop &amp; Cursor Push Alert)

<div align="center">
  <img src="assets/demo_banner.svg" alt="Apprise-MCP Live Demo" width="840" style="border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.3);" />
</div>

> **What you prompt your AI:**  
> *"Analyze this 50-page financial report, summarize the top 3 risks, and ping my Telegram when you're done."*  
>  
> **What happens:**  
> You close your laptop, grab a coffee, and **your phone buzzes instantly** with the full summary!

---

</div>

## 💡 Why Do You Need This?

| Without Apprise-MCP 😴 | With Apprise-MCP ⚡ |
| :--- | :--- |
| **Babysitting the screen:** You sit watching Claude/Cursor generate code for 10 minutes. | **Walk away freely:** Prompt your agent, close the tab, and get a ping on your phone when it's done. |
| **Missed critical alerts:** Your trading bot or scraper crashes at 3:00 AM, and you only find out the next morning. | **Instant multi-channel sirens:** AI immediately sends emergency alerts to your Telegram, Discord, and SMS. |
| **Building 50 different APIs:** Spending days registering developer accounts for Telegram, Discord, Slack, Twilio. | **One unified standard:** Powered by `caronc/apprise`, supporting **80+ platforms with zero extra code**. |

---

## ⚡ Quick Start (30 Seconds)

### 1. Install Dependencies
```bash
pip install apprise fastmcp pydantic
```

### 2. Verify Your First Alert
Run a quick test using your Telegram, Discord, or Slack webhook:
```bash
python -c "import apprise; ap = apprise.Apprise(); ap.add('tgram://YOUR_BOT_TOKEN/YOUR_CHAT_ID'); ap.notify(title='🎉 Hello!', body='Apprise-MCP is live!')"
```

---

## 🔌 Connect to Your AI Client

### 1. Claude Desktop / Cowork
Open your `claude_desktop_config.json`:
* **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

Add this block under `mcpServers`:

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
1. Open **Cursor Settings** (`Ctrl + Shift + J` or `Cmd + Shift + J`) -> **Features** -> **MCP**.
2. Click **+ Add New MCP Server**:
   * **Name**: `apprise-mcp`
   * **Type**: `command`
   * **Command**: `python path/to/apprise-mcp/server.py`
3. Hit Save. When the status turns green, Cursor's Composer can ping your phone anytime!

### 3. VS Code (Cline / Roo Code / Continue)
Add the same JSON snippet to your `cline_mcp_settings.json`.

---

## 🛠️ Popular Supported Channels

`apprise-mcp` inherits the full power of [caronc/apprise](https://github.com/caronc/apprise), supporting over **80+ notification services and 160+ URL schemas**. 

Pass any combination of URLs, and your agent will broadcast to all of them simultaneously:

| Service | Target URL Format | Example Use Case |
| :--- | :--- | :--- |
| **Telegram** | `tgram://BOT_TOKEN/CHAT_ID` | Personal phone alerts, trading execution bots |
| **Discord** | `discord://WEBHOOK_ID/WEBHOOK_TOKEN` | Developer community channels, build alerts |
| **Slack** | `slack://TokenA/TokenB/TokenC` | Corporate team notifications, incident response |
| **Email (SMTP)** | `mailto://user:pass@smtp.gmail.com?to=boss@work.com` | Official client deliverables, executive briefings |
| **Pushover** | `pover://USER_KEY@TOKEN` | High-priority mobile push notifications |
| **DingTalk (钉钉)** | `dingtalk://ACCESS_TOKEN` | Enterprise automation in Asia |
| **WeCom (企业微信)** | `wxwork://CORP_ID/CORP_SECRET/AGENT_ID` | Chinese enterprise workflows |
| **Twilio (SMS)** | `twilio://ACCOUNT_SID:AUTH_TOKEN@FROM_PHONE/TO_PHONE` | Critical server down / phone SMS waking you up |

---

## 🧠 How the AI Uses It

Once connected, your AI Agent gains access to the `send_notification` tool.

```
┌──────────────────────────────────────────────┐
│                  AI Agent                    │
│   (Claude, Cursor, DeepSeek, VS Code, Auto)  │
└──────────────────────┬───────────────────────┘
                       │ Calls: send_notification(payload)
                       ▼
        ┌──────────────────────────────┐
        │       Apprise-MCP Server     │
        │    (FastMCP + Apprise Engine)│
        └──────────────┬───────────────┘
                       │ Dispatches simultaneously to:
       ┌───────────────┼───────────────┬───────────────┐
       ▼               ▼               ▼               ▼
  [ Telegram ]    [ Discord ]      [ Slack ]       [ Email ]
   (Your Phone)  (Dev Channel)   (Team Channel)  (Client Inbox)
```

**Example Multi-Channel Agent Call:**
```json
{
  "service_urls": [
    "tgram://BOT_TOKEN/CHAT_ID",
    "discord://WEBHOOK_ID/WEBHOOK_TOKEN"
  ],
  "title": "🚨 Deploy Successful!",
  "body": "Version v1.2.0 has been deployed to production. All 42 tests passed."
}
```

---

## 🤝 Acknowledgements & Ecosystem

* Built on top of the battle-tested [caronc/apprise](https://github.com/caronc/apprise) library created by Chris Caron.
* Protocol powered by [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) and [FastMCP](https://github.com/jlowin/fastmcp).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
