# Django Todo Apps
# install
- ikke gjøre å sende filene til github
<br>

- .gitignore
    - benv er i gitignore
- py -m venv benv
- .\benv\Scripts\activate
- py -m pip install django

- pip freeze // det kan være sjekke
- pip freeze >.\requirement.txt    (update)

- django-admin startproject cblog (prosjektsnavn)
- py manage.py startapp blog
    - blog/urls.py dosyası oluşturduk  // url yapısını oluşturmak için
    - settings.py içine 'blog' veya 'blog.apps.BlogConfig' ekle 
- mv .\blog\ src  // üst klasördeki blog ismini src olarak değiştirdik
- py -m pip install python-decouple  // .env içine verileri koymamızı sağlıyor
- py -m pip freeze >.\requirement.txt    (update)
- settings/SECRET_KEY -> .env
    - SECRET_KEY=...
    - PYTHONPATHC:\\Users\\MittHus\\Desktop\\django_blog\\django_blog\\benv\\Scripts\\python.exe
<br>

- settings.json içine şu komutları ekle:
{
    "python.pythonPath": "django_blog\\benv\\Scripts\\python.exe",
    "python.autoComplete.extraPaths": ["C:\\Users\\MittHus\\Desktop\\django_blog\\django_blog\\benv\\Scripts\\python.exe"],
    "python.envFile": ".env"
}

<br>

- kan gjøre å sende filene til github
<br>

- py manage.py runserver
<br>

- py -m pip install pillow  // resimleri kullanmak için bunu kurmalıyız
bu üçünü de unutmayın
py -m pip freeze >.\requirement.txt
py manage.py makemigrations
py manage.py migrate
<br>

- py manage.py migrate  // Modelde değişiklik yapacaksak migrate komutunu kullanıyoruz
- py manage.py createsuperuser
- py manage.py makemigrations
- py manage.py migrate

