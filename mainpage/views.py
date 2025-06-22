# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Article

@csrf_exempt  # Для простоты; лучше использовать CSRF токен в реальных проектах
def update_article(request, article_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            content = data.get('content')

            article = Article.objects.get(id=article_id)
            if title:
                article.title = title
            if content:
                article.content = content
            article.save()

            return JsonResponse({
                'status': 'success',
                'article': {
                    'id': article.id,
                    'title': article.title,
                    'content': article.content,
                }
            })
        except Article.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Article not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)