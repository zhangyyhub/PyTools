# -*- coding : utf-8 -*-
# Time       : 2023/6/13 16:42
# Auth       : Yangyang Zhang(张洋洋)
# File       : send_message_to_dingtalk.py
# Explain    : pip install DingtalkChatbot

from dingtalkchatbot.chatbot import DingtalkChatbot

webhook = 'https://oapi.dingtalk.com/robot/send?access_token=91ae5a4ff7d52ea8373436f38b0fe86ed332bc10a1d70a96fbb0644268078403'


def sendtext(webhook:str, msg:str):
    # 初始化机器人小丁
    xiaoding = DingtalkChatbot(webhook)
    # 发送消息到钉钉
    xiaoding.send_text(msg=msg, is_at_all=False)


if __name__ == '__main__':
    sendtext(webhook, '测试')
