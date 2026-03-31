# 🏨 Travel Booking - Automation Framework (Python)

### 📋 Layihə Haqqında
Bu layihə otel rezervasiya sistemlərinin həm istifadəçi interfeysi (UI), həm də daxili sistemlərinin (API) avtomatlaşdırılmış testlərini əhatə edir. Standart e-ticarət testlərindən fərqli olaraq, burada kompleks forma validasiyaları, tarix seçimi və REST API məlumat tamlığı yoxlanılır.

### 🛠️ Texnoloji Stack
- **Language:** Python 3.x
- **Framework:** Playwright (Python)
- **Test Runner:** Pytest

### 🔍 Test Ssenariləri

#### 1. UI Testing (test_hotel_reservation.py)
- **Platforma:** Adactin Hotel App
- **Ssenari:** Sistemə daxil olmaq (Login), yerləşmə yeri və otel növü seçmək, tarixlərin daxil edilməsi və rezervasiya formunun doğrulanması.

#### 2. API Testing (test_booking_api_validation.py)
- **Platforma:** Restful-Booker API
- **Ssenari:** Rezervasiya məlumatlarının GET sorğusu ilə çağırılması, status kodun (200 OK) və JSON strukturunun yoxlanılması.

### 🚀 Quraşdırma və İşə Salma
```bash
pip install playwright pytest
playwright install
pytest
