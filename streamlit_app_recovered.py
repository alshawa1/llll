{{ CHECKPOINT 74 }}
**The earlier parts of this conversation have been truncated due to its long length. The following content summarizes the truncated context so that you may continue your work. **


# User Requests
The following were user requests from the truncated conversation in chronological order:
1. كمل ولما تخلص رنه
2. TypeError: 'None' is of type <class 'NoneType'>, which is not an accepted type. label only accepts: str. Please convert the label to an accepted type.
Traceback:
File "C:\Users\dell\Downloads\فايلات مهاره\streamlit_app.py", line 1203, in <module>
st.metric(label=k, value=str(v))
~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\dell\anaconda3\Lib\site-packages\streamlit\runtime\metrics_util.py", line 444, in wrapped_func
result = non_optional_func(*args, **kwargs)
File "C:\Users\dell\anaconda3\Lib\site-packages\streamlit\elements\metric.py", line 192, in metric
metric_proto.label = _parse_label(label)
~~~~~~~~~~~~^^^^^^^
File "C:\Users\dell\anaconda3\Lib\site-packages\streamlit\elements\metric.py", line 216, in _parse_label
raise TypeError(
...<2 lines>...
)
Ask Google
Ask ChatGPT
❌ حدث خطأ أثناء تشغيل النظام: 'None' is of type <class 'NoneType'>, which is not an accepted type. label only accepts: str. Ple
<truncated 129 bytes>
3. العملاء المستهدفه كلها غلط فين الرولز الي انا قولتلك عليها تطبقها 
وانت بتنزل شيت ليه بتمسح انا قولتلك متغيرش اي داتا اصليه
4. انت نسيت لما قولنا تزود دول وقولت فكره حلوه ؟
معالجة الأخطاء الإملائية واللغوية الشائعة:


final_afrad = header + "\ndef run_afrad_app():\n" + indented_body

with open(afrad_app, "w", encoding="utf-8") as f:
f.write(final_afrad)
print("Created افراد_app.py")
else:
print("Could not split content properly!")

# Step 4: Write the NEW streamlit_app.py
new_streamlit_content = """import streamlit as st

st.set_page_config(page_title='مهاره سيستم', page_icon='\u2696\ufe0f', layout='wide', initial_sidebar_state='collapsed')

# CSS
st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');

html, body, [class*="css"], .stApp {
font-family: 'Cairo', sans-serif !important;
direction: RTL;
background-color: #0d0e1a !important;
}

.stApp {
background: radial-gradient(ellipse at top left, #1a0a2e 0%, #0d0e1a 60%) !important;
color: #e2e8f0 !important;
}

.login-card {
background: rgba(30, 10, 60, 0.6);
backdrop-filter: blur(10px);
border: 1px solid rgba(124, 58, 237, 0.4);
border-radius: 20px;
padding: 50px;
max-width: 450px;
margin: 100px auto;
text-align: center;
box-shadow: 0 10px 40px rgba(124, 58, 237, 0.2);
}

.logo-text {
font-size: 56px;
font-weight: 900;
background: linear-gradient(135deg, #a855f7, #7c3aed, #4f2d7f);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
line-height: 1.2;
}

.subtitle {
color: #a78bfa;
font-size: 18px;
margin-bottom: 20px;
}

.purple-divider {
height: 3px;
background: linear-gradient(90deg, transparent, #7c3aed, #a855f7, #7c3aed, transparent);
border-radius: 3px;
margin: 20px 0;
}

.stTextInput input {
background: rgba(79, 45, 127, 0.1) !important;
border: 1px solid rgba(79, 45, 127, 0.4) !important;
border-radius: 10px !important;
color: #e2e8f0 !important;
direction: RTL !important;
text-align: center;
}

.stButton > button {
background: linear-gradient(135deg, #4f2d7f 0%, #7c3aed 100%) !important;
color: white !important;
border: none !important;
border-radius: 10px;
font-weight: 700 !important;
font-size: 16px;
padding: 10px 24px;
box-shadow: 0 4px 15px rgba(124, 58, 237, 0.35);
width: 100%;
margin-top: 15px;
}

.footer {
color: #475569;
font-size: 12px;
margin-top: 30px;
}
</style>
''', unsafe_allow_html=True)

if 'authenticated' not in st.session_state:
st.session_state.authenticated = False
if 'sector' not in st.session_state:
st.session_state.sector = None

if not st.session_state.authenticated:
st.markdown('''
<div class="login-card">
<div class="logo-text">مهاره</div>
<div class="subtitle">نظام إدارة عمليات التحصيل</div>
<div class="purple-divider"></div>
</div>
''', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1.2, 1])
with col2:
pwd = st.text_input('كلمة المرور', type='password', label_visibility='collapsed', placeholder='أدخل كلمة المرور...')
if st.button('تسجيل الدخول'):
if pwd == '333':
st.session_state.authenticated = True
st.session_state.sector = 'افراد'
st.rerun()
elif pwd == '444':
st.session_state.authenticated = True
st.session_state.sector = 'اعمال'
st.rerun()
else:
st.error('❌ كلمة المرور غير صحيحة')

st.markdown('<div class="footer" style="text-align:center;">مهاره لتحصيل الديون © 2026</div>', unsafe_allow_html=True)
st.stop()

# Logged in
with st.sidebar:
if st.button('🚪 تسجيل الخروج', use_container_width=True):
st.session_state.authenticated = False
st.session_state.sector = None
st.rerun()

if st.session_state.sector == 'افراد':
import افراد_app
افراد_app.run_afrad_app()
elif st.session_state.sector == 'اعمال':
import اعمال_app
اعمال_app.run_aamal_app()
"""

with open(orig_app, "w", encoding="utf-8") as f:
f.write(new_streamlit_content)
print("Updated streamlit_app.py")

