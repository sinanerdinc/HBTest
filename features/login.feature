Feature: Üye girişi ile ilgili testler

  Scenario: Kullanıcı başarıyla giriş yapar.
    Given   Anasayfaya gittiğimde
    When    Üye girişi yaptığımda
    Then    Başarıyla giriş yaptığımı görmeliyim.

  Scenario: Kullanıcı sitede arama yapar, ilk ürüne girer ve minumum 2 satıcı olduğunu doğrular.
    When    Sitede "drone" araması yaptığımda
    When    Sonuçlar içerisinden ilk ürüne tıkladığımda
    Then    En az "2" adet satıcı görmeliyim.

  Scenario: Farklı tedarikçilerden ürünü sepete atmak.
    Given   Sayfada "1." sıradaki tedarikçiden ürünü sepete atarsam
    When    Alışverişe devam et butonuna tıkladığımda
    Given   Sayfada "2." sıradaki tedarikçiden ürünü sepete atarsam
    Then    Sepette "2" ürün olduğunu görmeliyim.
    Then    Ekran görüntüsü almalıyım.
