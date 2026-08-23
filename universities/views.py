# from django.shortcuts import render

# # Create your views here.
############################################################

from django.shortcuts import render, get_object_or_404
import django_filters
from .models import University, Country

class UniversityFilter(django_filters.FilterSet):
    country = django_filters.ModelChoiceFilter(queryset=Country.objects.all())
    max_tuition = django_filters.NumberFilter(field_name="tuition_from_usd", lookup_expr="lte")

    class Meta:
        model = University
        fields = ["country", "max_tuition"]

def directory(request):
    qs = University.objects.select_related("country")
    f = UniversityFilter(request.GET, queryset=qs)
    return render(request, "universities/directory.html", {"filter": f, "countries": Country.objects.all()})

def university_detail(request, slug):
    uni = get_object_or_404(University, slug=slug)
    return render(request, "universities/detail.html", {"university": uni})