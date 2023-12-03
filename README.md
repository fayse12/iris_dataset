# iris_dataset

-1 ifadesi, sütunları seçerken sonuncu sütunu (class sütunu) hariç alır. Yani, :-1 ifadesi tüm satırları ve class sütunu hariç tüm özellik sütunlarını seçer. Yani, X değişkeni sadece özellikleri içerir ve class sütunu bu alt kümede bulunmaz.
Bu satır, iloc fonksiyonu ile tüm satırları ve son sütunu hariç diğer sütunları seçer. :-1 ifadesi, bu seçimi yaparken son sütunu hariç alır. Bu nedenle, X değişkeni sepal_length, sepal_width, petal_length, ve petal_width özelliklerini içeren bir DataFrame'i temsil eder ve class sütunu bu alt kümede yer almaz.

Adım 5'deki bu satırda, t-SNE (t-distributed stochastic neighbor embedding) algoritması uygulanıyor. 

TSNE: t-SNE'nin scikit-learn kütüphanesindeki implementasyonunu temsil eden sınıf.

n_components=2: İndirgenmiş boyut sayısını ifade eder. Bu durumda, t-SNE tarafından oluşturulan görselleştirmenin iki boyutlu olmasını sağlar. Yani, her örnek artık iki boyutlu bir vektörle temsil edilecek.

random_state=42: Bu parametre, t-SNE'nin stokastik doğası nedeniyle işlemin yeniden üretilebilir olmasını sağlar. Yani, aynı parametrelerle tekrar çalıştığınızda aynı sonuçları alırsınız. random_state parametresinin değeri burada herhangi bir sayı olabilir, ancak genellikle kullanıcılar aynı sonuçları elde etmek için belirli bir sayı kullanmayı tercih eder.

fit_transform(X): t-SNE'yi öğrenme ve dönüştürme işlemlerini bir arada gerçekleştirir. Bu metodun parametresi olarak, indirgenmiş boyutlu veri setini elde etmek istediğimiz orijinal veri setini (X) kullanırız. X_tsne değişkeni, t-SNE uygulanmış veri setini temsil eder.

Bu adımda, t-SNE'nin temelini oluşturan matematiksel işlemler gerçekleştirilir ve orijinal veri seti, indirgenmiş iki boyutlu uzayda temsil edilir. X_tsne değişkeni, her bir örneği iki boyutlu bir uzayda temsil eden bir matrisi içerir. Bu indirgenmiş boyutlu veri seti, genellikle daha kolay anlaşılabilir ve görselleştirilebilir.

scatter: Bu metod, bir saçılma (scatter) grafiği oluşturur. İlk iki parametre, x ve y eksenlerindeki konumları belirtir. X_tsne[:, 0] ifadesi x eksenindeki değerleri, X_tsne[:, 1] ifadesi ise y eksenindeki değerleri temsil eder.

c: Renkleri belirlemek için kullanılır. Burada iris_data["class"].astype("category").cat.codes ifadesi, "class" sütunundaki kategori değerlerini sayısal kodlara dönüştürür. Bu sayısal kodlar renkleri temsil eder.

cmap: Renk haritasını belirler. "viridis" burada kullanılan renk haritasıdır, ancak başka renk haritaları da kullanılabilir.

title: Grafiğin başlığını belirler.

show: Grafiği ekranda gösterir.

Bu satır, t-SNE tarafından indirgenmiş iki boyutlu veriyi renkli bir saçılma grafiği olarak görselleştirir. Her bir nokta bir Iris çiçeği örneğini temsil eder ve renk, çiçeğin sınıfını (setosa, versicolor, veya virginica) gösterir.
