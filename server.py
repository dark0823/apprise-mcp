"""
Apprise Omni-Channel Notification MCP Server
让任何 AI Agent (Claude Desktop, Cursor, Antigravity, OpenClaw 等) 拥有全球 80+ 平台的即时通知推送能力。
"""

import sys
import apprise
from fastmcp import FastMCP
from pydantic import BaseModel, Field

# 初始化 FastMCP 服务器
mcp = FastMCP("Omni-Channel-Notifier")

class NotificationPayload(BaseModel):
    service_urls: list[str] = Field(
        ...,
        description=(
            "推送目标 URL 列表。例如 Telegram: 'tgram://BOT_TOKEN/CHAT_ID', "
            "Discord: 'discord://WEBHOOK_ID/WEBHOOK_TOKEN', "
            "Slack: 'slack://TokenA/TokenB/TokenC'"
        )
    )
    title: str = Field(..., description="通知标题，例如：【交易风控警报】或【任务已完成】")
    body: str = Field(..., description="通知详细正文内容")

@mcp.tool()
def send_notification(payload: NotificationPayload) -> str:
    """
    向人类指定的设备或社群频道发送即时推送通知。
    原生支持 Telegram, Discord, Slack, 企业微信, 钉钉, Email 等 80+ 平台。
    """
    try:
        apobj = apprise.Apprise()

        # 添加所有目标渠道 URL
        for url in payload.service_urls:
            apobj.add(url.strip())

        # 执行推送
        success = apobj.notify(
            title=payload.title,
            body=payload.body,
        )

        if success:
            return f"✅ 成功投递通知！标题: '{payload.title}' 已推送至 {len(payload.service_urls)} 个目标渠道。"
        else:
            return "❌ 推送失败，请检查 service_urls 格式或网络连接状态。"
            
    except Exception as e:
        return f"❌ 运行时异常: {str(e)}"

@mcp.tool()
def get_channel_cheatsheet() -> str:
    """
    查询 Apprise 支持的常用渠道 URL 编写格式规范。
    """
    return """
    === 常用渠道 URL 语法速查表 ===
    1. Telegram:
       tgram://BOT_TOKEN/CHAT_ID
       示例: tgram://1234567890:ABCdefGhIJKlmNoPQRsTUVwxyZ/123456789

    2. Discord:
       discord://WEBHOOK_ID/WEBHOOK_TOKEN

    3. Slack:
       slack://TokenA/TokenB/TokenC

    4. Email (SMTP):
       mailto://user:password@smtp.gmail.com?to=target@example.com

    5. 钉钉 (DingTalk):
       dingtalk://access_token

    6. 企业微信 (WeCom):
       wxwork://corp_id/corp_secret/agent_id
    """

if __name__ == "__main__":
    mcp.run()
