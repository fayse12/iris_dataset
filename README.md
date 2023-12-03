# iris_dataset

# Sadece özellikleri al::

-1 ifadesi, sütunları seçerken sonuncu sütunu (class sütunu) hariç alır. Yani, :-1 ifadesi tüm satırları ve class sütunu hariç tüm özellik sütunlarını seçer. Yani, X değişkeni sadece özellikleri içerir ve class sütunu bu alt kümede bulunmaz.
Bu satır, iloc fonksiyonu ile tüm satırları ve son sütunu hariç diğer sütunları seçer. :-1 ifadesi, bu seçimi yaparken son sütunu hariç alır. Bu nedenle, X değişkeni sepal_length, sepal_width, petal_length, ve petal_width özelliklerini içeren bir DataFrame'i temsil eder ve class sütunu bu alt kümede yer almaz.

-----------------------------

# t-SNE uygula::

t-SNE (t-distributed stochastic neighbor embedding) algoritması uygulanıyor. 
TSNE: t-SNE'nin scikit-learn kütüphanesindeki implementasyonunu temsil eden sınıf.
n_components=2: İndirgenmiş boyut sayısını ifade eder. Bu durumda, t-SNE tarafından oluşturulan görselleştirmenin iki boyutlu olmasını sağlar. Yani, her örnek artık iki boyutlu bir vektörle temsil edilecek.
random_state=42: Bu parametre, t-SNE'nin stokastik doğası nedeniyle işlemin yeniden üretilebilir olmasını sağlar. Yani, aynı parametrelerle tekrar çalıştığınızda aynı sonuçları alırsınız. random_state parametresinin değeri burada herhangi bir sayı olabilir, ancak genellikle kullanıcılar aynı sonuçları elde etmek için belirli bir sayı kullanmayı tercih eder.
fit_transform(X): t-SNE'yi öğrenme ve dönüştürme işlemlerini bir arada gerçekleştirir. Bu metodun parametresi olarak, indirgenmiş boyutlu veri setini elde etmek istediğimiz orijinal veri setini (X) kullanırız. X_tsne değişkeni, t-SNE uygulanmış veri setini temsil eder.

-----------------------------

# t-SNE sonuçlarını ve sınıf etiketlerini birleştir::

Bu adımda, t-SNE'nin temelini oluşturan matematiksel işlemler gerçekleştirilir ve orijinal veri seti, indirgenmiş iki boyutlu uzayda temsil edilir. X_tsne değişkeni, her bir örneği iki boyutlu bir uzayda temsil eden bir matrisi içerir. Bu indirgenmiş boyutlu veri seti, genellikle daha kolay anlaşılabilir ve görselleştirilebilir.

-----------------------------

# Sonucu görselleştir::

Bu Python kodu, matplotlib kütüphanesini kullanarak t-SNE (t-Distributed Stochastic Neighbor Embedding) algoritması sonucunu görselleştirmektedir. İlk olarak, colors adında bir sözlük oluşturulmuştur. Bu sözlük, "Iris-setosa", "Iris-versicolor" ve "Iris-virginica" sınıflarını temsil eden çiçek türlerine ait renkleri içermektedir. Örneğin, "Iris-setosa" sınıfı mor renkle, "Iris-versicolor" sınıfı yeşil renkle ve "Iris-virginica" sınıfı sarı renkle gösterilecektir.
Ardından, plt.scatter() fonksiyonu kullanılarak t-SNE sonuçları görselleştirilmektedir. tsne_df adındaki veri çerçevesi üzerindeki "Dimension 1" ve "Dimension 2" sütunları, t-SNE'nin iki boyutlu gömme uzayındaki koordinatları temsil etmektedir. c parametresi ile renklendirme işlemi gerçekleştirilmiştir. Burada, tsne_df["class"].map(colors) ifadesi, her sınıfa ait rengin belirlenmesini sağlar.
title: Grafiğin başlığını belirler.
show: Grafiği ekranda gösterir.
