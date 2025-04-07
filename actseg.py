def buscar_orden(orden):
    data = [{
        "orden": "993513256",
        "cliente": "José",
        "estado": "Completado",
        "fecha_emision": "2025-01-09",
        "fecha_agenda": "2025-02-04",
        "observacion":
        "XEYLIS FABIANA MARCANO | SIN CONTACTO TT, SE CANCELA Q20.",
        "fibra": "ACTIVIDAD BELIEVE- SIN VALIDACION TECNICA"
    }, {
        "orden": "123456789",
        "cliente": "Carlos",
        "estado": "Pendiente",
        "fecha_emision": "2025-03-01",
        "fecha_agenda": "2025-03-05",
        "observacion": "Pendiente por validación",
        "fibra": ""
    }]

    for item in data:
        if item["orden"] == orden:
            return item

    return {
        "orden": orden,
        "cliente": "Desconocido",
        "estado": "No encontrada",
        "fecha_emision": "",
        "fecha_agenda": "",
        "observacion": "No hay datos para esta orden.",
        "fibra": ""
    }
