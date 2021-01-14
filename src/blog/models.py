from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),  # 1.si database kaydedilmesi, 2.si kullanıcıya gözükme şekli
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)  # Protect tablonun silinmesine izin vermiyr, eğer bunu iin verirsek (CASCADE ile) tm post gidiyor
    publish_date = models.DateTimeField(auto_now_add=True)  # save ettiğimizde otomatik olarak datebase tarih ve saati koyuyuor
    last_updated = models.DateTimeField(auto_now=True)  # her update edildiğinde Time ı değiştiriyor
    # ForeignKey: Bir postun bir kategorisi olacak ama bir kategorinin birden fazla postu olabilir)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)  # Blank zorunlu değil demek