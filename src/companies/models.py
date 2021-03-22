from django.db import models

from model_utils.models import TimeStampedModel, StatusModel
import uuid
from model_utils import Choices


class Company(StatusModel, TimeStampedModel):
    STATUS = Choices(("unverified", "Non vérifiée"), ("verified", "Vérifiée"))
    uuid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False, primary_key=True
    )
    td_id = models.CharField("Identifiant Trackdechets", max_length=64)
    siret = models.CharField("Siret", max_length=20)
    name = models.CharField("Nom", max_length=256)
    info = models.TextField("Info", blank=True)

    class Meta:
        verbose_name = "Entreprise"
        verbose_name_plural = "Entreprises"
        ordering = ("status", "created",)
