Feature: Üye girişi yapmadan ilerleyen testler

  Scenario: Kullanıcı girişi yapmadan belirtilen bir ürünü sepete ekleme.
    Given   Sitede "uzaktan_kumanda" kategorisine gidersem
    When    Sonuçlar içerisinden ilk ürüne tıkladığımda
    When    Ürün detayındaki sepete ekle butonuna tıkladığımda
    Then    Sepette "1" ürün olduğunu görmeliyim.
    Then    Sayfada "Sepetinizi kaydetmek için giriş yapın." metnini görmeliyim.
