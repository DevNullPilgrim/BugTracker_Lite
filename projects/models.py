from django.db import models
from django.conf import settings


class Project(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_projects',
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='ProjectMembership',
        related_name='projects',
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Neta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name


class ProjectMembership(models.Model):
    class Role(models.TextChoices):
        MANAGER = "manager", "Manager"
        DEVELOPER = "developer", "Developer"
        REPORTER = "reporter", "Reporter"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    role = models.CharField(
        max_length=16,
        choices=Role.choices,
        default=Role.DEVELOPER
    )

    class meta:
        unique_together = ('user', 'project')
        verbose_name = 'Project membership'
        verbose_name_plural = "Project memberships"

    def __str__(self):
        return f'{self.user} in {self.project} as {self.role}'
