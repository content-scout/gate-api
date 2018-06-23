# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import reverse, get_object_or_404

from reviews.models import Movie


def search(request):
    resp = {
        'data': [],
        'status': 'OK',
        'error': None
    }

    name = request.GET.get('name')

    if not name:
        resp['error'] = 'No name parameter specified'
        resp['status'] = 'ERROR'
        return JsonResponse(resp, status=400)

    results = Movie.objects.filter(title__icontains=name)

    if not results.exists():
        resp['status'] = 'NO RESULTS FOUND'
        return JsonResponse(resp)

    else:
        for result in results:
            content_path = reverse('content', kwargs={'movie_id': result.id})
            resp['data'].append({
                'title': result.title,
                'url': request.build_absolute_uri(content_path)
            })
        return JsonResponse(resp)


def content(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    strobe_avg = movie.review_set.aggregate(Avg('strobe_level')).values()[0]
    sound_avg = movie.review_set.aggregate(Avg('sound_level')).values()[0]
    rating_avg = movie.review_set.aggregate(Avg('rating')).values()[0]

    resp = {
        'title': movie.title,
        'description': movie.description,
        'strobe_average': strobe_avg,
        'sound_avg': sound_avg,
        'rating_avg': rating_avg,
        'reviews': []
    }

    for review in movie.review_set.all():
        user_review = {
            'strobe_level': review.strobe_level,
            'sound_level': review.sound_level,
            'rating': review.rating,
            'review': review.review
        }
        resp['reviews'].append(user_review)

        return JsonResponse(resp)
