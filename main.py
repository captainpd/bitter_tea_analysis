from fetch_news import fetch_news
from text_analysis import word_count, word_combine


if __name__ == '__main__':
    # fetch_news(save_folder=r"data/news")

    list_word_countries = ['朝鲜', '美国', '台湾', '巴西', '以色列', '乌克兰', '意大利']
    result_count = word_count(files_folder=r"data\news", list_words=list_word_countries)
    print(result_count)

    list_word_combine = ['美国', '元首']
    result_combine = word_combine(files_folder=r"data\news", list_combine=list_word_combine)
    print(f"combine count: {len(result_combine)}")
    if result_combine:
        print(result_combine)