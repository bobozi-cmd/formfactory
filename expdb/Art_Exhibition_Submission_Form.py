
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "完成艺术展览提交表单",
        "experience": "",
        "parameters": {
            "artist_name": "艺术家的名字, 变量类型: str",
            "email": "艺术家的邮箱地址, 变量类型: str",
            "artwork_title": "艺术品的标题, 变量类型: str",
            "medium": "艺术作品的媒介, {'Painting', 'Sculpture', 'Photography', 'Digital Art', 'Mixed Media'}, 变量类型: str",
            "dimensions": "艺术品的尺寸(以厘米为单位), 格式例如 '100x80x5', 变量类型: str",
            "year": "艺术品创作年份, 范围为1900至2024, 变量类型: int",
            "description": "艺术品的描述, 变量类型: str",
            "exhibition_period": "首选展览时间段, {'Spring 2024', 'Summer 2024', 'Fall 2024', 'Winter 2024'}, 变量类型: str",
            "for_sale": "是否可供出售, 变量类型: bool"
        }
    }
    """
    try:
        await page.get_by_role('textbox', name='Artist Name *').fill(kwargs.get('artist_name', 'AB'))
    except Exception as e:
        print('Failed to set artist_name:', e)
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Email Address *').fill(kwargs.get('email', '22332@qq.com'))
    except Exception as e:
        print('Failed to set email:', e)
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Artwork Title *').fill(kwargs.get('artwork_title', 'HHHH'))
    except Exception as e:
        print('Failed to set artwork_title:', e)
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Medium *').select_option(kwargs.get('medium', 'Photography'))
    except Exception as e:
        print('Failed to select medium:', e)
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Dimensions (in cm) *').fill(kwargs.get('dimensions', '100x80x5'))
    except Exception as e:
        print('Failed to set dimensions:', e)
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('spinbutton', name='Year Created *').fill(str(kwargs.get('year', 2000)))
    except Exception as e:
        print('Failed to set year:', e)
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Artwork Description *').fill(kwargs.get('description', 'abccdaf'))
    except Exception as e:
        print('Failed to set description:', e)
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Preferred Exhibition Period').select_option(kwargs.get('exhibition_period', 'Summer 2024'))
    except Exception as e:
        print('Failed to select exhibition_period:', e)
    await asyncio.sleep(INTERVAL)
    try:
        if kwargs.get('for_sale', True):
            await page.get_by_role('checkbox', name='Artwork is available for sale').check()
    except Exception as e:
        print('Failed to set for_sale:', e)
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('button', name='Submit Artwork').click()
    except Exception as e:
        print('Submit failed:', e)
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/arts-creative/exhibition-submission"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
