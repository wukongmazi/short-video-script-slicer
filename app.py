"""
短视频脚本切片机 · Gradio 部署入口（可选）
适用场景：当魔搭创空间仅提供 Gradio/Streamlit SDK 时，用本文件作为入口，
将同目录的 index.html 以 iframe 形式展示。静态脚本在独立文档中运行，不受 gr.HTML 清洗影响。
"""
import gradio as gr
from fastapi.responses import HTMLResponse

with gr.Blocks(title="短视频脚本切片机") as demo:
    gr.HTML(
        '<iframe src="/slicer_app" '
        'style="width:100%;height:1600px;border:0;min-height:1600px" '
        'sandbox="allow-scripts allow-same-origin"></iframe>'
    )


@demo.app.get("/slicer_app")
def serve_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


if __name__ == "__main__":
    demo.launch()
