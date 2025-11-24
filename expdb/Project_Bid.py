
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "在施工项目提交页面填入信息并提交表单",
        "experience": "",
        "parameters": {
            "company_name": "公司名称, 文本格式, 变量类型: str",
            "license_number": "承包商许可证号码, 文本格式, 变量类型: str",
            "project_name": "项目名称, 文本格式, 变量类型: str",
            "bid_amount": "投标金额, 以美元计, 正数, 变量类型: int",
            "project_duration": "预计工期, 周数, 正整数, 变量类型: int",
            "start_date": "拟开工日期, 格式 YYYY-MM-DD, 变量类型: str",
            "completion_date": "预计完成日期, 格式 YYYY-MM-DD, 变量类型: str",
            "work_description": "详细工作描述, 可能为空, 文本格式, 变量类型: str",
            "contact_person": "联系人姓名, 可能为空, 文本格式, 变量类型: str",
            "phone_number": "联系人电话号码, 可能为空, 文本格式, 变量类型: str"
        }
    }
    """
    try:
        await page.get_by_role('textbox', name='Company Name').click()
        await page.get_by_role('textbox', name='Company Name').fill(kwargs.get('company_name' ))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Contractor License Number').click()
        await page.get_by_role('textbox', name='Contractor License Number').fill(kwargs.get('license_number' ))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Project Name').click()
        await page.get_by_role('textbox', name='Project Name').fill(kwargs.get('project_name' ))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('spinbutton', name='Bid Amount ($)').click()
        await page.get_by_role('spinbutton', name='Bid Amount ($)').fill(str(kwargs.get('bid_amount' )))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('spinbutton', name='Estimated Duration (weeks)').click()
        await page.get_by_role('spinbutton', name='Estimated Duration (weeks)').fill(str(kwargs.get('project_duration' )))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Proposed Start Date').fill(kwargs.get('start_date' ))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Estimated Completion Date').fill(kwargs.get('completion_date' ))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Detailed Work Description').click()
        await page.get_by_role('textbox', name='Detailed Work Description').fill(kwargs.get('work_description' ))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Contact Person').click()
        await page.get_by_role('textbox', name='Contact Person').fill(kwargs.get('contact_person' ))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Phone Number').click()
        await page.get_by_role('textbox', name='Phone Number').fill(kwargs.get('phone_number' ))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('button', name='Submit Bid').click()
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/construction-manufacturing/project-bid"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
