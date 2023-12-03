import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Iris veri setini yükle
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris_data = pd.read_csv(url, header=None, names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

# Sadece özellikleri al
X = iris_data.iloc[:, :-1]

# t-SNE uygula
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)

# Sonucu görselleştir
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=iris_data["class"].astype("category").cat.codes, cmap="viridis")
plt.title("t-SNE Görselleştirmesi - Iris Veri Seti")
plt.show()   
