
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写咨询预约表单",
        "experience": "",
        "parameters": {
            "full_name": "用户的全名, 变量类型: str",
            "email_address": "用户的电子邮件地址, 变量类型: str",
            "type_of_consultation": "咨询类型, {'': 'Select type', 'Retirement Planning': 'Retirement Planning', 'Investment Planning': 'Investment Planning', 'Tax Planning': 'Tax Planning', 'Estate Planning': 'Estate Planning', 'General Financial Planning': 'General Financial Planning'}, 变量类型: str",
            "preferred_date": "用户偏好的日期, 格式为 YYYY-MM-DD, 变量类型: str",
            "preferred_time": "用户偏好的时间段, {'': 'Select time', 'Morning (9:00 AM-12:00 PM)': 'Morning (9:00 AM - 12:00 PM)', 'Afternoon (1:00 PM-4:00 PM)': 'Afternoon (1:00 PM - 4:00 PM)', 'Evening (4:00 PM -6:00 PM)': 'Evening (4:00 PM - 6:00 PM)'}, 变量类型: str",
            "additional_comments": "附加评论或说明, 变量类型: str"
        }
    }
    """
    try:
        await page.get_by_role('textbox', name='Full Name').click()
        await page.get_by_role('textbox', name='Full Name').fill(kwargs.get('full_name', ''))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Email Address').click()
        await page.get_by_role('textbox', name='Email Address').fill(kwargs.get('email_address', ''))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Type of Consultation').select_option(kwargs.get('type_of_consultation', ''))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Preferred Date').fill(kwargs.get('preferred_date', ''))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Preferred Time').select_option(kwargs.get('preferred_time', ''))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Additional Comments').click()
        await page.get_by_role('textbox', name='Additional Comments').fill(kwargs.get('additional_comments', ''))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('button', name='Schedule Consultation').click()
    except:
        pass
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/finance-banking/financial-planning"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
