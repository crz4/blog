from django.http import HttpResponse
from django.views.decorators.http import require_GET

@require_GET
def generate_table(request):
    try:
        size = int(request.GET.get('size', ''))
        if size < 1:
            raise ValueError
    except (ValueError, TypeError):
        return HttpResponse("Некорректный размер", status=400)

    # Генерируем HTML таблицу
    table_html = '<table border="1" cellpadding="5">'
    # Заголовки столбцов
    table_html += '<tr><th></th>'
    for i in range(1, size + 1):
        table_html += f'<th>{i}</th>'
    table_html += '</tr>'

    # Строки таблицы
    for row in range(1, size + 1):
        table_html += f'<tr><th>{row}</th>'
        for col in range(1, size + 1):
            product = row * col
            table_html += f'<td>{product}</td>'
        table_html += '</tr>'

    table_html += '</table>'

    return HttpResponse(table_html)