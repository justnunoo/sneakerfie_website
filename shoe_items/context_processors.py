from .models import UserProfile

def cart_item_count(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        return {'cart_item_count': user_profile.cart_count}
    return {'cart_item_count': 0}