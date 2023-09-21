# Streamlitライブラリをインポート
import streamlit as st

import ramdom

# タイトルを設定
st.title('おみくじアプリ')

if st.button("おみくじを引く"):
    result=["大吉","中吉","小吉","吉","凶","大凶"]
    result=ramdom.choice(results)
    st.write(f"結果：{result}")


