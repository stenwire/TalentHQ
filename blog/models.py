from django.db import models
from django.template.defaultfilters import slugify
from django.urls.base import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from authme.models import CustomUser
from utils.models import TrackObjectStateMixin


class BlogPost(TrackObjectStateMixin):
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Author"
    )
    title = models.CharField(max_length=120, verbose_name="Title")
    content = models.TextField(_("Content"))
    published_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True
    )
    slug = models.SlugField(blank=True, max_length=127, editable=False)

    OWNER_FIELD = "author"

    class Meta:
        ordering = ("-published_date",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "blog:read-update-delete-article-view",
            kwargs={"pk": self.id},
        )
