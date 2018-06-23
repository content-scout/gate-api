# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    description = models.TextField(null=True)


class Review(models.Model):
    NO_VALUE = 1
    LOW_VALUE = 2
    MED_VALUE = 3
    HIGH_VALUE = 4
    EXTREME_VALUE = 5

    STROBE_OPTIONS = (
        (NO_VALUE, 'No Strobe'),
        (LOW_VALUE, 'Low Strobe'),
        (MED_VALUE, 'Medium Strobe'),
        (HIGH_VALUE, 'High Strobe'),
        (EXTREME_VALUE, 'Extreme Strobe')
    )

    SOUND_OPTIONS = (
        (NO_VALUE, 'No Lound Sounds'),
        (LOW_VALUE, 'Occasioanl Lound Sounds'),
        (MED_VALUE, 'Some Lound Sounds'),
        (HIGH_VALUE, 'Many Lound Sounds'),
        (EXTREME_VALUE, 'Extremely Lound Sounds'),
    )

    RATING_OPTIONS = (
        (NO_VALUE, 'No Problem'),
        (LOW_VALUE, 'Little Problem'),
        (MED_VALUE, 'Medium Problem'),
        (HIGH_VALUE, 'Big Problem'),
        (EXTREME_VALUE, 'Extreme Problem')
    )

    strobe_level = models.IntegerField(choices=STROBE_OPTIONS)
    sound_level = models.IntegerField(choices=SOUND_OPTIONS)
    rating = models.IntegerField(choices=RATING_OPTIONS)
    review = models.TextField()

    movie = models.ForeignKey(Movie)
