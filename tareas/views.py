from django.shortcuts import render, redirect
from .models import Tareas
from .forms import Tareas_Form
from django.http import HttpResponse

def ver_tareas(request):
    tarea=Tareas.objects.all()
    return render(request, 'tareas/ver_tareas.html', {'tareas': tarea})

def crear_tarea(request):
    crear=Tareas_Form()
    if request.method == 'POST':
        crear = Tareas_Form(request.POST, request.FILES)
        if crear.is__valid():
            crear.save()
            return redirect('ver_tareas')

        else:
            return HttpResponse("""Tu formulario es incorrecto recarga la pagina 
            en < a href= "{{ url : 'ver_tareas' }}" > Recargar </a>  """)

    else:
        return render(request, 'tareas/formulario_tarea:html', 
                      {'crear': crear}
                      )


def actualizar_tarea(request):
    tarea_id= int(tarea_id)
    try:
        edid_tarea= Tareas.objects.get(id= tarea_id)

    except Tareas.DoesNotExist:
        return redirect('crear_tarea')
    tarea_form=Tareas_Form(request.POST or None, instance=edid_tarea)

    if tarea_form.is_valid():
        tarea_form.save()
        return redirect('ver_tareas') 
    return render(request, 'tareas/formulario_tarea.html',
                  {'editar':edid_tarea}    
                  )


def eliminar_tarea(request):
    tarea_id=int(tarea_id)

    try:
        tarea=Tareas.objects.get(id=tarea_id)

    except Tareas.DoesNotExist:
        return redirect('ver_tareas')

    tarea.delete()
    return redirect('ver_tareas')