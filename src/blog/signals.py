# Bu dosyayı linkteki kelimeler arasında - eklemek için yaptık

from django.db.models.signals import pre_save  # Host'u kaydetmeden önce slug oluştursun istiyorum. Bu yüzden bu metodu kullanıyoruz
from django.dispatch import receiver  # hosttan save e basınca receiver yazılan kodun gerçekleşmesini sağlıyor
from  django.template.defaultfilters import slugify  # slug arasındaki tireleri koyan fonksiyonu import ediyoruz
from .models import Post

@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.author.username + " " + instance.title)
        
# a = "serdar durmus"
# print(slugify(a))

# To-do
# Post model yaptığımızda belleğe eklenen resim silinmiyor, bu resmin de silinmesini sağla