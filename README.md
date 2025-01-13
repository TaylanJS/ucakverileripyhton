Weather Forecasting with Time Series Models
Bu proje, zaman serisi modelleme tekniklerini kullanarak hava durumu tahminleri yapmak üzerine odaklanır. Projede, çeşitli derin öğrenme modelleri ve Python tabanlı kütüphaneler kullanılmıştır.
Proje Özeti
Proje, şu çerçevede geliştirilmiştir:
Zaman serisi veri setleri ile çalışma.
Informer, Autoformer, Reformer, TFT ve NVIDIA gibi modern zaman serisi modelleme tekniklerini kullanma.
Python ve Google Colab kullanarak hava durumu tahmin modeli oluşturma.
Geliştirme Ortamı
Proje aşağıdaki ortamda geliştirilmiştir:
Programlama Dili: Python 3.8+
Ortam: Google Colab, Jupyter Notebook

Kütüphaneler:
PyTorch
TensorFlow
Scikit-learn
Matplotlib, Seaborn (görselleştirme için)
Pandas, NumPy (veri işleme için)

Projenin Yüklenmesi ve Çalıştırılması
Projeyi kendi ortamınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Depoyu Klonlayın
git clone https://github.com/TaylanJS/yazlab_havadurumu.git
cd yazlab_havadurumu

2. Gerekli Bağımlılıkları Kurun
pip install -r requirements.txt

3. Google Colab'da Notebook'u Açın
yazlab1_2proje.ipynb dosyasını Google Colab'a yükleyin.
Notebook'ı çalıştırın.

Kullanılan Modeller
Projede kullanılan temel zaman serisi modelleri:
Informer: Uzun sekans tahmini için optimize edilmiştir.
Autoformer: Otomatik özellik öğrenimi ile tahmin yapar.
Reformer: Daha hızlı ve verimli bir Transformer modeli.
TFT (Temporal Fusion Transformer): Zaman serilerinde geleceği tahmin etmek için çoklu kaynakları birleştirir.
NVIDIA: Hızlı hesaplamalar için GPU destekli modeller.
Arayüz Örneği

Autoformer
![epochloss](https://github.com/user-attachments/assets/a6baf01d-7b8d-40ba-9730-983eaa6c584a)
![TAHMİN](https://github.com/user-attachments/assets/708f54d3-005d-4d01-a283-35bce6ad5abc)

INFORMER
![epochloss](https://github.com/user-attachments/assets/3eae9be9-b7ef-4421-b0d2-e358750c0f73)
![tahmin](https://github.com/user-attachments/assets/d4db4f3d-62dd-4923-843d-1fae0c401e7b)


TFT(NVIDIA)
![kayip](https://github.com/user-attachments/assets/337f1325-deb8-4cac-b70c-425642bd56cb)
![hatadagilimi](https://github.com/user-attachments/assets/9781dd62-0f9a-4f2a-8764-8e1833242038)
![epoch-loss](https://github.com/user-attachments/assets/06fdacb7-c04a-4f5f-9cf6-609306065da2)
![el](https://github.com/user-attachments/assets/73d347bd-4223-4f94-8981-207548d2b8fe)
![tahmingercek](https://github.com/user-attachments/assets/f60829a8-eb19-4902-8bd4-73ba9f970ac4)

Taylan Doğan
Umar Muskiev
