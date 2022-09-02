from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Result
from participants.models import Participant
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Register your models here.
class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class ResultAdmin(admin.ModelAdmin):
    list_display = ("participant_number", "sample_number")

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == 'POST':
            csv_file = request.FILES['csv_upload']

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded.')
                return HttpResponseRedirect(request.path_info)

            csv_file.readline() #skips header row in csv file
            file_data = csv_file.read().decode('utf-8')
            csv_data = file_data.split('\n')
            

            for rows in csv_data:
                if rows:
                    fields = rows.split(',')
                    created = Result.objects.update_or_create(
                        sample_number = fields[0],
                        sample_label = fields[1],
                        na = fields[2],
                        mg = fields[4],
                        al = fields[6],
                        si = fields[8],
                        p = fields[10],
                        s = fields[12],
                        cl = fields[14],
                        k = fields[16],
                        ca = fields[18],
                        ti = fields[20],
                        v = fields[22],
                        cr = fields[24],
                        mn = fields[26],
                        fe = fields[28],
                        co = fields[30],
                        ni = fields[32],
                        cu = fields[34],
                        zn = fields[36],
                        ga = fields[38],
                        ge = fields[40],
                        As = fields[42],
                        se = fields[44],
                        br = fields[46],
                        rb = fields[48],
                        sr = fields[50],
                        y = fields[52],
                        nb = fields[54],
                        mo = fields[56],
                        ru = fields[58],
                        rh = fields[60],
                        pd = fields[62],
                        ag = fields[64],
                        cd = fields[66],
                        In = fields[68],
                        sn = fields[70],
                        sb = fields[72],
                        te = fields[74],
                        i = fields[76],
                        cs = fields[78],
                        ba = fields[80],
                        la = fields[82],
                        ce = fields[84],
                        pr = fields[86],
                        nd = fields[88],
                        hf = fields[90],
                        ta = fields[92],
                        w = fields[94],
                        pt = fields[96],
                        au = fields[98],
                        hg = fields[100],
                        tl = fields[102],
                        pb = fields[104],
                        bi = fields[106],
                        th = fields[108],
                        u = fields[110],
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {'form': form}
        return render(request, 'admin/csv_upload.html', data)

admin.site.register(Result, ResultAdmin)