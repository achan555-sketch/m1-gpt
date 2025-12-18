import streamlit as st
import pandas as pd
import numpy as np

# --- 画面設定 ---
st.title('🏆 M-1審査員タイプ診断')
st.write('あなたの採点傾向から、相性の良い審査員を判定します！')

# --- サイドバーで入力 ---
st.sidebar.header("あなたの採点を入力")
score1 = st.sidebar.slider('令和ロマン', 80, 100, 93)
score2 = st.sidebar.slider('ヤーレンズ', 80, 100, 92)
score3 = st.sidebar.slider('さや香', 80, 100, 89)

# --- 診断ボタン ---
if st.button('診断する！🚀'):
    st.write("🤖 分析中...")
    
    # 簡易診断ロジック（松本さん=厳しめ、上沼さん=高め と仮定）
    user_avg = (score1 + score2 + score3) / 3
    
    st.markdown("---")
    if user_avg > 94:
        st.error("あなたは...【 上沼恵美子 】タイプです！")
        st.write("情熱的で、高い点数をつける傾向があります！")
    elif user_avg > 90:
        st.success("あなたは...【 松本人志 】タイプです！")
        st.write("バランス感覚に優れ、標準的な評価をします。")
    else:
        st.info("あなたは...【 博多大吉 】タイプです！")
        st.write("冷静に技術を見極める、少し厳しめの採点です。")
