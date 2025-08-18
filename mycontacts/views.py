from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddForm
from .models import Contact


def show(request):
    """ Lista todos os contatos """
    contact_list = Contact.objects.all()
    return render(request, 'mycontacts/show.html', {'contacts': contact_list})


def add(request):
    """ Adiciona um novo contato """
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            # cria contato manualmente
            Contact.objects.create(
                name=form.cleaned_data['name'],
                relation=form.cleaned_data['relation'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
            )
            return redirect('show')   # depois de salvar volta para a lista
        else:
            return render(request, 'mycontacts/add.html', {'form': form})
    else:
        form = AddForm()
        return render(request, 'mycontacts/add.html', {'form': form})


def detail(request, contact_id):
    """ Mostra detalhes de um contato """
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'mycontacts/detail.html', {'contact': contact})


def edit(request, contact_id):
    """ Edita um contato existente """
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            # atualiza contato manualmente
            contact.name = form.cleaned_data['name']
            contact.relation = form.cleaned_data['relation']
            contact.phone = form.cleaned_data['phone']
            contact.email = form.cleaned_data['email']
            contact.save()
            return redirect('show')
    else:
        # pré-carrega os valores atuais do contato
        form = AddForm(initial={
            'name': contact.name,
            'relation': contact.relation,
            'phone': contact.phone,
            'email': contact.email,
        })
    return render(request, 'mycontacts/edit.html', {'form': form, 'contact': contact})


def delete(request, contact_id):
    """ Deleta um contato """
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('show')
