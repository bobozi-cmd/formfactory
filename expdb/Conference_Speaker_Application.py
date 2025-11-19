
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写并提交会议发言人申请表单",
        "experience": "",
        "parameters": {
            "full_name": "申请人全名, 变量类型: str",
            "email": "申请人的电子邮件地址, 变量类型: str",
            "phone": "申请人的电话号码, 格式为 111-222-3333, 变量类型: str",
            "organization": "申请人所在机构或组织, 变量类型: str",
            "presentation_title": "演讲标题, 变量类型: str",
            "topic_area": "演讲主题领域, {'Visual Arts', 'Performing Arts', 'Literature', 'Digital Media', 'Art History', 'Creative Writing'}, 变量类型: str",
            "abstract": "演讲概要, 文字长度在250-500之间, 变量类型: str",
            "learning_objectives": "学习目标, 以 1. 2. 3. 标记每个项目, 变量类型: str",
            "bio": "专业简介, 字数不超过200字, 变量类型: str",
            "speaking_experience": "以往演讲经验, 使用 1. 2. 3. 标记; 在过去三年中相关的演讲经历, 变量类型: str",
            "presentation_format": "演讲形式, {'Lecture', 'Workshop', 'Panel Discussion'}, 变量类型: str",
            "tech_requirements": "特殊技术需求, 用','分隔, 变量类型: str",
            "agree_terms": "同意发言人指南和参与条款, 必须为 'Yes', 变量类型: str"
        }
    }
    """
    try:
        await page.get_by_role('textbox', name='Full Name *').fill(kwargs.get('full_name', 'ZHOU1'))
        await page.get_by_role('textbox', name='Email Address *').fill(kwargs.get('email', '21012@qq.com'))
        phone = kwargs.get('phone', '111-222-3333')
        if not re.match('\\d{3}-\\d{3}-\\d{4}', phone):
            raise ValueError('Phone number must be in the format 111-222-3333')
        await page.get_by_role('textbox', name='Phone Number *').fill(phone)
        await page.get_by_role('textbox', name='Organization/Institution').fill(kwargs.get('organization', 'AIOPEN'))
        await page.get_by_role('textbox', name='Presentation Title *').fill(kwargs.get('presentation_title', 'HI'))
        topic_area = kwargs.get('topic_area', 'Literature')
        if topic_area not in ['Visual Arts', 'Performing Arts', 'Literature', 'Digital Media', 'Art History', 'Creative Writing']:
            raise ValueError('Invalid topic area')
        await page.get_by_label('Topic Area *').select_option(topic_area)
        await page.get_by_role('textbox', name='Presentation Abstract *').fill(kwargs.get('abstract', 'Hello'))
        await page.get_by_role('textbox', name='Learning Objectives *').fill(kwargs.get('learning_objectives', '1. A 2. B 3.C'))
        await page.get_by_role('textbox', name='Professional Biography *').fill(kwargs.get('bio', 'hello'))
        await page.get_by_role('textbox', name='Previous Speaking Experience').fill(kwargs.get('speaking_experience', '1. A 2. B 3. C'))
        presentation_format = kwargs.get('presentation_format', 'Lecture')
        if presentation_format not in ['Lecture', 'Workshop', 'Panel Discussion']:
            raise ValueError('Invalid presentation format')
        await page.get_by_text(presentation_format, exact=True).click()
        await page.get_by_role('textbox', name='Special Technical Requirements').fill(kwargs.get('tech_requirements', 'PPP, INT, AOO'))
        if kwargs.get('agree_terms', 'No') != 'Yes':
            raise ValueError('You must agree to the terms')
        await page.get_by_text('I agree to the speaker guidelines and terms of participation *').click()
        await page.get_by_role('button', name='Submit Application').click()
    except Exception as e:
        print(f'An error occurred: {str(e)}')
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/arts-creative/speaker-application"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
