import streamlit as st
import requests

# 添加 CSS 样式表
st.markdown(
    """
    <style>
    .sidebar-content .sidebar-section h1 {
                text-align: center;
            }
    .stButton button {
        width: 100%;
        height: 50px;
        font-weight: border;
        color: white;
        background-color: rgba(65,105,225,0.8)
    }
     .stButton button:hover {
        border-color: white;
    }

    [data-testid="stSidebar"][aria-expanded="true"] {
        background-color: rgba(70,130,180,0.6);
    }

    [data-testid="stAppViewContainer"] {
        background: url("https://s2.loli.net/2023/03/08/Yws5czXmraRS3uQ.jpg");
        background-size: cover;
    } 
    </style>
    """,
    unsafe_allow_html=True,
)

logo_url = "https://s2.loli.net/2023/03/08/LRV6NGHzsT14quw.png"
response = requests.get(logo_url)
logo = response.content

# 定义侧边栏

st.sidebar.image(logo, use_column_width=True)

# 这里不知道怎么居中，以下代码无效：
# .sidebar-content .sidebar-section h1 {
#                text-align: center;
#            }

blank = "&nbsp;" * 15
st.sidebar.title(blank + "健康管理平台")
st.sidebar.markdown("---")

if st.sidebar.button("**首页**"):
    # 处理跳转到首页的逻辑
    st.write("欢迎访问健康管理平台！")
if st.sidebar.button("**II型糖尿病**"):
    # 处理跳转到 II 型糖尿病页面的逻辑
    st.write("这里是 II 型糖尿病页面。")
if st.sidebar.button("**膳食指导平台**"):
    # 处理跳转到膳食指导平台的逻辑
    st.write("这里是膳食指导平台页面。")
if st.sidebar.button("**特医配方平台**"):
    # 处理跳转到特医配方平台的逻辑
    st.write("这里是特医配方平台页面。")
if st.sidebar.button("**机器学习实现**"):
    # 处理跳转到机器学习实现页面的逻辑
    st.write("这里是机器学习实现页面。")
if st.sidebar.button("**关于我们**"):
    # 处理跳转到关于我们页面的逻辑
    st.write("这里是关于我们页面。")

st.sidebar.markdown("---")
st.sidebar.markdown("**联系电话**：114514")
st.sidebar.markdown("**地址**：XX省XX市XX区XX街道XX号")

# git push test