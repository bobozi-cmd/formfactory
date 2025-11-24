
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填充制造订单请求表单并提交",
        "experience": "",
        "parameters": {
            "company_name": "公司名称, 变量类型: str",
            "customer_account_number": "客户账号, 变量类型: str",
            "product_type": "产品类别, {'': 'Select product type', 'Custom Product': 'Custom Product', 'Standard Product': 'Standard Product', 'Product Modification': 'Product Modification'}, 变量类型: str",
            "product_description": "产品描述, 如果为空, 应处理异常., 变量类型: str",
            "quantity": "数量, 必须为大于0的整数., 变量类型: int",
            "dimensions": "产品尺寸, 格式为LxWxH, 如果格式错误, 应处理异常., 变量类型: str",
            "material": "材料, 变量类型: str",
            "technical_specifications": "技术规范, 如果为空, 应处理异常., 变量类型: str",
            "quality_standards": "质量标准, 如果为空, 应处理异常., 变量类型: str",
            "required_delivery_date": "要求的交货日期, 格式为YYYY-MM-DD., 变量类型: str",
            "preferred_shipping_method": "首选运输方式, {'': 'Select shipping method', 'Ground': 'Ground', 'Express': 'Express', 'Air Freight': 'Air Freight', 'Sea Freight': 'Sea Freight'}, 变量类型: str"
        }
    }
    """
    try:
        await page.get_by_role('textbox', name='Company Name').fill(kwargs.get('company_name'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Customer Account Number').fill(kwargs.get('customer_account_number'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Product Type').select_option(kwargs.get('product_type'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Product Description').fill(kwargs.get('product_description'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('spinbutton', name='Quantity').fill(str(kwargs.get('quantity' )))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Dimensions').fill(kwargs.get('dimensions' ))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Material').fill(kwargs.get('material' ))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Technical Specifications').fill(kwargs.get('technical_specifications'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Quality Standards').fill(kwargs.get('quality_standards'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Required Delivery Date').fill(kwargs.get('required_delivery_date'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Preferred Shipping Method').select_option(kwargs.get('preferred_shipping_method'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('button', name='Submit Order Request').click()
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/construction-manufacturing/order-request"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
