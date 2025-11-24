
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填充研究报名表并提交",
        "experience": "",
        "parameters": {
            "full_name": "参与者的全名, 变量类型: str",
            "age": "参与者的年龄, 必须大于等于18岁, 变量类型: int",
            "existing_conditions": "参与者的现有医疗状况, 如果为空会被捕获并忽略错误, 变量类型: str",
            "current_medications": "参与者当前的药物, 如果为空会被捕获并忽略错误, 变量类型: str",
            "preferred_study_type": "参与者偏好的研究类型, 可选值为 {'Clinical Trial', 'Observational Study', 'Survey-based Research'}, 变量类型: str",
            "availability": "参与者的可用时间, 可选值为 {'Weekdays', 'Weekends', 'Both'}, 变量类型: str",
            "email_address": "参与者的电子邮件地址, 变量类型: str",
            "phone_number": "参与者的电话号码, 变量类型: str"
        }
    }
    """
    await page.get_by_role('textbox', name='Full Name').fill(kwargs.get('full_name'))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('spinbutton', name='Age').fill(str(kwargs.get('age')))
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Existing Medical Conditions').fill(kwargs.get('existing_conditions'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Current Medications').fill(kwargs.get('current_medications'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Preferred Study Type').select_option(kwargs.get('preferred_study_type'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Availability').select_option(kwargs.get('availability'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Email Address').fill(kwargs.get('email_address'))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Phone Number').fill(kwargs.get('phone_number'))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('button', name='Submit Enrollment').click()
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/healthcare-medical/research-enrollment"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
