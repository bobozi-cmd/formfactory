
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写并提交NDA表单",
        "experience": "",
        "parameters": {
            "party_name": "参与方的名称, 不能为空., 变量类型: str",
            "party_type": "参与方的类型, {'individual': 'Individual', 'company': 'Company', 'partnership': 'Partnership'}, 变量类型: str",
            "purpose": "NDA的目的, 可以为空., 变量类型: str",
            "effective_date": "NDA的生效日期, 格式为'YYYY-MM-DD'., 变量类型: str",
            "duration_years": "NDA的年限, 必须为正整数., 变量类型: int",
            "rep_name": "负责人的名称, 可以为空., 变量类型: str",
            "rep_title": "负责人职称, 可以为空., 变量类型: str"
        }
    }
    """
    try:
        party_name = kwargs.get('party_name', 'AA')
        if not party_name.strip():
            raise ValueError('party_name cannot be empty')
        await page.get_by_role('textbox', name='Party Name (Individual/').click()
        await page.get_by_role('textbox', name='Party Name (Individual/').fill(party_name)
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        party_type = kwargs.get('party_type', 'company')
        await page.get_by_label('Party Type').select_option(party_type)
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        purpose = kwargs.get('purpose', '   ')
        await page.get_by_role('textbox', name='Purpose of NDA').click()
        await page.get_by_role('textbox', name='Purpose of NDA').fill(purpose)
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        effective_date = kwargs.get('effective_date', '1999-11-21')
        await page.get_by_role('textbox', name='Effective Date').press('ArrowRight')
        await page.get_by_role('textbox', name='Effective Date').fill(effective_date)
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        duration_years = kwargs.get('duration_years', '12')
        await page.get_by_role('spinbutton', name='Duration (Years)').click()
        await page.get_by_role('spinbutton', name='Duration (Years)').fill(duration_years)
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        rep_name = kwargs.get('rep_name', '  ')
        await page.get_by_role('textbox', name='Representative Name').click()
        await page.get_by_role('textbox', name='Representative Name').fill(rep_name)
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        rep_title = kwargs.get('rep_title', '  ')
        await page.get_by_role('textbox', name='Title/Position').click()
        await page.get_by_role('textbox', name='Title/Position').fill(rep_title)
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_text('I have read and agree to the').click()
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_text('I confirm that I have the').click()
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('button', name='Submit NDA').click()
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/legal-compliance/nda-submission"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
