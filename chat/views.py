from django.shortcuts import render 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message
from django.contrib.auth.models import User

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        # Save the message to the database
        recipient_user = User.objects.get(username='nunoojusticesamuel')
        Message.objects.create(sender=request.user, content=message, recipient= recipient_user)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def get_chat_history(request):
    # Retrieve the chat history from the database
    chat_history = Message.objects.all()
    # Serialize the chat history into JSON format
    serialized_chat_history = [{'sender': msg.sender.username, 'content': msg.content} for msg in chat_history]
    return JsonResponse({'chat_history': serialized_chat_history})

def chat_page(request):
    return render(request, 'chat/chat.html')