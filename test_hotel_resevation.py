import pytest
from playwright.sync_api import Page, expect

# Otel rezervasiya axınının yoxlanılması
def test_hotel_booking_flow(page: Page):
    # 1. Platformaya daxil oluruq
    page.goto("https://adactinhotelapp.com/")

    # 2. Login (Bu məlumatlar test üçün standartdır)
    page.fill("#username", "LalaTesting")
    page.fill("#password", "Lala12345")
    page.click("#login")

    # 3. Rezervasiya formunu doldururuq
    page.select_option("#location", "London") # Londonu seçirik
    page.select_option("#hotels", "Hotel Sunshine")
    page.select_option("#room_type", "Super Deluxe")
    page.select_option("#room_nos", "1")
    
    # Check-in və Check-out tarixlərini set edirik
    page.fill("#datepick_in", "20/05/2026")
    page.fill("#datepick_out", "25/05/2026")
    
    page.click("#Submit")

    # 4. Nəticəni yoxlayırıq
    # Seçim səhifəsinin gəldiyini "Select Hotel" yazısı ilə təsdiqləyirik
    expect(page.locator(".login_title")).to_be_visible()
    
    print("Otel axtarış ssenarisi uğurla tamamlandı! ✅")
