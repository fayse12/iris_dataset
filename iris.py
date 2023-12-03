import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

#eğer url den değil de localde olan bir csv dosyasından veri setini okumak isteseydik;
#file_path = "path/to/iris.csv"
#iris_data = pd.read_csv(file_path, header=None, names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

# Iris veri setini yükle
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris_data = pd.read_csv(url, header=None, names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

# Sadece özellikleri al
X = iris_data.iloc[:, :-1]

# t-SNE uygula
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)

# t-SNE sonuçlarını ve sınıf etiketlerini birleştir
tsne_df = pd.DataFrame(X_tsne, columns=["Dimension 1", "Dimension 2"])
tsne_df["class"] = iris_data["class"]

# Sonucu görselleştir
colors = {"Iris-setosa": "purple", "Iris-versicolor": "green", "Iris-virginica": "yellow"}
plt.scatter(tsne_df["Dimension 1"], tsne_df["Dimension 2"], c=tsne_df["class"].map(colors), label=tsne_df["class"])
plt.title("t-SNE Görselleştirmesi - Iris Veri Seti")

# Renk çubuğunu ekle
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Setosa', markerfacecolor='purple', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='Versicolor', markerfacecolor='green', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='Virginica', markerfacecolor='yellow', markersize=10)]

plt.legend(handles=legend_elements, title='Sınıflar')

# Grafiği göster
plt.show()
