# 🌐 Complete List of Supported Channels (161 Schemas)

`apprise-mcp` natively inherits all **161 URL schemas** and **90+ notification services** from [caronc/apprise](https://github.com/caronc/apprise).

Any combination of these URLs can be passed into the `service_urls` array parameter of `send_notification`, and your AI Agent will broadcast to all of them in parallel.

---

## 💬 1. Instant Messaging & Team Chat

| Service | Primary Schema | Website / Docs |
| :--- | :--- | :--- |
| **Telegram** | `tgram://` | [telegram.org](https://telegram.org) |
| **Discord** | `discord://` | [discord.com](https://discord.com) |
| **Slack** | `slack://` | [slack.com](https://slack.com) |
| **WhatsApp** | `whatsapp://` | [whatsapp.com](https://whatsapp.com) |
| **Microsoft Teams (Workflows)** | `workflow://` | [microsoft.com](https://www.microsoft.com/microsoft-teams) |
| **Google Chat** | `gchat://` | [chat.google.com](https://chat.google.com) |
| **Cisco Webex Teams** | `wxteams://` | [webex.com](https://webex.teams.com) |
| **Mattermost** | `mmost://` | [mattermost.com](https://mattermost.com) |
| **Matrix** | `matrix://` | [matrix.org](https://matrix.org) |
| **Rocket.Chat** | `rocket://` | [rocket.chat](https://rocket.chat) |
| **Zulip** | `zulip://` | [zulip.com](https://zulip.com) |
| **Signal API** | `signal://` | [signal.org](https://signal.org) |
| **Line** | `line://` | [line.me](https://line.me) |
| **Viber** | `viber://` | [viber.com](https://viber.com) |
| **Kook** | `kook://` | [kookapp.cn](https://kookapp.cn) |
| **Revolt** | `revolt://` | [revolt.chat](https://revolt.chat) |
| **Session** | `session://` | [getsession.org](https://getsession.org) |
| **Threema Gateway** | `threema://` | [gateway.threema.ch](https://gateway.threema.ch) |
| **IRC** | `irc://` | [ircv3.net](https://ircv3.net) |
| **Delta Chat** | `deltachat://` | [delta.chat](https://delta.chat) |
| **Flock** | `flock://` | [flock.com](https://flock.com) |
| **GroupMe** | `groupme://` | [groupme.com](https://groupme.com) |
| **Guilded** | `guilded://` | [guilded.gg](https://guilded.gg) |
| **Zoho Cliq** | `cliq://` | [zoho.com/cliq](https://zoho.com/cliq) |
| **Zoom** | `zoom://` | [zoom.us](https://zoom.us) |

---

## 🇨🇳 2. Asian Enterprise & Indie Push Ecosystem

| Service | Primary Schema | Notes |
| :--- | :--- | :--- |
| **DingTalk (钉钉)** | `dingtalk://` | Robot webhook token |
| **WeCom (企业微信)** | `wxwork://` | Corp ID + Secret + Agent ID |
| **WeCom Bot (企微机器人)** | `wecombot://` | Group robot webhook key |
| **Feishu (飞书)** | `feishu://` | Custom bot webhook |
| **Lark (海外版飞书)** | `lark://` | Custom bot webhook |
| **Bark (iOS)** | `bark://` | Lightweight custom iOS push notification |
| **PushDeer** | `pushdeer://` | Open-source iOS/Android push |
| **ServerChan (Server酱)** | `schan://` | SendKey WeChat push |
| **WxPusher** | `wxpusher://` | WeChat official account push |
| **Pushplus (推送加)** | `pushplus://` | WeChat template notification |
| **OneBot (QQ 机器人)** | `onebot://` | Universal QQ bot protocol |
| **PushMe** | `pushme://` | Multi-client push notification |

---

## 🚨 3. DevOps, Monitoring & Incident Alerts

| Service | Primary Schema | Website / Docs |
| :--- | :--- | :--- |
| **PagerDuty** | `pagerduty://` | [pagerduty.com](https://pagerduty.com) |
| **Opsgenie** | `opsgenie://` | [opsgenie.com](https://opsgenie.com) |
| **Better Stack** | `betterstack://` | [betterstack.com](https://betterstack.com) |
| **Splunk On-Call (VictorOps)** | `splunk://` | [splunk.com](https://splunk.com) |
| **GoAlert** | `goalert://` | [goalert.me](https://goalert.me) |
| **incident.io** | `incidentio://` | [incident.io](https://incident.io) |
| **ilert** | `ilert://` | [ilert.com](https://ilert.com) |
| **SIGNL4** | `signl4://` | [signl4.com](https://signl4.com) |
| **Squadcast** | `squadcast://` | [squadcast.com](https://squadcast.com) |
| **Spike.sh** | `spike://` | [spike.sh](https://spike.sh) |
| **PagerTree** | `pagertree://` | [pagertree.com](https://pagertree.com) |
| **GitHub** | `github://` | [github.com](https://github.com) |
| **Jira** | `jira://` | [atlassian.com](https://atlassian.com) |

---

## 📱 4. Mobile & Desktop Push Services

| Service | Primary Schema | Website / Docs |
| :--- | :--- | :--- |
| **Pushover** | `pover://` | [pushover.net](https://pushover.net) |
| **Pushbullet** | `pbul://` | [pushbullet.com](https://pushbullet.com) |
| **Gotify** | `gotify://` | [gotify.net](https://gotify.net) |
| **ntfy** | `ntfy://` | [ntfy.sh](https://ntfy.sh) |
| **OneSignal** | `onesignal://` | [onesignal.com](https://onesignal.com) |
| **Firebase (FCM)** | `fcm://` | [firebase.google.com](https://firebase.google.com) |
| **Simplepush** | `spush://` | [simplepush.io](https://simplepush.io) |
| **Pushsafer** | `psafer://` | [pushsafer.com](https://pushsafer.com) |
| **Pushy** | `pushy://` | [pushy.me](https://pushy.me) |
| **Join (by joaoapps)** | `join://` | [joaoapps.com/join](https://joaoapps.com/join) |
| **Prowl (iOS)** | `prowl://` | [prowlapp.com](https://prowlapp.com) |
| **Chanify** | `chanify://` | [chanify.net](https://chanify.net) |
| **Windows Notification** | `windows://` | Local Windows Toast Notification |

---

## ✉️ 5. Email Services (SMTP & Cloud APIs)

| Service | Primary Schema | Website / Docs |
| :--- | :--- | :--- |
| **Standard SMTP E-Mail** | `mailto://` | Standard SMTP (Gmail, Outlook, Private) |
| **AWS SES** | `ses://` | [aws.amazon.com/ses](https://aws.amazon.com/ses) |
| **Resend** | `resend://` | [resend.com](https://resend.com) |
| **SendGrid** | `sendgrid://` | [sendgrid.com](https://sendgrid.com) |
| **Mailgun** | `mailgun://` | [mailgun.com](https://mailgun.com) |
| **Postmark** | `postmark://` | [postmarkapp.com](https://postmarkapp.com) |
| **Brevo (Sendinblue)** | `brevo://` | [brevo.com](https://brevo.com) |
| **MailerSend** | `mailersend://` | [mailersend.com](https://mailersend.com) |
| **SparkPost** | `sparkpost://` | [sparkpost.com](https://sparkpost.com) |
| **SMTP2Go** | `smtp2go://` | [smtp2go.com](https://smtp2go.com) |
| **SendPulse** | `sendpulse://` | [sendpulse.com](https://sendpulse.com) |

---

## 📞 6. SMS & Voice Gateways

| Service | Primary Schema | Website / Docs |
| :--- | :--- | :--- |
| **Twilio** | `twilio://` | [twilio.com](https://twilio.com) |
| **Vonage (Nexmo)** | `vonage://` | [vonage.com](https://vonage.com) |
| **MessageBird** | `msgbird://` | [messagebird.com](https://messagebird.com) |
| **Telnyx** | `telnyx://` | [telnyx.com](https://telnyx.com) |
| **AWS SNS** | `sns://` | [aws.amazon.com/sns](https://aws.amazon.com/sns) |
| **ClickSend** | `clicksend://` | [clicksend.com](https://clicksend.com) |
| **Plivo** | `plivo://` | [plivo.com](https://plivo.com) |
| **BulkSMS** | `bulksms://` | [bulksms.com](https://bulksms.com) |
| **Sinch** | `sinch://` | [sinch.com](https://sinch.com) |
| **Clickatell** | `clickatell://` | [clickatell.com](https://clickatell.com) |
| **46elks** | `46elks://` | [46elks.com](https://46elks.com) |
| **SMS Eagle** | `smseagle://` | [smseagle.eu](https://smseagle.eu) |
| **Octopush** | `octopush://` | [octopush.com](https://octopush.com) |
| **Burst SMS** | `burstsms://` | [burstsms.com](https://burstsms.com) |
| **Free Mobile (France)** | `freemobile://` | [mobile.free.fr](https://mobile.free.fr) |
| **Exotel (India)** | `exotel://` | [exotel.com](https://exotel.com) |
| **MSG91 (India)** | `msg91://` | [msg91.com](https://msg91.com) |
| **Africas Talking** | `atalk://` | [africastalking.com](https://africastalking.com) |
| **Kavenegar (Middle East)** | `kavenegar://` | [kavenegar.com](https://kavenegar.com) |

---

## 🏠 7. Smart Home & Media Centers

| Service | Primary Schema | Website / Docs |
| :--- | :--- | :--- |
| **Home Assistant** | `hassio://` | [home-assistant.io](https://home-assistant.io) |
| **Kodi / XBMC** | `kodi://` | [kodi.tv](https://kodi.tv) |
| **Emby** | `emby://` | [emby.media](https://emby.media) |
| **Jellyfin** | `jellyfin://` | [jellyfin.org](https://jellyfin.org) |
| **LaMetric Time** | `lametric://` | [lametric.com](https://lametric.com) |
| **Enigma2** | `enigma2://` | [dreambox.de](https://dreambox.de) |

---

## 🌐 8. Social Networks & Web3

| Service | Primary Schema | Website / Docs |
| :--- | :--- | :--- |
| **Twitter / X** | `x://` | [x.com](https://x.com) |
| **Reddit** | `reddit://` | [reddit.com](https://reddit.com) |
| **Mastodon** | `mastodon://` | [joinmastodon.org](https://joinmastodon.org) |
| **Bluesky** | `bsky://` | [bsky.app](https://bsky.app) |
| **Misskey** | `misskey://` | [misskey-hub.net](https://misskey-hub.net) |

---

## ⚡ 9. Custom Webhooks, Queues & Raw Protocols

| Protocol | Primary Schema | Description |
| :--- | :--- | :--- |
| **Custom JSON Webhook** | `json://` | Post raw JSON to any external API |
| **Custom Form Webhook** | `form://` | Post HTTP form payload (`application/x-www-form-urlencoded`) |
| **Custom XML Webhook** | `xml://` | Post XML payload |
| **AMQP (RabbitMQ)** | `amqp://` | Publish messages to message queues |
| **MQTT** | `mqtt://` | IoT MQTT publish |
| **Remote Syslog** | `rsyslog://` | Stream logs directly to enterprise SIEM |
