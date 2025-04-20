# %%
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# %%
def generate_wordcloud(keywords):
    if not keywords:
        print("[⚠️] No keywords to visualize.")
        return
    
    text_blob = " ".join(keywords)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_blob)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Keyword Cloud", fontsize=16)
    plt.tight_layout(pad=0)
    plt.show()    

# %%



