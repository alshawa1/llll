# -*- coding: utf-8 -*-
# نظام قطاع الأعمال - مهاره سيستم
import streamlit as st
import sys
import os
import re
import importlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BIZ_DIR = os.path.join(BASE_DIR, "قطاع اعمال للاتصالات")

def purge_colliding_modules():
    colliding = ['core', 'data', 'utils', 'export', 'modules', 'gui', 'pages', 'payment_analysis', 'powerbi_exporter', 'reports', 'business_rules']
    mods_to_del = [m for m in list(sys.modules.keys()) if m.split('.')[0] in colliding]
    mods_to_del.sort(key=lambda m: len(m.split('.')), reverse=True)
    for mod in mods_to_del:
        sys.modules.pop(mod, None)

    try:
        importlib.invalidate_caches()
    except Exception:
        pass

    while BIZ_DIR in sys.path:
        sys.path.remove(BIZ_DIR)
    sys.path.insert(0, BIZ_DIR)

def run_aamal_app():
    purge_colliding_modules()
    
    pages = {
        "لوحة التحكم": "01_لوحة_التحكم.py",
        "تحليل المحافظ": "02_تحليل_المحافظ.py",
        "أخطاء النظام": "03_أخطاء_النظام.py",
        "حالة الإهمال": "04_حالة_الإهمال.py",
        "السحب والتدوير": "05_السحب_والتدوير.py",
        "توازن المحافظ": "06_توازن_المحافظ.py",
        "التقارير": "07_التقارير.py",
        "تصدير Power BI": "08_تصدير_Power_BI.py",
    }
    
    with st.sidebar:
        st.markdown("### 🏢 قطاع الأعمال")
        selected_page = st.radio("اختر البرنامج:", list(pages.keys()), label_visibility="collapsed")
    
    page_file = os.path.join(BIZ_DIR, "pages", pages[selected_page])
    
    with open(page_file, "r", encoding="utf-8") as f:
        code = f.read()
    
    # Remove st.set_page_config calls
    code = re.sub(r"st\.set_page_config\([^)]*\)", "# set_page_config removed", code)
    
    exec(compile(code, page_file, 'exec'), {'__name__': '__main__', '__file__': page_file})
