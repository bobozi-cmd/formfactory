
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填充并提交文学杂志提交表单",
        "experience": "",
        "parameters": {
            "author_name": "作者的姓名, 变量类型: str",
            "email": "作者的电子邮件地址, 变量类型: str",
            "work_title": "作品标题, 变量类型: str",
            "genre": "作品类型, {'': 'Select Genre', 'Poetry': 'Poetry', 'Fiction': 'Fiction', 'Non-Fiction': 'Non-Fiction', 'Essay': 'Essay', 'Literary Review': 'Literary Review'}, 变量类型: str",
            "word_count": "作品字数 (Poetry: max 100 lines; Fiction: 1000-7500 words; Non-Fiction: 1000-5000 words), 变量类型: int",
            "abstract": "作品的摘要或简述 (max 300 words), 变量类型: str",
            "issue": "优选发表期刊, {'Spring 2024': 'Spring 2024', 'Summer 2024': 'Summer 2024', 'Fall 2024': 'Fall 2024', 'Winter 2024': 'Winter 2024'}, 变量类型: str",
            "previously_published": "作品以前是否发表过, 变量类型: bool",
            "simultaneous_submission": "此作品是否为同时提交, 变量类型: bool",
            "terms": "是否同意提交指南和出版条款, 变量类型: bool"
        }
    }
    """
    try:
        await page.get_by_role('textbox', name='Author Name *').click()
        await page.get_by_role('textbox', name='Author Name *').fill(kwargs.get('author_name', 'AAA'))
    except Exception as e:
        print(f'Error filling author_name: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Email Address *').click()
        await page.get_by_role('textbox', name='Email Address *').fill(kwargs.get('email', '1212@qq.com'))
    except Exception as e:
        print(f'Error filling email: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Title *').click()
        await page.get_by_role('textbox', name='Title *').fill(kwargs.get('work_title', 'BBB'))
    except Exception as e:
        print(f'Error filling work_title: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.locator('form div').filter(has_text='Genre * Select Genre Poetry').nth(3).click()
        await page.get_by_label('Genre *').select_option(kwargs.get('genre', 'Poetry'))
    except Exception as e:
        print(f'Error selecting genre: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('spinbutton', name='Word Count *').click()
        await page.get_by_role('spinbutton', name='Word Count *').fill(str(kwargs.get('word_count', 100)))
    except Exception as e:
        print(f'Error filling word_count: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Abstract/Summary *').click()
        await page.get_by_role('textbox', name='Abstract/Summary *').fill(kwargs.get('abstract', 'Brief desc'))
    except Exception as e:
        print(f'Error filling abstract: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Preferred Issue').select_option(kwargs.get('issue', 'Fall 2024'))
    except Exception as e:
        print(f'Error selecting issue: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        if kwargs.get('previously_published', True):
            await page.get_by_role('checkbox', name='This work has been previously').check()
    except Exception as e:
        print(f'Error checking previously_published: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        if kwargs.get('simultaneous_submission', True):
            await page.get_by_role('checkbox', name='This is a simultaneous').check()
    except Exception as e:
        print(f'Error checking simultaneous_submission: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        if kwargs.get('terms', True):
            await page.get_by_role('checkbox', name='I agree to the submission').check()
    except Exception as e:
        print(f'Error checking terms: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('button', name='Submit Work').click()
    except Exception as e:
        print(f'Error clicking submit button: {e}')
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/arts-creative/literary-submission"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
