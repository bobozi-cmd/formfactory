
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写并提交 Bug 报告表单",
        "experience": "",
        "parameters": {
            "bug_title": "Bug 标题, 变量类型: str",
            "severity_level": "严重性级别, {'Critical': 'Critical', 'High': 'High', 'Medium': 'Medium', 'Low': 'Low'}, 变量类型: str",
            "environment": "环境, 使用 ',' 分割, 变量类型: str",
            "browser_platform": "浏览器/平台的格式如: Chrome 96.0, Windows 10, 变量类型: str",
            "steps_to_reproduce": "重现步骤, 使用 1. 2. 3. 标记, 变量类型: str",
            "expected_behavior": "期望的行为, 变量类型: str",
            "actual_behavior": "实际的行为, 变量类型: str",
            "your_name": "填写者的名字, 变量类型: str",
            "your_email": "填写者的邮箱, 变量类型: str"
        }
    }
    """
    try:
        await page.get_by_role('textbox', name='Bug Title').click()
        await page.get_by_role('textbox', name='Bug Title').fill(kwargs['bug_title'])
    except Exception as e:
        print(f'Error filling Bug Title: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Severity Level').select_option(kwargs['severity_level'])
    except Exception as e:
        print(f'Error selecting Severity Level: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Environment').click()
        await page.get_by_role('textbox', name='Environment').fill(kwargs['environment'])
    except Exception as e:
        print(f'Error filling Environment: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Browser/Platform').click()
        await page.get_by_role('textbox', name='Browser/Platform').fill(kwargs['browser_platform'])
    except Exception as e:
        print(f'Error filling Browser/Platform: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Steps to Reproduce').click()
        await page.get_by_role('textbox', name='Steps to Reproduce').fill(kwargs['steps_to_reproduce'])
    except Exception as e:
        print(f'Error filling Steps to Reproduce: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Expected Behavior').click()
        await page.get_by_role('textbox', name='Expected Behavior').fill(kwargs['expected_behavior'])
    except Exception as e:
        print(f'Error filling Expected Behavior: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Actual Behavior').click()
        await page.get_by_role('textbox', name='Actual Behavior').fill(kwargs['actual_behavior'])
    except Exception as e:
        print(f'Error filling Actual Behavior: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Your Name').click()
        await page.get_by_role('textbox', name='Your Name').fill(kwargs['your_name'])
    except Exception as e:
        print(f'Error filling Your Name: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Your Email').click()
        await page.get_by_role('textbox', name='Your Email').fill(kwargs['your_email'])
    except Exception as e:
        print(f'Error filling Your Email: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('button', name='Submit Bug Report').click()
    except Exception as e:
        print(f'Error clicking Submit Bug Report: {e}')
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/tech-software/bug-report"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
