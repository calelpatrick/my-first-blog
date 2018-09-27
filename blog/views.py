from django.shortcuts import render
from django.utils import timezone
from .models import Habitacion
from django.shortcuts import render, get_object_or_404
from .forms import HabForm
from django.shortcuts import redirect
def hab_list(request):
	habs = Habitacion.objects.all()
	return render(request, 'blog/hab_list.html', {'habs': habs})


def hab_detail (request, pk):
	pkh=get_object_or_404(Habitacion, pk=pk)
	return render(request, 'blog/hab_detail.html',{'pkh':pkh})

def hab_new(request):
	if request.method == "POST":
		form = HabForm(request.POST)
		if form.is_valid():
			pkh = form.save(commit=False)
			pkh.save()
			return redirect('hab_detail', pk=pkh.pk)
	else:
		form = HabForm()
	return render(request, 'blog/hab_edit.html', {'form': form})
