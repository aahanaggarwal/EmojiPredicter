#%%
import pandas as pd

data = pd.read_csv('final_clean.vec', sep=' ', index_col=False)

print(data.head())

#%%

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd

prop = FontProperties(fname='EmojiOneColor-SVGinOT.ttf')

plt.rcParams['font.family'] = prop.get_family()

# filter data to only include the rows where the word column contains the word 'love'
emoji_data = data[data['word'].str.contains(':') == True].head(100)
# data = data[data['word'].str.contains(':')]

# increase font size
plt.rcParams['font.size'] = 30

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(x=emoji_data['x'], y=emoji_data['y'])

word_to_emoji = {
    ':smiling_face_with_heart_eyes:': '😍',
    ':face_with_tears_of_joy:': '😂',
    ':red_heart:': '❤️',
    ':loudly_crying_face:': '😭',
    ':smiling_face_with_heart-eyes:': '😍',
    # ':fire:': '🔥',
    # ':folded_hands:': '🙏',
    ':weary_face:': '😩',
    # ':person_shrugging:': '🤷',
    # ':two_hearts:': '💕',
    # ':sparkles:': '✨',
}

for index, row in emoji_data.head(10).iterrows():
    if row['word'] in [':folded_hands:',':fire:', ':person_shrugging:', ':two_hearts:', ':sparkles:']:
        continue
    ax.annotate(word_to_emoji[row['word']], (row['x'], row['y']))

plt.title('Emoji Word Cloud')
plt.show()

# %%