border: 1px solid rgba(124, 58, 237, 0.4);
border-radius: 16px 16px 4px 16px;
padding: 12px 16px;
margin: 8px 0;
font-size: 14px;
direction: RTL;
}
.chat-bubble-ai {
background: rgba(15, 23, 42, 0.7);
border: 1px solid rgba(79, 45, 127, 0.3);
border-radius: 16px 16px 16px 4px;
padding: 14px 18px;
margin: 8px 0;
font-size: 14px;
direction: RTL;
line-height: 1.8;
}
.chat-avatar-ai {
width: 28px; height: 28px;
border-radius: 50%;
background: linear-gradient(135deg, #4f2d7f, #7c3aed);
display: inline-flex; align-items: center; justify-content: center;
font-size: 12px; margin-left: 8px;
}

/* ─── عنوان بطاقة الـ AI ─── */
.ai-header-card {
background: linear-gradient(135deg, rgba(79,45,127,0.3) 0%, rgba(124,58,237,0.15) 100%);
border: 1px solid rgba(124, 58, 237, 0.4);
border-radius: 16px;
padding: 20px 24px;
margin-bottom: 16px;
direction: RTL;
}

/* ─── شاشة كلمة المرور ─── */
.login-card {
background: linear-gradient(135deg, rgba(79,45,127,0.25) 0%, rgba(30,10,60,0.8) 100%);
border: 1px solid rgba(124, 58, 237, 0.5);
border-radius: 24px;
padding: 48px 40px;
max-width: 480px;
margin: 60px auto;
box-shadow: 0 20px 60px rgba(79, 45, 127, 0.4);
direction: RTL;
text-align: center;
}

/* ─── عنوان STC ─── */
.stc-logo-text {
font-size: 52px;
font-weight: 900;
background: linear-gradient(135deg, #a855f7, #7c3aed, #4f2d7f);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
letter-spacing: 2px;
line-height: 1;
}
.stc-tagline {
color: #a78bfa;
font-size: 15px;
margin-top: 4px;
}

/* ─── شريط الفصل الأرجواني ─── */
.purple-divider {
height: 3px;
background: linear-gradient(90deg, transparent, #7c3aed, #a855f7, #7c3aed, transparent);
border-radius: 3px;
margin: 12px 0;
}

/* ─── Spinner Shimmer ─── */
@keyframes shimmer {
0% { background-position: -200% center; }
100% { background-position: 200% center; }
}
.loading-text {
background: linear-gradient(90deg, #4f2d7f, #a855f7, #4f2d7f);
background-size: 200% auto;
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
animation: shimmer 2s linear infinite;
}

/* ─── DataFrames ─── */
[data-testid="stDataFrame"] {
border-radius: 12px;
overflow: hidden;
border: 1px solid rgba(79, 45, 127, 0.3);
}

/* ─── File Uploader ─── */
[data-testid="stFileUploader"] {
background: rgba(79, 45, 127, 0.08) !important;
border: 2px dashed rgba(124, 58, 237, 0.4) !important;
border-radius: 14px !important;
padding: 12px;
transition: border-color 0.2s, background 0.2s;
}
[data-testid="stFileUploader"]:hover {
border-color: rgba(124, 58, 237, 0.7) !important;
background: rgba(79, 45, 127, 0.14) !important;
}

/* ─── RTL كامل ─── */
.stMarkdown, .stSelectbox, .stFileUploader, .stButton,
.stMultiSelect, .stDateInput, .stTextArea, p, label {
direction: RTL;
text-align: right !important;
}
</style>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
#  🔒 بوابة كلمة المرور
# ════════════════════════════════════════════════════════════════════
if "authenticated" not in st.session_state:
st.session_state.authenticated = False

if not st.session_state.authenticated:
col_l, col_c, col_r = st.columns([1, 1.4, 1])
with col_c:
st.markdown("""
<div class="login-card">
<div class="stc-logo-text">STC</div>
<div class="stc-tagline">Operations AI Copilot</div>
<div class="purple-divider" style="margin:20px 0;"></div>
<p style="color:#94a3b8; font-size:14px; margin-bottom:24px;">
🔐 هذا النظام مخصص لفريق عمليات STC فقط<br>أدخل كلمة المرور للمتابعة
</p>
</div>
""", unsafe_allow_html=True)

pwd_input = st.text_input(
"كلمة المرور",
type="password",
placeholder="أدخل كلمة المرور هنا...",
key="pwd_input",
label_visibility="collapsed"
)
login_btn = st.button("🔓 دخول", use_container_width=True)

if login_btn or (pwd_input and pwd_input == "333"):
if pwd_input == "333":
st.session_state.authenticated = True
st.rerun()
else:
st.error("❌ كلمة المرور غير صحيحة. حاول مرة أخرى.")
st.stop()


# ════════════════════════════════════════════════════════════════════
#  تعريف الموديولات
# ════════════════════════════════════════════════════════════════════
MODULES = {
"ai_copilot": {
"name": "🤖 AI Operations Copilot",
"desc": "مساعد الذكاء الاصطناعي لقسم العمليات. يفهم بياناتك، يحللها، ويجيب عن أي سؤال باللغة الطبيعية.",
"id": 99,
"files": [
{"key": "portfolio", "label": "ملف المحفظة (.xlsx)", "required": True},
{"key": "payments", "label": "ملف السدادات (.xlsx) - اختياري", "required": False}
]
},
"rotation": {
"name": "🔄 السحب والتدوير",
"desc": "سحب جميع عملاء محصل معين وإعادة توزيعهم بالتساوي على باقي المحصليين التابعين لنفس المشرف، مع الحفاظ على جميع مديونيات العميل الواحد لدى نفس المحصل الجديد.",
"id": 6,
"files": [
{"key": "portfolio", "label": "ملف المحفظة الأساسية (.xlsx)", "required": True}
]
},
"contact": {
"name": "📞 التوصل وعدم التوصل",
"desc": "تحليل وتصنيف العملاء بناءً على حالات التواصل الرئيسية والفرعية والمتابعة للوصول إلى التصنيف النهائي وتتبع محاولات الاتصال.",
"id": 2,
"files": [
{"key": "portfolio", "label": "ملف المحفظة الأساسية (.xlsx)", "required": True}
]
},
"targets": {
"name": "🎯 العملاء المستهدفة",
"desc": "تحديد العملاء ذوي الأولوية المرتفعة بناءً على متبقي السداد الموثق ونسب التغطية والتوجيهات المعتمدة.",
"id": 7,
"files": [
{"key": "portfolio", "label": "ملف المحفظة الأساسية (.xlsx)", "required": True}
]
},
"neglect": {
"name": "⏰ الإهمال والمتابعات",
"desc": "تحليل وتصنيف حالات الإهمال وتحديد العملاء غير المتابعين بناءً على أيام المتابعة وآخر محاولة تواصل.",
"id": 3,
"files": [
{"key": "portfolio", "label": "ملف المحفظة الأساسية (.xlsx)", "required": True}
]
},
"errors": {
"name": "🔴 أخطاء النظام والوعود",
"desc": "كشف وتوثيق الأخطاء في بيانات المحفظة والمطابقة مع وعود السداد النشطة أو المنتهية لتصحيح حالة العميل.",
"id": 1,
"files": [
{"key": "portfolio", "label": "ملف المحفظة الأساسية (.xlsx)", "required": True},
{"key": "promise", "label": "ملف وعود السداد (.xlsx) - اختياري", "required": False}
]
},
"balancing": {
"name": "⚖️ سحب وتوزيع المحافظ",
"desc": "إعادة توزيع العملاء من محافظ مصدر على محافظ هدف بخوارزمية ذكية تحقق توازناً مزدوجاً في عدد العملاء وإجمالي متبقي السداد بين جميع المحصلين المستهدفين.",
"id": 8,
"files": [
{"key": "portfolio", "label": "ملف المحفظة الأساسية (.xlsx)", "required": True}
]
},
"operations": {
"name": "📊 مركز تقارير العمليات",
"desc": "تقرير يومي وأسبوعي وشهري شامل بنسب التغطية والسدادات ومتبقي المديونية مع Pivot Tables وDashboard تفاعلية دون أي تعديل على البيانات الأصلية.",
"id": 9,
"files": [
{"key": "portfolio", "label": "ملف المحفظة الموزعة (.xlsx) - مطلوب", "required": True},
{"key": "payments", "label": "ملف السدادات (.xlsx) - اختياري", "required": False}
]
},
"electronic": {
"name": "💻 التحصيل الإلكتروني",
"desc": "تحليل أداء التحصيل الإلكتروني وعرض نسب التغطية والتوصل مع إمكانية التصفية حسب الفرع والمشرف وبناء ملخص بناءً على الـ Segment ونوع الخدمة.",
"id": 10,
"files": [
{"key": "portfolio", "label": "ملف التحصيل الإلكتروني (الكتروني.xlsx)", "required": True}
]
}
}


# ════════════════════════════════════════════════════════════════════
#  دوال مساعدة
# ════════════════════════════════════════════════════════════════════
@st.cache_data(show_spinner="⏳ جارٍ قراءة وتحميل البيانات بأقصى سرعة...")
def read_excel_calamine(file_path: str) -> pl.DataFrame:
try:
return pl.read_excel(file_path, engine="calamine").select([
pl.col(c).cast(pl.String, strict=False).fill_null("").str.strip_chars().alias(c)
for c in pl.read_excel(file_path, engine="calamine").columns
])
except Exception as e:
from python_calamine import CalamineWorkbook
wb = CalamineWorkbook.from_path(file_path)
sheet = wb.get_sheet_by_name(wb.sheet_names[0])
data = sheet.to_python()
if not data:
return pl.DataFrame()
headers = []
seen = {}
for i, h in enumerate(data[0]):
h_str = str(h).strip() if h is not None else f"Column_{i}"
if not h_str:
h_str = f"Column_{i}"
if h_str in seen:
seen[h_str] += 1
h_str = f"{h_str}_{seen[h_str]}"
else:
seen[h_str] = 0
headers.append(h_str)
records = data[1:]
str_records = [
[str(cell) if cell is not None else "" for cell in row]
for row in records
]
return pl.DataFrame(str_records, schema=headers, orient="row")


@st.cache_data
def scan_portfolio_for_balancing(file_path):
try:
df = read_excel_calamine(file_path)
from modules.module8_balancing import PortfolioBalancingModule
portfolios = PortfolioBalancingModule.get_portfolios(df)
collector_map = PortfolioBalancingModule.get_collectors_per_portfolio(df)
return portfolios, collector_map
except Exception as e:
st.error(f"حدث خطأ أثناء فحص الملف: {e}")
return [], {}


@st.cache_data
def scan_portfolio_for_operations(file_path):
try:
df = read_excel_calamine(file_path)
from modules.module9_operations_report import OperationsReportModule
return OperationsReportModule.get_filter_options(df)
except Exception as e:
st.error(f"حدث خطأ أثناء فحص ملف العمليات: {e}")
return {}


@st.cache_data
def scan_portfolio_for_targeting(file_path):
try:
df = read_excel_calamine(file_path)
from modules.module11_targeting_report import TargetingReportModule
return TargetingReportModule.get_supervisors_and_collectors(df)
except Exception as e:
st.error(f"حدث خطأ أثناء فحص ملف المحفظة للاستهداف: {e}")
return {}


@st.cache_data
def scan_portfolio_for_electronic(file_path):
try:
df = read_excel_calamine(file_path)
from modules.module9_operations_report import _detect
branch_col = _detect(df, ["الفرع", "branch"])
sup_col = _detect(df, ["المشرف", "supervisor"])
branches = df[branch_col].drop_nulls().unique().to_list() if branch_col else []
supervisors = df[sup_col].drop_nulls().unique().to_list() if sup_col else []
return {"branches": sorted([str(x) for x in branches if str(x).strip()]), 
"supervisors": sorted([str(x) for x in supervisors if str(x).strip()])}
except Exception as e:
st.error(f"حدث خطأ أثناء فحص ملف التحصيل الإلكتروني: {e}")
return {}


@st.cache_data
def scan_portfolio_for_rotation(file_path):
try:
df = read_excel_calamine(file_path)
from modules.module6b_rotation import PortfolioRotationModule
supervisors = PortfolioRotationModule.get_supervisors(df)
mapping = {}
for sup in supervisors:
mapping[sup] = PortfolioRotationModule.get_collectors_for_supervisor(df, sup)
return mapping
except Exception as e:
st.error(f"حدث خطأ أثناء فحص الملف: {e}")
return None


@st.cache_data
def load_portfolio_df(file_path):
"""تحميل إطار البيانات من ملف المحفظة"""
return read_excel_calamine(file_path)




# ════════════════════════════════════════════════════════════════════
#  الشريط الجانبي - STC Header + Navigation
# ════════════════════════════════════════════════════════════════════
with st.sidebar:
# شعار STC
st.markdown("""
<div style="text-align:center; padding: 20px 0 10px 0;">
<div class="stc-logo-text">STC</div>
<div class="stc-tagline">Operations AI Copilot</div>
<div class="purple-divider"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='color:#a78bfa; font-size:13px; text-align:center; margin-bottom:12px;'>⚙️ البرامج المتاحة</p>", unsafe_allow_html=True)

selected_key = st.radio(
label="اختر البرنامج:",
options=list(MODULES.keys()),
format_func=lambda k: MODULES[k]["name"],
label_visibility="collapsed"
)

st.markdown("<div class='purple-divider'></div>", unsafe_allow_html=True)

# زر تسجيل الخروج
if st.button("🔒 تسجيل الخروج", use_container_width=True):
st.session_state.authenticated = False
st.session_state.pop("ai_portfolio_df", None)
st.session_state.pop("ai_payments_df", None)
st.session_state.pop("chat_history", None)
st.session_state.pop("ai_supervisors", None)
st.rerun()

st.markdown("""
<div style='text-align:center; margin-top:20px; color:#475569; font-size:11px;'>
STC Operations © 2026<br>جميع الحقوق محفوظة
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
#  الرأس الرئيسي للصفحة
# ════════════════════════════════════════════════════════════════════
module_info = MODULES[selected_key]

# Header بطاقة عليا
if selected_key == "ai_copilot":
st.markdown("""
<div class="ai-header-card">
<div style="display:flex; align-items:center; gap:16px; flex-direction:row-reverse;">
<div style="font-size:48px; line-height:1;">🤖</div>
<div>
<div style="font-size:24px; font-weight:800; color:#e2e8f0;">
AI Operations Copilot
</div>
<div style="color:#a78bfa; font-size:14px; margin-top:4px;">
مساعد الذكاء الاصطناعي لقسم العمليات — يفهم بياناتك ويجيب عن أي سؤال
</div>
<div class="purple-divider" style="margin:10px 0 0 0; width:200px;"></div>
</div>
</div>
</div>
""", unsafe_allow_html=True)
else:
st.markdown(f"""
<div style="padding: 16px 0 8px 0;">
<h2 style="color:#c084fc; font-weight:800; margin-bottom:4px;">{module_info['name']}</h2>
<div class="purple-divider" style="width:120px;"></div>
</div>
""", unsafe_allow_html=True)
st.info(module_info["desc"])


# ════════════════════════════════════════════════════════════════════
#  🤖 واجهة AI Operations Copilot
# ════════════════════════════════════════════════════════════════════
if selected_key == "ai_copilot":

<div class="purple-divider" style="width:120px;"></div>
</div>
""", unsafe_allow_html=True)
st.info(module_info["desc"])


# ════════════════════════════════════════════════════════════════════
#  🤖 واجهة AI Operations Copilot
# ════════════════════════════════════════════════════════════════════
if selected_key == "ai_copilot":

# تهيئة الحالة
if "chat_history" not in st.session_state:
st.session_state.chat_history = []
if "ai_portfolio_df" not in st.session_state:
st.session_state.ai_portfolio_df = None
if "ai_payments_df" not in st.session_state:
st.session_state.ai_payments_df = None
if "ai_supervisors" not in st.session_state:
st.session_state.ai_supervisors = []
if "ai_selected_sups" not in st.session_state:
st.session_state.ai_selected_sups = []

# ─── قسم رفع الملفات ───
st.markdown("#### 📂 رفع الملفات")
col_p, col_pay = st.columns(2)

with col_p:
port_file = st.file_uploader("ملف المحفظة (.xlsx) *", type=["xlsx", "xls"], key="ai_port_file")
with col_pay:
pay_file = st.file_uploader("ملف السدادات (.xlsx) - اختياري", type=["xlsx", "xls"], key="ai_pay_file")

if port_file:
with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
tmp.write(port_file.getbuffer())
tmp_path = tmp.name
try:
df_port = load_portfolio_df(tmp_path)
st.session_state.ai_portfolio_df = df_port
sup_col = detect_supervisor_column(df_port)
if sup_col:
all_sups = sorted(df_port[sup_col].cast(pl.String).drop_nulls().unique().to_list())
st.session_state.ai_supervisors = all_sups
else:
st.session_state.ai_supervisors = []
st.success(f"✅ تم تحميل المحفظة — {len(df_port):,} عميل | {len(df_port.columns)} عمود")
except Exception as e:
st.error(f"خطأ في قراءة ملف المحفظة: {e}")
finally:
try:
os.unlink(tmp_path)
except:
pass

if pay_file:
with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
tmp.write(pay_file.getbuffer())
tmp_path = tmp.name
try:
df_pay = load_portfolio_df(tmp_path)
st.session_state.ai_payments_df = df_pay
st.success(f"✅ تم تحميل السدادات — {len(df_pay):,} صف")
except Exception as e:
st.error(f"خطأ في قراءة ملف السدادات: {e}")
finally:
try:
os.unlink(tmp_path)
except:
pass

# ─── فلتر المشرفين ───
if st.session_state.ai_portfolio_df is not None:
st.markdown("<div class='purple-divider'></div>", unsafe_allow_html=True)
st.markdown("#### 👥 تحديد نطاق العمل (المشرفين)")
st.caption("اختر المشرفين الذين تريد أن يعمل الـ AI على بياناتهم. اتركها فارغة للعمل على الكل.")

sups_all = st.session_state.ai_supervisors
if sups_all:
selected_sups = st.multiselect(
"اختر المشرفين:",
options=sups_all,
default=st.session_state.ai_selected_sups,
key="sup_multiselect",
label_visibility="collapsed"
)
st.session_state.ai_selected_sups = selected_sups
if selected_sups:
st.info(f"🔍 العمل على: {', '.join(selected_sups)} ({len(selected_sups)} مشرف)")
else:
st.info("🌐 العمل على المحفظة الكاملة (جميع المشرفين)")
else:
st.warning("⚠️ لم يتم اكتشاف عمود المشرفين تلقائياً. سيعمل الـ AI على كامل المحفظة.")

# ─── واجهة الدردشة ───
st.markdown("<div class='purple-divider'></div>", unsafe_allow_html=True)
st.markdown("#### 🧠 تحدث مع AI Operations Copilot")

# عرض رسائل المحادثة
chat_container = st.container()
with chat_container:
if not st.session_state.chat_history:
st.markdown("""
<div class="chat-bubble-ai">
<strong>🤖 مرحباً!</strong> أنا AI Operations Copilot الخاص بـ STC.<br><br>
يمكنني الإجابة عن أي سؤال حول محفظتك. جرب مثلاً:<br>
• <em>كم نسبة التغطية اليوم؟</em><br>
• <em>كم عدد العملاء الإجمالي؟</em><br>
• <em>من أفضل مشرف في المحفظة؟</em><br>
• <em>ما توصيتك لتحسين الأداء؟</em><br>
• <em>كم إجمالي متبقي السداد؟</em>
</div>
""", unsafe_allow_html=True)

for msg in st.session_state.chat_history:
if msg["role"] == "user":
st.markdown(f"""
<div class="chat-bubble-user">
<strong>👤 أنت:</strong><br>{msg['content']}
</div>
""", unsafe_allow_html=True)
else:
st.markdown(f"""
<div class="chat-bubble-ai">
<strong>🤖 AI Copilot:</strong><br>{msg['content']}
</div>
""", unsafe_allow_html=True)

# حقل الإدخال
col_q, col_send = st.columns([5, 1])
with col_q:
user_question = st.text_input(
"اسأل الـ AI...",
placeholder="مثال: كم نسبة التغطية اليوم؟",
key="ai_question",
label_visibility="collapsed"
)
with col_send:
send_btn = st.button("✉️ إرسال", use_container_width=True)

col_clr, _ = st.columns([1, 4])
with col_clr:
if st.button("🗑️ مسح المحادثة", use_container_width=True):
st.session_state.chat_history = []
st.rerun()

if (send_btn or user_question) and user_question and user_question.strip():
if send_btn or True:
# حفظ سؤال المستخدم
st.session_state.chat_history.append({"role": "user", "content": user_question})

# تشغيل الـ AI
with st.spinner("🤖 AI يحلل بياناتك..."):
try:
from core.knowledge_base import CopilotKnowledgeBase
from core.ai_copilot import AIOperationsCopilot

kb = CopilotKnowledgeBase()
copilot = AIOperationsCopilot(
portfolio_df=st.session_state.ai_portfolio_df,
payments_df=st.session_state.ai_payments_df,
kb=kb
)
answer = copilot.ask(
question=user_question,
selected_supervisors=st.session_state.ai_selected_sups or None
)
except Exception as e:
answer = f"⚠️ حدث خطأ أثناء تحليل البيانات: {e}"

st.session_state.chat_history.append({"role": "ai", "content": answer})
st.rerun()

else:
st.markdown("""
<div style="
text-align:center;
padding: 60px 20px;
color: #64748b;
border: 2px dashed rgba(79,45,127,0.3);
border-radius: 20px;
margin-top: 24px;
">
<div style="font-size:64px; margin-bottom:16                    if dest_count == 0:
st.error("⚠️ يرجى تحديد محصل مستقبل واحد على الأقل لنقل العملاء إليه!")
else:
smart_check = st.checkbox(
"🚨 تفعيل التوجيه والتعيين الذكي بحسب حالة العميل (رصيد 0 ⬅️ opertaions / سلبي ⬅️ test / إيجابي ⬅️ المحصل الجديد)",
value=False,
help="في حال عدم تفعيل الخيار: يتم توزيع كامل عملاء المحصل بشكل طبيعي دون تطبيق شروط opertaions أو test."
)
if smart_check:
st.info(
"💡 **التوجيه والتعيين الذكي مفعّل:**\n"
"- 🔵 **عملاء متبقي سداد صفر أو أقل:** يُسند المحصل الجديد واليوزر كـ `opertaions`.\n"
"- 🔴 **العملاء السلبيون (رافض/لايرد/مقطوع/مغلق):** يُسند اليوزر الجديد كـ `test`.\n"
"- 🟢 **العملاء الإيجابيون:** يُوزعون بالتساوي على المحصلين المستقبلين وتحديد يوزرهم وتحديث مشرفهم الجديد تلقائياً."
)
st.success(
f"✅ سيتم سحب عملاء **'{withdrawn_names_str}'** "
f"({len(selected_cols)} محصلين) وتوزيعهم على "
f"**{dest_count} محصلين مستقبلين**."
)
# supervisor = أول مشرف مختار (للـ fallback في module)
rotation_params["supervisor"] = selected_sups[0]
rotation_params["collector"] = selected_cols
rotation_params["target_collectors"] = target_cols_sel if target_cols_sel else None
rotation_params["smart_assignment"] = smart_check      with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp_scan:
tmp_scan.write(portfolio_file.getbuffer())
tmp_scan_path = tmp_scan.name
try:
mapping = scan_portfolio_for_rotation(tmp_scan_path)
if mapping:
all_sups = sorted(list(mapping.keys()))
# كل المحصلين في الملف
all_collectors_map = {c: sup for sup, cols in mapping.items() for c in cols}

st.markdown("#### 🔄 إعدادات السحب وإعادة التوزيع")

# ── خطوة 1: اختيار مشرف/مشرفين ──
st.markdown("##### 1️⃣ اختر المشرف / المشرفين:")
selected_sups = st.multiselect(
"اختر مشرف واحد أو أكثر:",
options=all_sups,
help="يمكنك اختيار أكثر من مشرف — المحصلون المتاحون للسحب سيكونون من المشرفين المختارين"
)

# ── خطوة 2: المحصلون المسحوبون من المشرفين المختارين ──
if selected_sups:
pool_for_withdraw = sorted(list({c for sup in selected_sups for c in mapping.get(sup, [])}))
st.markdown("##### 2️⃣ اختر المحصل/المحصلين المراد **سحب** محافظهم:")
selected_cols = st.multiselect(
"المحصلون المتاحون للسحب (من المشرفين المختارين):",
options=pool_for_withdraw,
help="اختر محصل واحد أو أكثر لسحب محافظهم"
)
if selected_sups:
pool_for_withdraw = sorted(list({c for sup in selected_sups for c in mapping.get(sup, [])}))
st.markdown("##### 2️⃣ اختر المحصل/المحصلين المراد **سحب** محافظهم:")
selected_cols = st.multiselect(
"المحصلون المتاحون للسحب (من المشرفين المختارين):",
options=pool_for_withdraw,
help="اختر محصل واحد أو أكثر لسحب محافظهم"
)
else:
st.multiselect("2️⃣ اختر المحصل/المحصلين المراد سحب محافظهم:", ["-- اختر المشرف أولاً --"], disabled=True)
selected_cols = []

# ── خطوة 3: المحصلون المستقبلون ──
if selected_sups and selected_cols:
withdrawn_set = set(selected_cols)

# كل المحصلين في الملف ما عدا المسحوبين — مجمّعين حسب المشرف
st.markdown("##### 3️⃣ اختر المحصلين **المستقبلين** (لنقل العملاء إليهم):")

# عرض المحصلين مجمعين بالمشرف لوضوح أكثر
receiver_by_sup = {}
for sup, cols in mapping.items():
available = [c for c in cols if c not in withdrawn_set]
if available:
receiver_by_sup[sup] = available

# بناء options مع label واضح
all_receivers = sorted(list({c for cols in receiver_by_sup.values() for c in cols}))

# default = محصلو نفس المشرفين المختارين (غير المسحوبين)
default_receivers = sorted(list({
c for sup in selected_sups
for c in mapping.get(sup, [])
if c not in withdrawn_set

# ── معلومات إضافية: من أي مشرف كل مستقبل ──
if target_cols_sel:
info_lines = []
for c in target_cols_sel:
sup_of_c = all_collectors_map.get(c, "غير معروف")
info_lines.append(f"**{c}** (مشرفه: {sup_of_c})")
with st.expander("📋 تفاصيل المحصلين المستقبلين"):
st.markdown(" — ".join(info_lines))

dest_count = len(target_cols_sel) if target_cols_sel else len(default_receivers)
withdrawn_names_str = " | ".join(selected_cols)

if dest_count == 0:
st.error("⚠️ يرجى تحديد محصل مستقبل واحد على الأقل لنقل العملاء إليه!")
else:
smart_check = st.checkbox(
"🚨 تفعيل التوجيه والتعيين الذكي بحسب حالة العميل (رصيد 0 ⬅️ opertaions / سلبي ⬅️ test / إيجابي ⬅️ المحصل الجديد)",
value=False,
help="في حال عدم تفعيل الخيار: يتم توزيع كامل عملاء المحصل بشكل طبيعي دون تطبيق شروط opertaions أو test."

if dest_count == 0:
st.error("⚠️ يرجى تحديد محصل مستقبل واحد على الأقل لنقل العملاء إليه!")
else:
smart_check = st.checkbox(
"🚨 تفعيل التوجيه والتعيين الذكي بحسب حالة العميل (رصيد 0 ⬅️ opertaions / سلبي ⬅️ test / إيجابي ⬅️ المحصل الجديد)",
value=False,
help="في حال عدم تفعيل الخيار: يتم توزيع كامل عملاء المحصل بشكل طبيعي دون تطبيق شروط opertaions أو test."
)
if smart_check:
st.info(
"💡 **التوجيه والتعيين الذكي مفعّل:**\n"
"- 🔵 **عملاء متبقي سداد صفر أو أقل:** يُسند المحصل الجديد واليوزر كـ `opertaions`.\n"
"- 🔴 **العملاء السلبيون (رافض/لايرد/مقطوع/مغلق):** يُسند اليوزر الجديد كـ `test`.\n"
"- 🟢 **العملاء الإيجابيون:** يُوزعون بالتساوي على المحصلين المستقبلين وتحديد يوزرهم وتحديث مشرفهم الجديد تلقائياً."
)
st.success(
f"✅ سيتم سحب عملاء **'{withdrawn_names_str}'** "
f"({len(selected_cols)} محصلين) وتوزيعهم على "
f"**{dest_count} محصلين مستقبلين**."
)
except:
pass

# ─── واجهة سحب وتوزيع المحافظ ───
balancing_params = {}
source_ports: list = []
target_ports: list = []
if selected_key == "balancing" and uploaded_files.get("portfolio"):
portfolio_file = uploaded_files["portfolio"]
with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp_scan:
st.markdown("#### ⚖️ تحديد المحافظ")
c1, c2 = st.columns(2)
with c1:
st.markdown("المحافظ المصدر (السحب منها):")
source_ports = st.multiselect(
label="اختر محفظة أو أكثر لسحب عملائها:",
options=portfolios,
key="bal_source",
label_visibility="collapsed"
)
if source_ports:
total_source_col = sum(len(collector_map.get(p, [])) for p in source_ports)
st.info(f"👥 عدد المحصلين في المحافظ المصدر: **{total_source_col}**")
with c2:
st.markdown("المحافظ الهدف (التوزيع عليها):")
available_targets = [p for p in portfolios if p not in (source_ports or [])]
target_ports = st.multiselect(
label="اختر محفظة أو أكثر للتوزيع عليها:",
options=available_targets,
key="bal_target",
label_visibility="collapsed"
)
if target_ports:
total_target_col = sum(len(collector_map.get(p, [])) for p in target_ports)
st.info(f"👥 عدد المحصلين في المحافظ الهدف: **{total_target_col}**")
if source_ports:
if target_ports:
overlap = set(source_ports) & set(target_ports)
if overlap:
st.error(f"⚠️ لا يمكن أن تكون المحفظة مصدراً وهدفاً في نفس الوقت: {', '.join(overlap)}")
else:
st.success(f"✅ سيتم سحب عملاء **{' | '.join(source_ports)}** وتوزيعهم على محصلي **{' | '.join(target_ports)}**.")
else:
st.success(f"✅ سيتم سحب وتوزيع عملاء **{' | '.join(source_ports)}** بالتساوي داخل كل محفظة.")
st.markdown("##### ⚙️ إعدادات التوازن والتفاوت المسموح")
col_a, col_b, col_c = st.columns(3)
with col_a:
max_cnt_diff = st.number_input(
"أقصى تفاوت في عدد العملاء:",
min_value=5, max_value=100, value=35, step=5,
help="أقصى فرق مسموح به بين أعلى محصل وأقل محصل في عدد العملاء (مثلاً 30 - 40 عميل)"
)
with col_b:
max_bal_diff = st.number_input(
"أقصى تفاوت في متبقي السداد:",
min_value=10000, max_value=300000, value=80000, step=5000,
help="أقصى فرق مسموح به بين أعلى محصل وأقل محصل في متبقي سداد موثق (مثلاً 70,000 - 90,000)"
)
with col_c:
min_customers_col = st.number_input(
"الحد الأدنى لعملاء المحصل:",
min_value=0, max_value=500, value=150, step=10,
help="لا يُسحب من محصل إذا كان عملائه سينزلون تحت هذا الحد. صفر = بلا حد أدنى"
)

withdraw_all_check = st.checkbox(
"🚨 سحب كامل عملاء المحفظة المصدر (100%) وتوزيعهم بالكامل على باقي المحافظ",
value=False,
help="عند تفعيل هذا الخيار، سيتم تفريغ المحفظة المصدر بنسبة 100% وإعادة توزيع كافة عملائها بالتساوي على باقي المحافظ/المحصلين"
)

if min_customers_col > 0:
st.info(f"🛡️ **حماية وتبادل ذكي**: لا ينزل أي محصل تحت **{min_customers_col}** عميل. لو رصيده أعلى من المتوسط يتم تبادل عملائه الغالية بأخرى رخيصة ليصل للتوازن.")

balancing_params["source"] = source_ports
g_col1, g_col2 = st.columns(2)
with g_col1:
def_cov = st.number_input("مستهدف التغطية الافتراضي (لكل محصل):", min_value=1, value=200, step=10)
with g_col2:
def_col = st.number_input("مستهدف التحصيل الافتراضي (لكل محصل):", min_value=1, value=1000, step=100)

supervisor_targets = {}
if sup_col_map:
st.markdown("##### 👥 تحديد مستهدفات المشرفين والمحصلين:")
for sup_name, collectors in sup_col_map.items():
with st.expander(f"📌 المشرف: {sup_name} ({len(collectors)} محصل)", expanded=True):
c_t1, c_t2 = st.columns(2)
with c_t1:
cov_t = st.number_input(f"مستهدف تغطية محصلي {sup_name}:", min_value=1, value=def_cov, key=f"cov_{sup_name}")
portfolio_file = uploaded_files["portfolio"]
with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp_scan:
tmp_scan.write(portfolio_file.getbuffer())
tmp_scan_path = tmp_scan.name
try:
filter_options = scan_portfolio_for_operations(tmp_scan_path)
sup_col_map = scan_portfolio_for_targeting(tmp_scan_path)
if filter_options:
st.markdown("---")
st.markdown("### 🏢 Reports Center - مركز التقارير")

rep_cat = st.radio(
"اختر فئة التقرير المطلوب:",
options=["📊 التقرير العملياتي الشامل", "🎯 تقرير أداء الاستهداف (تغطية وتحصيل حسب المستهدف)"],
index=0,
horizontal=True
)

if "أداء الاستهداف" in rep_cat:
ops_params["is_targeting_report"] = True
st.info("🎯 تقرير أداء الاستهداف — يتيح تحديد مستهدف التغطية ومستهدف التحصيل لكل محصل ومقارنته بالأداء الفعلي:")

col_mode, _ = st.columns([3, 1])
with col_mode:
rep_type = st.radio(
"اختر نوع التقرير الزمنية:",
options=["📅 Daily (يومي)", "🗓 Weekly (أسبوعي)", "📆 Monthly (شهري)"],
index=0,
horizontal=True
)

st.markdown("##### ⏱️ إعدادات الفترة الزمنية")
if "Daily" in rep_type:
ops_params["report_mode"] = "daily"
d_val = st.date_input("تاريخ التقرير اليومي:", datetime.today())
ops_params["target_date"] = d_val.strftime("%Y-%m-%d")
elif "Weekly" in rep_type:
ops_params["report_mode"] = "weekly"
w_cols = st.columns(2)
with w_cols[0]:
s_val = st.date_input("تاريخ البداية:", datetime.today() - timedelta(days=6))
with w_cols[1]:
e_val = st.date_input("تاريخ النهاية:", datetime.today())
ops_params["start_date"] = s_val.strftime("%Y-%m-%d")
ops_params["end_date"] = e_val.strftime("%Y-%m-%d")
elif "Monthly" in rep_type:
ops_params["report_mode"] = "monthly"
m_cols = st.columns(2)
curr_y = datetime.today().year
curr_m = datetime.today().month
with m_cols[0]:
m_val = st.selectbox("الشهر:", options=list(range(1, 13)), index=curr_m - 1)
with m_cols[1]:
y_val = st.selectbox("السنة:", options=list(range(2023, 2031)),
index=list(range(2023, 2031)).index(curr_y) if curr_y in range(2023, 2031) else 0)
ops_params["month"] = m_val
ops_params["year"] = y_val

st.markdown("##### 🎯 إعدادات المستهدفات (التغطية والتحصيل)")
g_col1, g_col2 = st.columns(2)
with g_col1:
def_cov = st.number_input("مستهدف التغطية الافتراضي (لكل محصل):", min_value=1, value=200, step=10)
with g_col2:
def_col = st.number_input("مستهدف التحصيل الافتراضي (لكل محصل):", min_value=1, value=1000, step=100)

supervisor_targets = {}
if sup_col_map:
st.markdown("##### 👥 تحديد المشرفين والمحصلين المستهدفين:")

all_sups = sorted(list(sup_col_map.keys()))
selected_sups = st.multiselect(
"اختر المشرفين المراد تضمينهم في التقرير:",
options=all_sups,
default=all_sups,
help="يمكنك إزالة أي مشرف لتجاهله هو ومحصلينه من التقرير"
)

for sup_name in selected_sups:
collectors = sup_col_map.get(sup_name, [])
with st.expander(f"📌 المشرف: {sup_name} ({len(collectors)} محصل)", expanded=True):
c_t1, c_t2 = st.columns(2)
with c_t1:
cov_t = st.number_input(f"مستهدف تغطية محصلي {sup_name}:", min_value=1, value=def_cov, key=f"cov_{sup_name}")
with c_t2:
col_t = st.number_input(f"مستهدف تحصيل محصلي {sup_name}:", min_value=1, value=def_col, key=f"col_{sup_name}")

sel_cols = st.multiselect(
f"تحديد محصلي المشرف {sup_name}:",
options=collectors,
default=collectors,
key=f"cols_{sup_name}"
)
if sel_cols:
supervisor_targets[sup_name] = {
"coverage_target": cov_t,
"collection_target": col_t,
"collectors": sel_cols
}

ops_params["supervisor_targets"] = supervisor_targets

r = ContactStatusModule().run(portfolio)
stats.update(r["stats"])
writer.write_contact(r["data"], r["pivot_supervisor"], r["pivot_collector"], r["pivot_status"])

elif task_id == 3:
from modules.module3_neglect import NeglectModule
r = NeglectModule().run(portfolio)
stats.update(r["stats"])
writer.write_neglect(r["data"], r["full_analysis"], r["pivot_summary"],
r["pivot_supervisor"], r["pivot_collector"], r["pivot_status"],
r["pivot_branch"], r["pivot_portfolio"], r["pivot_days"])

elif task_id == 7:
from modules.module7_targets import TargetCustomersModule
r = TargetCustomersModule().run(portfolio, promise, pl.DataFrame())
stats.update(r["stats"])
writer.write_targets(r["data"], r["pivot_supervisor"])

elif task_id == 6:
sup = rotation_params["supervisor"]
col = rotation_params["collector"]
tgt_cols = rotation_params.get("target_collectors")
from modules.module6b_rotation import PortfolioRotationModule
r = PortfolioRotationModule().run(portfolio, col, sup, target_collectors=tgt_cols)
stats.update(r["stats"])
writer.write_rotation(r["data"], r["execution_report"],
r["distribution_summary"], r["withdrawal_summary"])

elif task_id == 8:
from modules.module8_balancing import PortfolioBalancingModule
tgt = balancing_params.get("target") or None
r = PortfolioBalancingModule().run(
portfolio,
source_portfolios=balancing_params["source"],
target_portfolios=tgt,
min_receiver_chunk=balancing_params.get("chunk", 200)
)
stats.update(r["stats"])
writer.write_balancing(r["data"], r["summary_pivot"],
r.get("planning_sheet"), r.get("source_summary"),
r.get("final_result_sheet"))

elif task_id == 9:
from modules.module9_operations_report import OperationsReportModule
pmt_df = dfs.get("payments")
r = OperationsReportModule().run(
portfolio,
payments=pmt_df,
report_mode=ops_params.get("report_mode", "daily"),
target_date=ops_params.get("target_date"),
start_date=ops_params.get("start_date"),
end_date=ops_params.get("end_date"),
month=ops_params.get("month"),
year=ops_params.get("year"),
supervisors=ops_params.get("supervisors"),
collectors=ops_params.get("collectors"),
portfolios=ops_params.get("portfolios"),
main_statuses=ops_params.get("main_statuses"),
sub_statuses=ops_params.get("sub_statuses"),
)
stats.update(r["stats"])
writer.write_operations_report(
r["data"], r["pivot_supervisor"], r["pivot_collector"],
r["pivot_portfolio"], r.get("pivot_main_status"), r.get("pivot_sub_status"),
r.get("top10_supervisors"), r.get("top10_collectors"),
r.get("top10_portfolios"), r["stats"],
)

elif task_id == 10:
from modules.module10_electronic_collection import ElectronicCollectionModule
r = ElectronicCollectionModule().run(
portfolio,
report_mode=elec_params.get("report_mode", "coverage"),
target_date=elec_params.get("target_date"),
start_date=elec_params.get("start_date"),
end_date=elec_params.get("end_date"),
branches=elec_params.get("branches"),
supervisors=elec_params.get("supervisors")
)
if "error" in r:
st.error(r["error"])
st.stop()
stats.update(r["stats"])
writer.write_electronic_collection(
r["data"], r["pivot_supervisor"], r["pivot_collector"],
r["pivot_segment"], r["stats"]
)

if task_id not in [10]:
writer.write_dashboard(stats, task_id)
writer.write_summary(stats)
writer.save()

st.balloons()
st.success("✨ اكتملت معالجة البيانات بنجاح وتم إنشاء التقرير المنسق!")

# ─── عرض الإحصائيات ───
st.markdown("#### 📊 ملخص نتائج التقرير")
stats_cols = st.columns(min(len(stats), 4))
for j, (k, v) in enumerate(stats.items()):
col_idx = j % len(stats_cols)
with stats_cols[col_idx]:
st.metric(label=k, value=str(v))

# عرض أفضل مشرف وأفضل محصل إذا كان تقرير العمليات
if task_id == 9 and 'r' in locals():
best_sup = r.get("best_supervisor", "غير محدد")
best_col = r.get("best_collector", "غير محدد")
if best_sup != "غير محدد" or best_col != "غير محدد":
r = NeglectModule().run(portfolio)
stats.update(r["stats"])
writer.write_neglect(r["data"], r["full_analysis"], r["pivot_summary"],
r["pivot_supervisor"], r["pivot_collector"], r["pivot_status"],
r["pivot_branch"], r["pivot_portfolio"], r["pivot_days"])

elif task_id == 7:
from modules.module7_targets import TargetCustomersModule
r = TargetCustomersModule().run(portfolio, promise, pl.DataFrame())
stats.update(r["stats"])
writer.write_targets(r["data"], r["pivot_supervisor"])

elif task_id == 6:
sup = rotation_params["supervisor"]
col = rotation_params["collector"]
tgt_cols = rotation_params.get("target_collectors")
from modules.module6b_rotation import PortfolioRotationModule
r = PortfolioRotationModule().run(portfolio, col, sup, target_collectors=tgt_cols)
stats.update(r["stats"])
writer.write_rotation(r["data"], r["execution_report"],
r["distribution_summary"], r["withdrawal_summary"])

elif task_id == 8:
from modules.module8_balancing import PortfolioBalancingModule
tgt = balancing_params.get("target") or None
r = PortfolioBalancingModule().run(
portfolio,
source_portfolios=balancing_params["source"],
target_portfolios=tgt,
min_receiver_chunk=balancing_params.get("chunk", 200)
)
stats.update(r["stats"])
writer.write_balancing(r["data"], r["summary_pivot"],
r.get("planning_sheet"), r.get("source_summary"),
r.get("final_result_sheet"))

elif task_id == 9:
if ops_params.get("is_targeting_report"):
from modules.module11_targeting_report import TargetingReportModule
pmt_df = dfs.get("payments", pl.DataFrame())
r = TargetingReportModule().run(
portfolio,
payments=pmt_df,
report_mode=ops_params.get("report_mode", "daily"),
target_date=ops_params.get("target_date"),
start_date=ops_params.get("start_date"),
end_date=ops_params.get("end_date"),
month=ops_params.get("month"),
year=ops_params.get("year"),
supervisor_targets=ops_params.get("supervisor_targets"),
)
path_map[PROMISE_PAY] = tmp_path
elif key == "payments":
path_map["payments"] = tmp_path

dfs, results = load_files(path_map)
for k, vr in results.items():
if not vr.is_valid:
st.error(f"❌ الملف {k} غير صالح: {vr.summary()}")
st.stop()
writer.write_neglect(r["data"], r["full_analysis"], r["pivot_summary"],
r["pivot_supervisor"], r["pivot_collector"], r["pivot_status"],
r["pivot_branch"], r["pivot_portfolio"], r["pivot_days"])

elif task_id == 7:
from modules.module7_targets import TargetCustomersModule
r = TargetCustomersModule().run(portfolio, promise, pl.DataFrame())
stats.update(r["stats"])
writer.write_targets(r["data"], r["pivot_supervisor"])

elif task_id == 6:
sup = rotation_params["supervisor"]
col = rotation_params["collector"]
tgt_cols = rotation_params.get("target_collectors")
from modules.module6b_rotation import PortfolioRotationModule
r = PortfolioRotationModule().run(portfolio, col, sup, target_collectors=tgt_cols)
stats.update(r["stats"])
writer.write_rotation(r["data"], r["execution_report"],
r["distribution_summary"], r["withdrawal_summary"])

from modules.module7_targets import TargetCustomersModule
r = TargetCustomersModule().run(portfolio, promise, pl.DataFrame())
stats.update(r["stats"])
writer.write_targets(r["data"], r["pivot_supervisor"])

from modules.module7_targets import TargetCustomersModule
r = TargetCustomersModule().run(portfolio, promise, pl.DataFrame())
stats.update(r["stats"])
writer.write_targets(r["data"], r["pivot_supervisor"])

elif task_id == 6:
sup = rotation_params["supervisor"]
col = rotation_params["collector"]
tgt_cols = rotation_params.get("target_collectors")
from modules.module6b_rotation import PortfolioRotationModule
r = PortfolioRotationModule().run(portfolio, col, sup, target_collectors=tgt_cols)
stats.update(r["stats"])
writer.write_rotation(r["data"], r["execution_report"],
r["distribution_summary"], r["withdrawal_summary"])
portfolio,
source_portfolios=balancing_params["source"],
target_portfolios=tgt,
min_customers_per_collector=balancing_params.get("min_per_col", 0),
max_count_diff=balancing_params.get("max_count_diff", 35),
max_balance_diff=float(balancing_params.get("max_bal_diff", 80000.0)),
withdraw_all_source=balancing_params.get("withdraw_all", False),
)
stats.update(r["stats"])
writer.write_balancing(r["data"], r["summary_pivot"],
r.get("planning_sheet"), r.get("source_summary"),
r.get("final_result_sheet"))

elif task_id == 9:
if ops_params.get("is_targeting_report"):
from modules.module11_targeting_report import TargetingReportModule
pmt_df = dfs.get("payments", pl.DataFrame())
r = TargetingReportModule().run(
portfolio,
payments=pmt_df,
report_mode=ops_params.get("report_mode", "daily"),
target_date=ops_params.get("target_date"),
start_date=ops_params.get("start_date"),
end_date=ops_params.get("end_date"),
month=ops_params.get("month"),
year=ops_params.get("year"),
supervisor_targets=ops_params.get("supervisor_targets"),
)
if "error" in r:
st.error(r["error"])
st.stop()
stats.update(r.get("stats", {}))
writer.write_targeting_report(r["data"], r.get("stats"))
else:
from modules.module9_operations_report import OperationsReportModule
pmt_df = dfs.get("payments")
r = OperationsReportModule().run(
portfolio,
payments=pmt_df,
report_mode=ops_params.get("report_mode", "daily"),
target_date=ops_params.get("target_date"),
start_date=ops_params.get("start_date"),
end_date=ops_params.get("end_date"),
month=ops_params.get("month"),
year=ops_params.get("year"),
supervisors=ops_params.get("supervisors"),
collectors=ops_params.get("collectors"),
portfolios=ops_params.get("portfolios"),
main_statuses=ops_params.get("main_statuses"),
sub_statuses=ops_params.get("sub_statuses"),
)
stats.update(r["stats"])
writer.write_operations_report(
r["data"], r["pivot_supervisor"], r["pivot_collector"],
r["pivot_portfolio"], r.get("pivot_main_status"), r.get("pivot_sub_status"),
r.get("top10_supervisors"), r.get("top10_collectors"),
r.get("top10_portfolios"), r["stats"],
)

elif task_id == 10:
from modules.module10_electronic_collection import ElectronicCollectionModule
r = ElectronicCollectionModule().run(
portfolio,
report_mode=elec_params.get("report_mode", "coverage"),
target_date=elec_params.get("target_date"),
start_date=elec_params.get("start_date"),
end_date=elec_params.get("end_date"),
branches=elec_params.get("branches"),
supervisors=elec_params.get("supervisors")
)
if "error" in r:
st.error(r["error"])

elif task_id == 10:
from modules.module10_electronic_collection import ElectronicCollectionModule
r = ElectronicCollectionModule().run(
portfolio,
report_mode=elec_params.get("report_mode", "coverage"),
target_date=elec_params.get("target_date"),
start_date=elec_params.get("start_date"),
end_date=elec_params.get("end_date"),
branches=elec_params.get("branches"),
supervisors=elec_params.get("supervisors")
)
if "error" in r:
st.error(r["error"])
st.stop()
stats.update(r["stats"])
writer.write_electronic_collection(
r["data"], r["pivot_supervisor"], r["pivot_collector"],
r["pivot_segment"], r["stats"]
st.success("✨ اكتملت معالجة البيانات بنجاح وتم إنشاء التقرير المنسق!")

# ─── عرض الإحصائيات ───
st.markdown("#### 📊 ملخص نتائج التقرير")
stats_cols = st.columns(min(len(stats), 4))
for j, (k, v) in enumerate(stats.items()):
col_idx = j % len(stats_cols)
with stats_cols[col_idx]:
st.metric(label=str(k) if k is not None else "غير مصنف", value=str(v))

# عرض أفضل مشرف وأفضل محصل إذا كان تقرير العمليات
if task_id == 9 and 'r' in locals():
best_sup = r.get("best_supervisor", "غير محدد")
best_col = r.get("best_collector", "غير محدد")
if best_sup != "غير محدد" or best_col != "غير محدد":
st.markdown("---")
st.markdown("### 🏆 نجوم وأبطال الأداء الفردي")
c_hero1, c_hero2 = st.columns(2)
with c_hero1:
st.markdown(f"""
<div style="background: linear-gradient(135deg, rgba(79, 45, 127, 0.4), rgba(124, 58, 237, 0.2)); border: 2px solid #7c3aed; border-radius: 16px; padding: 20px; text-align: center; color: white;">
<h3 style="color: #fbbf24; margin-bottom: 5px;">أفضل مشرف أداء</h3>
<h2 style="color: #ffffff; margin-top: 0;">{best_sup}</h2>
<p style="color: #cbd5e1; font-size: 0.95rem;">أعلى نسبة تغطية وتواصل وتحصيل مالي متميز</p>
</div>
""", unsafe_allow_html=True)
with c_hero2:
st.markdown(f"""
<div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.3), rgba(6, 182, 212, 0.2)); border: 2px solid #10b981; border-radius: 16px; padding: 20px; text-align: center; color: white;">
<h3 style="color: #34d399; margin-bottom: 5px;">أفضل محصل أداء</h3>
<h2 style="color: #ffffff; margin-top: 0;">{best_col}</h2>
<p style="color: #cbd5e1; font-size: 0.95rem;">أعلى معدل تواصل ونسبة إغلاق وسداد موثق</p>
</div>
""", unsafe_allow_html=True)

# جدول ملخص تقرير الاستهداف أو ملخص العمليات التنفيذي (Module 9)
if task_id == 9 and 'r' in locals() and ops_params.get("is_targeting_report"):
st.markdown("---")
st.markdown("### 🎯 جدول تقرير أداء الاستهداف (تغطية وتحصيل)")
st.caption("مقارنة الأداء الفعلي بمستهدف التغطية ومستهدف التحصيل لكل مشرف ومحصل:")
st.dataframe(r["data"].to_pandas(), use_container_width=True, hide_index=True)
elif task_id == 9 and 'r' in locals() and "pivot_supervisor" in r:
st.markdown("---")
st.markdown("### 📋 الملخص التنفيذي للإدارة (Executive Summary)")
st.caption("نظرة شاملة وسريعة لأداء كافة المشرفين من حيث التغطية، معدل التواصل، والتحصيل المالي.")

st.markdown("### 🎯 جدول تقرير أداء الاستهداف (تغطية وتحصيل)")
st.caption("مقارنة الأداء الفعلي بمستهدف التغطية ومستهدف التحصيل لكل مشرف ومحصل:")
st.dataframe(r["data"].to_pandas(), use_container_width=True, hide_index=True)
elif task_id == 9 and 'r' in locals() and "pivot_supervisor" in r:
st.markdown("---")
st.markdown("### 📋 الملخص التنفيذي للإدارة (Executive Summary)")
st.caption("نظرة شاملة وسريعة لأداء كافة المشرفين من حيث التغطية، معدل التواصل، والتحصيل المالي.")

sup_df = r["pivot_supervisor"]
display_cols = ["المشرف", "عدد العملاء", "تمت التغطية", "نسبة التغطية %", "نسبة التوصل %", "إجمالي السداد", "نسبة التحصيل %"]
cols_to_show = [c for c in display_cols if c in sup_df.columns]

if cols_to_show:
show_df = sup_df.select(cols_to_show)
# استبعاد صف الإجمالي إذا كان يحتوي على رموز لتجنب تشوه الرسم البياني
show_df = show_df.filter(~pl.col("المشرف").cast(pl.String).str.contains("الإجمالي|📉|📈"))

st.dataframe(
show_df.to_pandas(), 
use_container_width=True, 
hide_index=True,
column_config={
"المشرف": st.column_config.TextColumn("👤 المشرف", width="medium"),
"عدد العملاء": st.column_config.NumberColumn("👥 العملاء", format="%d"),
"تمت التغطية": st.column_config.NumberColumn("✅ تمت التغطية", format="%d"),
"نسبة التغطية %": st.column_config.ProgressColumn(
"🎯 التغطية %", help="نسبة العملاء الذين تمت تغطيتهم", format="%.2f%%", min_value=0, max_value=100
),
"نسبة التوصل %": st.column_config.ProgressColumn(
"📞 التوصل %", help="نسبة التواصل الفعال", format="%.2f%%", min_value=0, max_value=100
),
"إجمالي السداد": st.column_config.NumberColumn(
"💰 التحصيل (ريال)", help="إجمالي المبالغ المحصلة", format="%.2f ﷼"
),
"نسبة التحصيل %": st.column_config.ProgressColumn(
"📈 نسبة التحصيل %", help="نسبة السداد للمديونية", format="%.2f%%", min_value=0, max_value=100
)
}
)

# جدول ملخص التحصيل الإلكتروني التنفيذي (Module 10)
if task_id == 10 and 'r' in locals() and "pivot_supervisor" in r:
st.markdown("---")
task_mode = elec_params.get("report_mode", "task1_contact")
if task_mode == "task1_contact":
st.markdown("### 📋 جدول ملخص حالات التواصل والنسب (Executive Summary)")
st.caption("يعرض إحصائيات التواصل الفعال، عدم التواصل، والحالات المغلقة/لا يرد مع النسب المئوية للمحفظة.")
disp_cols = ["المشرف", "عدد العملاء", "توصل", "نسبة التوصل %", "عدم توصل", "نسبة عدم التوصل %", "لايرد-مغلق", "نسبة لايرد ومغلق %"]
elif task_mode == "task2_coverage":
st.markdown("### 📋 جدول ملخص نسبة التغطية والنسب (Executive Summary)")
st.caption("يعرض نسبة العملاء المغطين وغير المغطين بناءً على تاريخ التغطية المحدد.")
disp_cols = ["المشرف", "عدد العملاء", "العملاء المغطين", "نسبة التغطية %", "غير المغطين", "نسبة عدم التغطية %"]
else:
st.markdown("### 📋 جدول الملخص التنفيذي الشامل (Executive Summary)")
st.caption("تقرير شامل يجمع أداء المشرفين والقطاعات ونسب التغطية والتواصل.")
disp_cols = ["المشرف", "عدد العملاء", "العملاء المغطين", "نسبة التغطية %", "توصل", "نسبة التوصل %"]

sup_df = r["pivot_supervisor"]
cols_to_show = [c for c in disp_cols if c in sup_df.columns]
if cols_to_show:
show_df = sup_df.select(cols_to_show)
st.dataframe(show_df.to_pandas(), use_container_width=True, hide_index=True)

if task_mode == "task3_comprehensive" and "pivot_segment" in r and not r["pivot_segment"].is_empty():
st.markdown("#### 🧩 ملخص القطاعات (Segment) ونوع الخدمة الموثقة")
st.dataframe(r["pivot_segment"].to_pandas(), use_container_width=True, hide_index=True)

# جدول توزيع المحصلين (Module 8)
if task_id == 8 and 'r' in locals() and "summary_pivot" in r:
st.markdown("---")
st.markdown("#### 📋 جدول ملخص التوزيع النهائي للمحصلين")
summary_df = r["summary_pivot"]
target_cols = ["المحصل", "المحصل الجديد", "اليوزر", "عدد العملاء بعد", "عدد العملاء", "إجمالي متبقي السداد"]
cols_to_show = [c for c in target_cols if c in summary_df.columns]
if cols_to_show:
show_df = summary_df.select(cols_to_show)
first_col = cols_to_show[0]
show_df = show_df.filter(~pl.col(first_col).cast(pl.String).str.contains("📉|📈"))
st.dataframe(show_df.to_pandas(), use_container_width=True, hide_index=True)

# ─── زر التحميل ───
with open(out_path, "rb") as f_out:
excel_bytes = f_out.read()

ts_str = datetime.now().strftime("%Y%m%d_%H%M%S")
download_name = f"مهاره_{selected_key}_{ts_str}.xlsx"

st.markdown("<div class='purple-divider'></div>", unsafe_allow_html=True)
st.download_button(
label="📥 تحميل التقرير النهائي (Excel Styled)",
data=excel_bytes,
file_name=download_name,
mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
use_container_width=True
)

except Exception as e:
st.exception(e)
st.error(f"❌ حدث خطأ أثناء تشغيل النظام: {e}")

finally:
for p in temp_files:
try:
os.unlink(p)
except:
pass
