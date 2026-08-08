import streamlit as st
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

st.set_page_config(page_title="أخطاء النظام", page_icon="⚠️", layout="wide")
st.markdown("<style>body{direction:rtl;text-align:right;}.stApp{direction:rtl;}</style>", unsafe_allow_html=True)

st.title("⚠️ فحص واكتشاف أخطاء النظام (16 قاعدة)")
st.markdown("##### نموذج تقييم أخطاء النظام — مهاره لتحصيل الديون")

from utils.page_upload import page_portfolio_uploader, render_supervisor_filter

df_full, column_map, raw_df = page_portfolio_uploader("page_03_errors", label="📂 ارفع ملف المحفظة لفحص أخطاء النظام (Excel)")

if df_full is None or df_full.empty:
    st.stop()

df = render_supervisor_filter(df_full, column_map, "page_03_errors")

try:
    from business_rules.system_errors import SystemErrorsEngine
    from reports.export import export_errors_report, export_errors, export_portfolio_with_summaries
except ImportError:
    SystemErrorsEngine = None

st.info("💡 اضغط على الزر أدناه لبدء فحص 16 قاعدة لأخطاء النظام:")
col_btn, col_space = st.columns([2, 3])
with col_btn:
    run_check = st.button("🚀 بدء فحص أخطاء النظام الآن", type="primary", use_container_width=True)

# ─────────────────────────────────────────────────────────────
# 1. فحص فائق السرعة (< 0.05s) بدون تجهيز مسبق لملفات الإكسيل
# ─────────────────────────────────────────────────────────────
if run_check:
    with st.spinner("جاري فحص 16 قاعدة للأخطاء..."):
        if SystemErrorsEngine:
            engine = SystemErrorsEngine()
            result = engine.detect(df, column_map)
            st.session_state['errors_result'] = result
            st.session_state['total_errors'] = result.get('total_errors', 0)
        else:
            st.error("محرك فحص الأخطاء غير متوفر")
            st.stop()

result = st.session_state.get('errors_result')
if result:
    df_errors = result['data']
    summary = result['summary']
    severity = result.get('error_counts_by_severity', {})
    total_errs = result['total_errors']

    st.markdown("---")
    st.markdown(f"### 📊 نتائج الفحص: تم اكتشاف **{total_errs:,}** خطأ تشغيلي")

    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("إجمالي الأخطاء", f"{total_errs:,}")
    m2.metric("Critical 🔴", f"{severity.get('Critical', 0):,}")
    m3.metric("High 🟠", f"{severity.get('High', 0):,}")
    m4.metric("Medium 🟡", f"{severity.get('Medium', 0):,}")
    m5.metric("Low 🟢", f"{severity.get('Low', 0):,}")

    st.markdown("---")

    # ─────────────────────────────────────────────────────────────
    # 2. أزرار تنزيل مباشرة (Lazy Execution عند التنزيل)
    # ─────────────────────────────────────────────────────────────
    st.markdown("### 📥 تنزيل شيت البيانات المعدل والتقارير:")
    c_dl1, c_dl2, c_dl3 = st.columns(3)

    with c_dl1:
        st.download_button(
            label="📥 تحميل التقرير النهائي (Excel Styled)",
            data=export_portfolio_with_summaries(
                clean_df=df,
                col_map=column_map,
                errors_df=df_errors,
                neglect_df=st.session_state.get('neglect_result', {}).get('data'),
                payment_df=st.session_state.get('payment_df')
            ),
            file_name="المحفظة_الأساسية_المعدلة_أخطاء_النظام.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            type="primary",
            use_container_width=True,
            key="dl_err_full_styled"
        )

    with c_dl2:
        st.download_button(
            label="📊 تنزيل التقرير الاحترافي (نموذج مهاره)",
            data=export_errors_report(df_errors, summary, column_map),
            file_name="نموذج_تقييم_أخطاء_النظام.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
            key="dl_err_pro_fast"
        )

    with c_dl3:
        st.download_button(
            label="📋 تنزيل تفاصيل الأخطاء فقط (Excel)",
            data=export_errors(df_errors),
            file_name="تفاصيل_أخطاء_النظام.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
            key="dl_err_raw_fast"
        )

    st.markdown("---")

    tabs = st.tabs(['📋 جدول الأخطاء التفصيلي', '📊 ملخص الأخطاء حسب النوع'])

    with tabs[0]:
        error_rows = df_errors[df_errors['نوع الخطأ'].astype(str).str.strip() != ''].copy()
        if not error_rows.empty:
            st.dataframe(error_rows, use_container_width=True, height=500)
        else:
            st.success("🎉 لم يتم العثور على أي أخطاء في المحفظة!")

    with tabs[1]:
        if summary:
            sum_df = pd.DataFrame(list(summary.items()), columns=['نوع الخطأ', 'عدد الحالات'])
            sum_df = sum_df.sort_values('عدد الحالات', ascending=False)
            st.dataframe(sum_df.style.format({'عدد الحالات': '{:,}'}), use_container_width=True)
else:
    st.info("👆 اضغط على زر **'🚀 بدء فحص أخطاء النظام الآن'** لعرض التحليل وأزرار التحميل.")
