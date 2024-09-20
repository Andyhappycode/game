from wordcloud import WordCloud
import matplotlib.pyplot as plt

while True:
    # 准备一段文本
    text = input("请输入文本：")

    # 生成词云图
    wordcloud = WordCloud(background_color="white", width=800, height=400, random_state=1).generate(text)

    # 显示词云图
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()