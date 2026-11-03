#!/usr/bin/env python3
"""
Apprise-MCP Command Line Interface (CLI)
让开发者、自动化脚本、以及 AI Agent 能够通过命令行直接调用 80+ 平台推送通知。
"""

import sys
import io
import argparse
import json
import apprise

# 确保在 Windows 控制台环境下输出 UTF-8 编码，防止 GBK 字符集报错
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def send_notification(urls, title, body, as_json=False):
    """执行底层推送"""
    if not urls:
        msg = "Error: At least one --url (-u) must be provided."
        if as_json:
            print(json.dumps({"success": False, "error": msg}))
        else:
            print(f"[ERROR] {msg}", file=sys.stderr)
        return 1

    ap = apprise.Apprise()
    for u in urls:
        ap.add(u.strip())

    try:
        success = ap.notify(title=title, body=body)
        if success:
            if as_json:
                print(json.dumps({
                    "success": True,
                    "title": title,
                    "channels_count": len(urls),
                    "urls": urls
                }))
            else:
                print(f"[SUCCESS] Notification sent successfully to {len(urls)} channel(s)!")
            return 0
        else:
            if as_json:
                print(json.dumps({"success": False, "error": "Dispatch failed. Check URLs or network."}))
            else:
                print("[FAILED] Notification dispatch failed. Verify channel credentials and connectivity.", file=sys.stderr)
            return 1
    except Exception as e:
        if as_json:
            print(json.dumps({"success": False, "error": str(e)}))
        else:
            print(f"[EXCEPTION] {str(e)}", file=sys.stderr)
        return 1

def main():
    parser = argparse.ArgumentParser(
        prog="apprise-cli",
        description="Apprise-MCP Universal Alert CLI for Humans and AI Agents."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # 子命令 1: notify (发送通知)
    notify_parser = subparsers.add_parser("notify", help="Send a notification to one or more channels")
    notify_parser.add_argument(
        "-u", "--url",
        action="append",
        required=True,
        help="Target channel URL (can be specified multiple times for broadcast, e.g. -u tgram://... -u discord://...)"
    )
    notify_parser.add_argument(
        "-t", "--title",
        default="AI Agent Alert",
        help="Notification title (default: 'AI Agent Alert')"
    )
    notify_parser.add_argument(
        "-b", "--body",
        required=True,
        help="Notification body / message text"
    )
    notify_parser.add_argument(
        "--json",
        action="store_true",
        help="Output result as structured JSON (optimized for AI agents)"
    )

    # 子命令 2: test (快速测试单个渠道)
    test_parser = subparsers.add_parser("test", help="Send a quick test ping to verify a channel URL")
    test_parser.add_argument("-u", "--url", required=True, help="Target channel URL to test")

    # 子命令 3: channels (列出常用渠道速查)
    subparsers.add_parser("channels", help="Show quick cheat sheet of popular channel URL formats")

    args = parser.parse_args()

    if args.command == "notify":
        sys.exit(send_notification(args.url, args.title, args.body, as_json=args.json))

    elif args.command == "test":
        print(f"Testing channel: {args.url[:30]}...")
        sys.exit(send_notification(
            [args.url],
            title="Apprise-MCP Test Ping",
            body="If you see this, your notification channel is working perfectly!"
        ))

    elif args.command == "channels":
        print("""
Popular Apprise URL Schemas:
  Telegram:    tgram://BOT_TOKEN/CHAT_ID
  Discord:     discord://WEBHOOK_ID/WEBHOOK_TOKEN
  Slack:       slack://TokenA/TokenB/TokenC
  Email:       mailto://user:pass@smtp.domain.com?to=target@domain.com
  Pushover:    pover://USER_KEY@TOKEN
  DingTalk:    dingtalk://ACCESS_TOKEN
  WeCom:       wxwork://CORP_ID/CORP_SECRET/AGENT_ID
  Twilio SMS:  twilio://ACCOUNT_SID:AUTH_TOKEN@FROM/TO

For the complete list of 161+ schemas, visit:
https://github.com/dark0823/apprise-mcp/blob/main/docs/SUPPORTED_CHANNELS.md
        """)
        sys.exit(0)

    else:
        parser.print_help()
        sys.exit(0)

if __name__ == "__main__":
    main()
