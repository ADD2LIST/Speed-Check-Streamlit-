import streamlit as st
import speedtest
from pyecharts import options as opts
from pyecharts.charts import Gauge


def run_speed_test():
    st.write("Running speed test...")
    speedtester = speedtest.Speedtest()
    download_speed = speedtester.download() / 1000000
    upload_speed = speedtester.upload() / 1000000

    gauge = (
        Gauge()
        .add("", [("Download Speed", download_speed)], min_=0, max_=1000)
        .add("", [("Upload Speed", upload_speed)], min_=0, max_=100)
        .set_global_opts(title_opts=opts.TitleOpts(title="Speed Test"))
    )

    st_pyecharts(gauge)

    st.write(f"Download Speed: {download_speed:.2f} Mbps")
    st.write(f"Upload Speed: {upload_speed:.2f} Mbps")


def main():
    st.title("Upload and Download Speed Test")

    st.write("Click the button below to run the speed test:")

    if st.button("Run Speed Test"):
        run_speed_test()


if __name__ == "__main__":
    main()
  
