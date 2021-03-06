import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from rest_framework import serializers


def validate_duration(value):
    if value % 15 != 0:
        raise serializers.ValidationError('only even quarters allowed, for example: 15, 45, 180, 105')


class Project(models.Model):
    name = models.CharField(max_length=128)
    billable = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "projects"

    class JSONAPIMeta:
        resource_name = "projects"

    def user_set(self):
        users = dict()

        for progress in self.progress_set.all():
            if progress.user_id not in users:
                users[progress.user_id] = [0, progress.user]
            users[progress.user_id][0] += int(progress.duration)

        most_active_users = sorted(users.items(), key=lambda x: int(x[1][0]), reverse=True)

        return [mau for id, mau in most_active_users]


class TajmUser(User):
    class Meta:
        proxy = True

    def project_set(self):
        projects = list(set([p.project_id for p in self.progress_set.all()]))
        project_set = Project.objects.filter(pk__in=projects)
        return project_set


class Deadline(models.Model):
    projects = models.ManyToManyField(Project)
    label = models.CharField(max_length=128)
    starts_at = models.DateField(null=True, blank=True)
    ends_at = models.DateField(null=True, blank=True)
    hour_amount = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)])

    class Meta:
        ordering = ["-ends_at", '-starts_at']
        verbose_name_plural = "deadlines"

    def is_billable(self):
        billable = 0
        for p in self.projects.all():
            billable += 1 if p.billable else -1
        return billable > 0


    def burndown(self):
        duration = 0
        kwargs = {}

        if self.starts_at:
            kwargs['done_at__gte'] = self.starts_at
        if self.ends_at:
            kwargs['done_at__lte'] = self.ends_at

        for p in self.projects.all():
            for d in p.progress_set.filter(**kwargs):
                duration += d.duration

        return duration

    def user_set(self):
        users = dict()
        kwargs = {}

        if self.starts_at:
            kwargs['done_at__gte'] = self.starts_at
        if self.ends_at:
            kwargs['done_at__lte'] = self.ends_at

        for p in self.projects.all():
            for progress in p.progress_set.filter(**kwargs):
                if progress.user_id not in users:
                    users[progress.user_id] = [0, progress.user]
                users[progress.user_id][0] += int(progress.duration)

        most_active_users = sorted(users.items(), key=lambda x: int(x[1][0]), reverse=True)

        return [mau for id, mau in most_active_users]


class Progress(models.Model):
    user = models.ForeignKey(TajmUser)
    duration = models.IntegerField(default=15, validators=[MinValueValidator(15), validate_duration])
    note = models.TextField()
    done_at = models.DateField(default=datetime.date.today)
    created_at = models.DateField(auto_now_add=True)
    started_at = models.TimeField(default='00:00:00')

    project = models.ForeignKey(Project)

    def __str__(self):
        return self.note

    class Meta:
        ordering = ["-done_at", 'created_at']
        verbose_name_plural = "progresses"

    class JSONAPIMeta:
        resource_name = "progresses"


class AbsenceCategory(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    class JSONAPIMeta:
        resource_name = "absence_categories"


class Absence(models.Model):
    user = models.ForeignKey(TajmUser)
    duration = models.IntegerField(default=480, validators=[MinValueValidator(15), validate_duration])
    note = models.TextField(default='', blank=True)
    done_at = models.DateField(default=datetime.date.today)
    started_at = models.TimeField(default='00:00:00')
    created_at = models.DateField(auto_now_add=True)

    category = models.ForeignKey(AbsenceCategory)

    def __str__(self):
        return self.category.name

    class Meta:
        ordering = ["-done_at"]
        verbose_name_plural = "absences"

    class JSONAPIMeta:
        resource_name = "absences"
