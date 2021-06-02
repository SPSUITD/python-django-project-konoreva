from django.shortcuts import render, redirect

from .models import PublicChat, Message
from .forms import MessageForm


def index(request):
  chats = PublicChat.objects.all() # Достаем все чаты из базы
  return render(request, 'index.html', {'chats': chats})


""" Страница чата """
def chat(request, pk):
  chat = PublicChat.objects.filter(pk=pk) # Ищем чат в базе
  if not chat.exists(): # Если чата не существует
    return redirect('index') # Редирект на главную

  chat = chat.first()
  messages = Message.objects.filter(chat=chat).order_by('created_date') # Достаем сообщения чата из базы, и фильруем по дате создания

  form = MessageForm()
  if request.method == 'POST': # Если POST запрос
    form = MessageForm(request.POST) # Заполняем форму данными
    if form.is_valid(): # Проверяем их
      msg = form.save(commit=False) 
      msg.chat = chat # Приписываем чат сообщению
      msg.save() # И сохраняем
  
  return render(request, 'chat.html', {'messages': messages, 'form': form, 'chat':chat})