from django.shortcuts import render

# post_list view
def post_list(request):
    return render(request, 'blog/post_list.html', {})