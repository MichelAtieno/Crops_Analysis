from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
import csv 
from datetime import datetime
from crop_details.models import Crops

# Create your views here.
def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    # row = "".join(row)
                    # row = row.replace(" ", "")
                    # row = row.split()
                    print(row)
                    # print(type(row))
                    product_variety = row[0]
                    commodity_type = row[1]
                    unit = row[2]
                    volume_in_kgs = row[3]
                    values_in_ksh = row[4]
                    date = datetime.strptime(row[5], '%m/%d/%Y %H:%M')
                    Crops.objects.create(
                        product_variety = product_variety,
                        commodity_type = commodity_type,
                        unit = unit,
                        volume_in_kgs = volume_in_kgs,
                        values_in_ksh = values_in_ksh,
                        date = date
                    )       
            obj.activated = True
            obj.save()
            
    return render(request, 'csvs/upload.html', {'form': form} )

