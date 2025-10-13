from django.shortcuts import render, redirect

def listar_certificados(request):
    certificados = [
        {"usuario": "João Silva", "evento": "Semana de Tecnologia", "data": "2024-11-12"},
        {"usuario": "Maria Santos", "evento": "Palestra de IA", "data": "2024-10-02"},
    ]
    return render(request, 'certificados/listar.html', {'certificados': certificados})

def emitir_certificado(request):
    if request.method == 'POST':
        # Aqui você incluiria a lógica de emissão (salvar no BD, gerar PDF, etc.)
        return redirect('listar_certificados')
    return render(request, 'certificados/emitir.html')
