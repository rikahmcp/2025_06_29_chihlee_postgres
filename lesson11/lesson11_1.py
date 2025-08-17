import streamlit as st
import datasource
from datetime import datetime, date

st.sidebar.title("台鐵車站資訊")
st.sidebar.header("2023年各站進出人數")
st.subheader("進出站人數顯示區")

@st.cache_data
def get_stations():
    """取得車站資料"""
    return datasource.get_stations_names()

@st.cache_data
def get_date_range():
    """取得日期範圍"""
    return datasource.get_min_and_max_date()

stations = get_stations()
if stations is None:
    st.error("無法取得車站資料，請稍後再試。")
    st.stop()


common_stations = ['臺北','桃園','新竹','台中','臺南','高雄','其它']

choice = st.sidebar.radio("快速選擇常用車站", common_stations)

if choice == "其它":
    station = st.sidebar.selectbox(
        "請選擇車站",
        stations,
    )
else:
    station = choice

date_range = get_date_range()
if date_range is None:
    st.error("無法取得日期範圍，請稍後再試。")
    st.stop()


choose_date_range = get_date_range()
if choose_date_range is None:
    st.error("無法取得日期範圍，請稍後再試。")
    st.stop()


def _to_date(v):
  if isinstance(v, date):
    return v
  if isinstance(v, datetime):
    return v.date()
  if isinstance(v, str):
    try:
      return date.fromisoformat(v)
    except Exception:
      try:
        return datetime.strptime(v, "%Y-%m-%d").date()
      except Exception:
        return datetime.strptime(v, "%Y/%m/%d").date()
  raise ValueError("Unsupported date format")

_min_date = _to_date(choose_date_range[0])
_max_date = _to_date(choose_date_range[1])

# 在 sidebar 顯示只限於資料範圍內的日期區間選擇器
_selected = st.sidebar.date_input(
  "請選擇日期範圍",
  value=(_min_date, _max_date),
  min_value=_min_date,
  max_value=_max_date
)

if isinstance(_selected, tuple):
  start_date, end_date = _selected
else:
  start_date = end_date = _selected

# 更新 choose_date_range 變數供後續使用
choose_date_range = (start_date, end_date)


st.write("您選擇的車站:", station)
st.write("日期範圍:", date_range[0], "至", date_range[1])
st.write("您選擇的日期範圍:", choose_date_range[0], "至", choose_date_range[1])
