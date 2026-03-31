import pytest
from playwright.sync_api import Playwright

# Rezervasiya məlumatlarının API səviyyəsində doğrulanması
def test_verify_booking_api(playwright: Playwright):
    # API üçün mühit yaradılır
    context = playwright.request.new_context(base_url="https://restful-booker.herokuapp.com")
    
    # 1 nömrəli rezervasiyanı yoxlayırıq
    response = context.get("/booking/1")
    
    # Status kodu 200 (Uğurlu) olmalıdır
    assert response.status == 200
    
    data = response.json()
    
    # Datanın içində vacib açarların (keys) olduğunu yoxlayırıq
    assert "firstname" in data
    assert "lastname" in data
    assert "totalprice" in data
    
    print("API Məlumat tamlığı testi uğurla keçdi! 🚀")
