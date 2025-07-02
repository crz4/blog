from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

@login_required
def subscribe(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    Subscription.objects.get_or_create(subscriber=request.user, subscribed_to=target_user)
    return redirect('some_view')

@login_required
def unsubscribe(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    Subscription.objects.filter(subscriber=request.user, subscribed_to=target_user).delete()
    return redirect('some_view')