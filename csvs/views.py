from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .forms import CsvModelForm
from .models import Csv
import csv, ast 
from datetime import datetime
from crop_details.models import Commodity_Type, Product_Variety

# Create your views here.

def index(request):
    latest = Commodity_Type.objects.order_by('-date')
    variety = get_variety()
    all_varieties = Product_Variety.objects.all()
    crops = Commodity_Type.objects.all()

    context =  {
        'crops': crops,
        'latest': latest,
        'variety': variety,
        'all_varieties': all_varieties,
        }

    return render(request, 'csvs/home.html',context)


def get_variety():
    queryset = Commodity_Type.objects.values('product_variety__variety')
    return queryset


def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                # try: 
                    if i==0:
                        pass
                    else:
                        # row = "".join(row)
                        # row = row.replace(" ", "")
                        # row = row.split()
                        # print(row)
                        # # print(type(row))
                        commodity = row[1]
                        unit = row[2]
                        volume_in_kgs = row[3]
                        values_in_ksh = row[4]
                        date = datetime.strptime(row[5], '%m/%d/%Y %H:%M')
                        instance = Commodity_Type.objects.create(
                            # product_variety = product_variety,
                            commodity = commodity,
                            unit = unit,
                            volume_in_kgs = volume_in_kgs,
                            values_in_ksh = values_in_ksh,
                            date = date
                        )
                        instance.save()
                        product_variety = Product_Variety.objects.filter(variety=row[0])
                        for var in product_variety:
                            instance.product_variety.add(var)
                            
                        print(instance)
                #         crops, _ = Crops.objects.get_or_create(
                #             commodity_type = row[1],
                #             unit = row[2],
                #             volume_in_kgs = row[3],
                #             values_in_ksh = row[4],
                #             date = datetime.strptime(row[5], '%m/%d/%Y %H:%M'),
                #         )
                #         varieties_str = row[0]
                #         variety_names = ast.literal_eval(varieties_str)
                #         variety_names = map(str.lower, variety_names)
                #         variety_names = list(set(variety_names))
                #         for variety_name in variety_names:
                #             var, _ = Product_Variety.objects.get_or_create(variety=variety_name)
                #             crops.product_variety.add(var)
                # except Exception as e:
                #     print(e)
            obj.activated = True
            obj.save()

    context =  {
        'form': form,
        }
            
    return render(request, 'csvs/upload.html',context)

def variety_profile(request, id):
    one_variety = get_object_or_404(Product_Variety, id=id)
    var_queryset = Commodity_Type.objects.all()
    var_query = one_variety.variety
    var_queryset = var_queryset.filter(Q(product_variety__variety__icontains=var_query)).distinct()
    
    context = {
        'one_variety': one_variety,
        'queryset': var_queryset,
    }

    return render(request, "csvs/variety_profile.html", context)
