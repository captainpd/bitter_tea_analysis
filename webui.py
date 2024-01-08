import gradio as gr
from fetch_news import fetch_news
from text_analysis import word_combine, word_count

with gr.Blocks() as demo:
    with gr.Tab(label="下载数据"):
        button_download = gr.Button(value="下载数据")
        text_download_path = gr.Text(value=r"data\news")
        button_download.click(fetch_news, inputs=[text_download_path])

    with gr.Tab(label="同时出现统计"):
        str_repeat_words = ",".join(['美国', '元首'])

        text_combine = gr.Text(label="同时出现词汇", value=str_repeat_words)
        button_combine = gr.Button(value="搜索同时出现词汇")
        json_result_combine = gr.Json(label="统计结果")
        button_combine.click(word_combine, inputs=[text_download_path, text_combine], outputs=[json_result_combine])

    with gr.Tab(label="关键词次数统计"):
        str_repeat_words = ",".join(['朝鲜', '美国', '台湾', '巴西', '以色列', '乌克兰', '意大利'])

        text_repeat = gr.Text(label="统计词汇", value=str_repeat_words)
        button_repeat = gr.Button(value="搜索重复词汇")
        json_result = gr.Json(label="统计结果")

        button_repeat.click(word_count, inputs=[text_download_path, text_repeat], outputs=[json_result])


if __name__ == '__main__':
    demo.launch(debug=True, inbrowser=True)