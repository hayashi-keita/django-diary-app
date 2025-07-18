from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import PageForm
from datetime import datetime
from zoneinfo import ZoneInfo
from .models import Page

class IndexVeiw(LoginRequiredMixin, View):
    def get(self, request):
        datetime_now = datetime.now(
            ZoneInfo('Asia/Tokyo')
            ).strftime('%Y年%m月%d %H:%M:%S')
        return render(request, 'diary/index.html', {'datetime_now': datetime_now})

class PageCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PageForm()
        return render(request, 'diary/page_form.html', {'form': form})

    def post(self, request):
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)
            page.user = request.user
            page.save()
            return redirect('diary:index')
        return render(request, 'diary/page_form.html', {'form': form})

class PageListView(LoginRequiredMixin, View):
    def get(self, request):
        page_list = Page.objects.order_by('-page_date')
        return render(request, 'diary/page_list.html', {'page_list': page_list})

class MypageListView(LoginRequiredMixin, View):
    def get(self, request):
        page_list = Page.objects.filter(user=request.user).order_by('-page_date')
        return render(request, 'diary/mypage_list.html', {'page_list': page_list})

class PageDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, 'diary/page_detail.html', {'page': page})

class PageUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        if page.user != request.user:
            return redirect('diary:page_list')
        form = PageForm(instance=page)
        return render(request, 'diary/page_update.html', {'form': form})
    
    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        if page.user != request.user:
            return redirect('diary:page_list')
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect('diary:page_detail', id=id)
        return render(request, 'diary/page_form.html', {'form': form})

class PageDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        if page.user != request.user:
            return redirect('diary:page_list')
        return render(request, 'diary/page_delete.html', {'page': page})
    
    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        if page.user != request.user:
            return redirect('diary:page_list')
        page.delete()
        return redirect('diary:page_list')
