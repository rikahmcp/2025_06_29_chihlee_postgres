import streamlit as st
import datasource

st.sidebar.title("台鐵車站資訊")
st.sidebar.header("2023年各站進出人數")
st.subheader("進出站人數顯示區")

@st.cache_resource
def get_stations():
    """取得車站資料"""
    return datasource.get_stations_names()

stations = get_stations()
if stations is None:
    st.error("無法取得車站資料，請檢查資料庫連線設定。")
    st.stop()


#sidebar要先顯示常用的車站名稱
#使用者可以很快的選擇
#如果不常用的車站名稱,再使用selectbox

# 先取前五個站為常用站（可改為固定清單或從使用者設定讀取）
common_stations = stations[:5] if len(stations) >= 5 else stations

# 在 sidebar 顯示常用站列表，並加上「其他」選項（當總站數大於常用站數時）, pass a unique key argument to the selectbox element.
if len(stations) > len(common_stations):
    common_stations.append("其他")
st.sidebar.header("常用車站")
selected_common_station = st.sidebar.selectbox(
    "請選擇車站",
    common_stations,
    key="common_stations"
)
#如果使用者選擇了「其他」，則顯示完整的車站列表, pass a unique key argument to the selectbox element.
if selected_common_station == "其他":
    station = st.sidebar.selectbox(
        "請選擇車站",
        stations,
        key="selected_all_stations"
    )
else:
    station = selected_common_station

st.write("您選擇的車站:", station)
