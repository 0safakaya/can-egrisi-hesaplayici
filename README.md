# 🎓 Üniversite Çan Eğrisi (Curve) Hesaplayıcı

Bu proje, bir sınıfın vize ve final notlarını işleyerek istatistiksel çan eğrisi çıkaran ve harf notlarını hesaplayan bir veri analizi betiğidir.

## Proje Amacı ve Özellikleri
Öğrenci notlarını klasik `if-else` döngüleriyle yavaş bir şekilde hesaplamak yerine, vektörel işlemler kullanarak performansı artırmak amaçlanmıştır.

- **Pandas** ile öğrenci not verileri tablo (DataFrame) formatına çevrildi.
- **NumPy** kullanılarak sınıfın not ortalaması ve standart sapması hesaplandı.
- `np.select` metodu ile istatistiksel koşullara göre (ortalamanın ve standart sapmanın altı/üstü) harf notları (AA, BB, CC, FF) tek kalemde ve yüksek hızda atandı.

## Kullanılan Teknolojiler
- **Dil:** Python 3
- **Kütüphaneler:** Pandas, NumPy

## Nasıl Çalıştırılır?

## Projeyi kendi bilgisayarınızda çalıştırmak için öncelikle gerekli kütüphaneleri kurun:
```bash
pip install pandas numpy