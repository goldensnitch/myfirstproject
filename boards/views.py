from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect

from .models import Board, Topic, Post, Associate, Dependant, Client
from django.utils import timezone
from .forms import NewTopicForm, NewAssociateForm, AssociateDetailsForm
from .forms import PersonalInfoForm, ContactInfoForm, IDProofInfoForm, DependantInfoForm
from .forms import NewClientForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import csv
import xlwt

from myproject.utils import render_to_pdf
from django.views.generic import View
from django import template
from django.template.loader import get_template

from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from django.template import Context

#for passing query arguments
from django.db.models import Q

#decorating views for authentication, login_required for fbv and LoginRequiredMixin for gcbv
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
        boards = Board.objects.all()
        return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
        board = get_object_or_404 (Board, pk=pk)
        return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})







@login_required
def aarya(request):
    return render(request, 'aarya.html')


@login_required
def associate(request):
    associates_list = Associate.objects.all().order_by('First_Name','Last_Name')

    query = request.GET.get('q')
    if query:
        associates_list = Associate.objects.filter( Q(First_Name__icontains=query) | Q(Last_Name__icontains=query))

    page = request.GET.get('page', 1)
    paginator = Paginator(associates_list, 4)
    try:
        associates = paginator.page(page)
    except PageNotAnInteger:
        associates = paginator.page(1)
    except EmptyPage:
        associates = paginator.page(paginator.num_pages)
    return render(request, 'associate.html', {'associates': associates})


@login_required
def associate_new(request):
        form = NewAssociateForm()
        user = User.objects.first()
        if request.method == 'POST':
            form = NewAssociateForm(request.POST)
            if form.is_valid():
                Associate = form.save(commit=False)
                Associate.created_by  = user
                Associate.updated_by = user
                Associate.created_at = timezone.now()
                Associate.updated_at = timezone.now()
                Associate.save()

                return redirect('associate')
        else:
            form = NewAssociateForm()
        return render(request, 'associate_new.html', {'form': form})


class associate_details(LoginRequiredMixin, UpdateView):
    model = Associate
    form_class = AssociateDetailsForm
    template_name = 'associate_details.html'

    def form_valid(self, form):
        user = User.objects.first()
        self.object = form.save(commit=False)
        self.object.updated_by = user
        self.object.save()
        return redirect('associate_details', self.object.pk)


class eh_personal_info(LoginRequiredMixin, UpdateView):
    model = Associate
    form_class = PersonalInfoForm
    template_name = 'eh_personal_info.html'

    def form_valid(self, form):
        user = User.objects.first()
        self.object = form.save(commit=False)
        self.object.updated_by = user
        self.object.save()
        return redirect('eh_personal_info', self.object.pk)


class eh_contact_info(LoginRequiredMixin, UpdateView):
    model = Associate
    form_class = ContactInfoForm
    template_name = 'eh_contact_info.html'

    def form_valid(self, form):
        user = User.objects.first()
        self.object = form.save(commit=False)
        self.object.updated_by = user
        self.object.save()
        return redirect('eh_contact_info', self.object.pk)


class eh_idproof_info(LoginRequiredMixin, UpdateView):
    model = Associate
    form_class = IDProofInfoForm
    template_name = 'eh_idproof_info.html'

    def form_valid(self, form):
        user = User.objects.first()
        self.object = form.save(commit=False)
        self.object.updated_by = user
        self.object.save()
        return redirect('eh_idproof_info', self.object.pk)


@login_required
def eh_dependant_list(request, pk):
    associate = get_object_or_404(Associate, pk=pk)
    return render(request, 'eh_dependant_list.html', {'associate': associate})


@login_required
def eh_dependant_new(request, pk):
    associate = get_object_or_404(Associate, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = DependantInfoForm(request.POST)
        if form.is_valid():
            Dependant = form.save(commit=False)
            Dependant.Associate = associate
            Dependant.created_by  = user
            Dependant.updated_by = user
            Dependant.save()

            return redirect('eh_dependant_list', pk=associate.pk)  # TODO: redirect to the depdendant details page
    else:
        form = DependantInfoForm()
    return render(request, 'eh_dependant_new.html', {'associate': associate, 'form': form})


class eh_dependant_info(LoginRequiredMixin, UpdateView):
    model = Dependant
    form_class = DependantInfoForm
    template_name = 'eh_dependant_info.html'
    pk_url_kwarg = 'dependant_pk'
    context_object_name = 'dependant'

    def form_valid(self, form):
        user = User.objects.first()
        dependant = form.save(commit=False)
        dependant.updated_by = user
        dependant.save()
        return redirect('eh_dependant_list',pk=dependant.Associate.pk)




def options(request):
    return render(request, 'options.html')





def AssociateExport_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="AssociateExport_csv.csv"'

    writer = csv.writer(response)
    writer.writerow(['First_Name', 'Last_Name', 'Date_of_Birth'])

    associates = Associate.objects.all().values_list('First_Name', 'Last_Name', 'Date_of_Birth')
    for associate in associates:
        writer.writerow(associate)

    return response


def AssociateExport_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="AssociateExport_xls.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Associates')

    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['First_Name', 'Last_Name',  ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Associate.objects.all().values_list('First_Name', 'Last_Name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



def idcard_html(request):
    associates = Associate.objects.all().order_by('First_Name','Last_Name')
    return render(request, 'ids.html', {'associates': associates})


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('ids.html')
        context = {
            'associates': Associate.objects.all().order_by('First_Name','Last_Name')
        }
        html = template.render(context)
        pdf = render_to_pdf('idstyles.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Idcard_%s.pdf" % ("12341231")
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
                response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")




@login_required
def client(request):
    client_list = Client.objects.all().order_by('Name')
    page = request.GET.get('page', 1)
    paginator = Paginator(client_list, 4)
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)
    return render(request, 'client.html', {'clients': clients})


@login_required
def client_new(request):
        form = NewClientForm()
        user = User.objects.first()
        if request.method == 'POST':
            form = NewClientForm(request.POST)
            if form.is_valid():
                Client = form.save(commit=False)
                Client.created_by  = user
                Client.updated_by = user
                Client.created_at = timezone.now()
                Client.updated_at = timezone.now()
                Client.save()

                return redirect('client')
        else:
            form = NewClientForm()
        return render(request, 'client_new.html', {'form': form})


class client_details(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = NewClientForm
    template_name = 'client_details.html'

    def form_valid(self, form):
        user = User.objects.first()
        self.object = form.save(commit=False)
        self.object.updated_by = user
        self.object.save()
        return redirect('client_details', self.object.pk)


