from django.shortcuts import render
def post_main(request):
    return render(request, 'game/main.html', {})

def post_explain(request):
    return render(request, 'game/explain.html', {})
def post_game(request):
    return render(request, 'game/game.html', {})
# Create your views here.
