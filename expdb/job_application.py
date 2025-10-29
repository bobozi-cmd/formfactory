
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "用户填写并提交申请表",
        "experience": "用户需要填写求职申请表单中的每个输入框。首先，点击 'Applicant Name' 输入框并输入申请者的名字。接着，点击 'Position Applied For' 输入框并完善申请职位的名称，然后点击 'Preferred Department' 输入框并填写偏好的部门。在填写每项信息前，需先点击输入框以确保其被选中。最后，点击 'Cover Letter' 输入框并输入自荐信内容。所有信息填写完毕后，点击 'Submit Application' 按钮提交表单并接收成功提交的确认消息。",
        "parameters": {
            "applicant_name": "申请人姓名, 变量类型: str",
            "position_applied": "申请的职位, 变量类型: str",
            "preferred_department": "期望的部门, 变量类型: str",
            "cover_letter": "求职信内容, 变量类型: str"
        }
    }
    """
    await page.get_by_role('textbox', name='Applicant Name').click()
    await asyncio.sleep(0.3)
    await page.get_by_role('textbox', name='Applicant Name').fill(kwargs['applicant_name'])
    await asyncio.sleep(0.3)
    await page.get_by_role('textbox', name='Position Applied For').click()
    await asyncio.sleep(0.3)
    await page.get_by_role('textbox', name='Position Applied For').fill(kwargs['position_applied'])
    await asyncio.sleep(0.3)
    await page.get_by_role('textbox', name='Preferred Department').click()
    await asyncio.sleep(0.3)
    await page.get_by_role('textbox', name='Preferred Department').fill(kwargs['preferred_department'])
    await asyncio.sleep(0.3)
    await page.get_by_role('textbox', name='Cover Letter').click()
    await asyncio.sleep(0.3)
    await page.get_by_role('textbox', name='Cover Letter').fill(kwargs['cover_letter'])
    await asyncio.sleep(0.3)
    await page.get_by_role('button', name='Submit Application').click()
    await asyncio.sleep(0.3)

target_url = "http://127.0.0.1:5000/academic-research/job-application"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
