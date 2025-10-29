
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写论文提交表单并提交",
        "experience": "用于指导一个新手视觉大模型执行相关任务的详细操作说明。填写论文提交表单时，应遵循以下步骤：\n\n1. 'Author Name' 字段：\n   - 点击并选中输入框。\n   - 输入作者的名字。\n\n2. 'Email' 字段：\n   - 点击并选中输入框。\n   - 输入有效的电子邮件地址，确保格式正确。\n\n3. 'Paper Title' 字段：\n   - 点击并选中输入框。\n   - 输入论文标题。\n\n4. 'Abstract' 字段：\n   - 点击并选中多行文本框。\n   - 输入简要论文摘要。\n\n5. 'Keywords' 字段：\n   - 点击并选中输入框。\n   - 输入关键词，用逗号分隔。\n\n6. 'Paper Category' 选择框：\n   - 点击以展开可选项。\n   - 选择正确的分类，例如 'Data Science'。\n\n7. 'Submit Paper' 按钮：\n   - 点击提交表单。",
        "parameters": {
            "author_name": "作者姓名, 变量类型: str",
            "email": "邮箱地址, 变量类型: str",
            "paper_title": "论文标题, 变量类型: str",
            "abstract": "论文摘要, 变量类型: str",
            "keywords": "关键词, 用逗号分隔, 变量类型: str",
            "paper_category": "论文类别, 变量类型: str, 具体选项包括: 'Renewable Energy', 'Environmental Science', 'Marketing Technology', 'Biotechnology', 'Quantum Computing', 'Psychology', 'Data Science', 'Neuroscience', 'Transportation Technology', 'Healthcare Technology', 'Telecommunication', 'Agriculture Technology', 'Artificial Intelligence', 'Cloud Computing', 'Robotics', 'Social Sciences', 'Materials Science', 'Education Technology', 'Urban Studies', 'Nanotechnology', 'Blockchain Technology', 'Design', 'Digital Media'"
        }
    }
    """
    await page.get_by_role('textbox', name='Author Name').click()
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Author Name').fill(kwargs['author_name'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Email').click()
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Email').fill(kwargs['email'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Paper Title').click()
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Paper Title').fill(kwargs['paper_title'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Abstract').click()
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Abstract').fill(kwargs['abstract'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Keywords').click()
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Keywords').fill(kwargs['keywords'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_label('Paper Category').select_option(kwargs['paper_category'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('button', name='Submit Paper').click()
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/academic-research/paper-submission"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
