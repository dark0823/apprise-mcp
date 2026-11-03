---
name: Apprise Universal Multi-Channel Notifier (OpenClaw & Agent Skill)
description: Universal multi-channel notification and alert skill for AI Agents (OpenClaw, Claude, Cursor, AutoGPT). Enables autonomous agents to dispatch real-time push notifications, trading execution logs, build statuses, and incident alerts to 80+ platforms (Telegram, Discord, Slack, Email, WeCom, DingTalk, Twilio) via CLI or MCP.
---

# 🚀 Apprise-MCP Universal Notifier Skill

This skill empowers autonomous AI agents (such as **OpenClaw**, **AutoGPT**, **Claude Code**, and **Cursor**) to break through sandbox boundaries and interact with the physical world by sending instant push notifications to human devices and community channels.

---

## 📌 When to Activate This Skill

The agent should automatically invoke this skill whenever:
1. **Long-running Task Completion**: When a coding, scraping, or data analysis task finishes and the user requested an alert.
2. **Trading & Financial Alerts**: When an automated strategy detects an SMC liquidity sweep, triggers an order execution, or breaches a drawdown limit.
3. **Incident & Error Escalation**: When a production server crashes, a rate limit is hit, or an unhandled exception occurs.
4. **Scheduled Daily Reports**: When dispatching daily morning briefs, market overviews, or to-do lists.

---

## 🛠️ Execution Methods for Agents

Agents can invoke this skill via **CLI (Command Line)** or **Native MCP Protocol**.

### Method A: CLI Execution (Recommended for OpenClaw / Terminal Agents)

Run the Python CLI with structured `--json` output:

```bash
python cli.py notify -u "TARGET_URL" -t "ALERT_TITLE" -b "MESSAGE_BODY" --json
```

#### Multi-Channel Broadcast:
To send simultaneously to multiple channels in a single command, specify `-u` multiple times:

```bash
python cli.py notify \
  -u "tgram://BOT_TOKEN/CHAT_ID" \
  -u "discord://WEBHOOK_ID/WEBHOOK_TOKEN" \
  -t "🚨 Critical Production Alert" \
  -b "Database connection pool saturated (98%). Failover initiated." \
  --json
```

#### JSON Response Schema:
```json
{
  "success": true,
  "title": "🚨 Critical Production Alert",
  "channels_count": 2,
  "urls": [
    "tgram://BOT_TOKEN/CHAT_ID",
    "discord://WEBHOOK_ID/WEBHOOK_TOKEN"
  ]
}
```

---

### Method B: Native MCP Tool Call

When operating inside an MCP-enabled environment (Claude Desktop, Cursor, Antigravity):

```json
{
  "name": "send_notification",
  "arguments": {
    "payload": {
      "service_urls": [
        "tgram://BOT_TOKEN/CHAT_ID",
        "discord://WEBHOOK_ID/WEBHOOK_TOKEN"
      ],
      "title": "🎉 Build Succeeded",
      "body": "All 42 tests passed. Deployment live on production."
    }
  }
}
```

---

## 📖 Quick Channel URL Cheat Sheet

| Platform | URL Format Example |
| :--- | :--- |
| **Telegram** | `tgram://BOT_TOKEN/CHAT_ID` |
| **Discord** | `discord://WEBHOOK_ID/WEBHOOK_TOKEN` |
| **Slack** | `slack://TokenA/TokenB/TokenC` |
| **Email (SMTP)** | `mailto://user:pass@smtp.gmail.com?to=target@domain.com` |
| **Pushover** | `pover://USER_KEY@TOKEN` |
| **DingTalk (钉钉)** | `dingtalk://ACCESS_TOKEN` |
| **WeCom (企业微信)** | `wxwork://CORP_ID/CORP_SECRET/AGENT_ID` |
| **Twilio SMS** | `twilio://ACCOUNT_SID:AUTH_TOKEN@FROM_PHONE/TO_PHONE` |

*For all 161+ supported protocol schemas, consult `docs/SUPPORTED_CHANNELS.md`.*
