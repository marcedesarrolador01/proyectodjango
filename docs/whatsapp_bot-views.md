# Webhook de Integración WhatsApp - API UltraMsg (Django)

---

## Descripción

Este módulo expone un endpoint webhook que recibe mensajes entrantes de WhatsApp vía UltraMsg API, procesa el contenido y responde de forma inteligente consultando el modelo `Post` de Django. La integración soporta respuestas de texto y mensajes multimedia (imágenes).

Este enfoque permite implementar un bot de WhatsApp sencillo para un blog de autos, facilitando:

- Respuestas automáticas de ayuda y menús.
- Búsqueda de posts por palabra clave.
- Consulta detallada de posts específicos con imagen adjunta.

---

## Implementación

```python
import os
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from web.models import Post

# Variables sensibles cargadas desde entorno para seguridad y flexibilidad
INSTANCE_ID = os.getenv("INSTANCE_ID")
TOKEN = os.getenv("TOKEN")

@csrf_exempt  # Exento de CSRF porque recibe llamadas externas (webhook)
@require_POST  # Solo acepta POST para evitar GET inseguros
def webhook(request):
    try:
        # Parsear JSON recibido
        data = json.loads(request.body)

        # Extraer mensaje y número remitente con validación básica
        mensaje = data.get("data", {}).get("body", "").strip()
        numero = data.get("data", {}).get("from", "")
        if not mensaje or not numero:
            return JsonResponse({"error": "Parámetros 'mensaje' o 'numero' faltantes."}, status=400)

        mensaje_lower = mensaje.lower()

        # Mensajes predefinidos para interacción básica
        ayuda_texto = (
            "👋 *Bienvenido al Bot del Blog de Autos*\n\n"
            "🔹 Para buscar artículos: envía una palabra clave, ejemplo: *Toyota*\n"
            "🔹 Para ver un post específico: escribe *ver post N*, ejemplo: *ver post 3*\n"
            "🔹 Para volver a ver este mensaje escribe: *ayuda* o *menu*\n"
            "🔹 Saludos: puedes escribir *hola* o *inicio*\n\n"
            "¡Estoy aquí para ayudarte! 🚗💨"
        )

        enviar_imagen = False
        imagen_url = None

        # Logica principal para definir la respuesta según el mensaje recibido
        if mensaje_lower in ["hola", "inicio"]:
            texto_respuesta = f"👋 ¡Hola! {ayuda_texto}"
        elif mensaje_lower in ["ayuda", "menu"]:
            texto_respuesta = ayuda_texto
        elif mensaje_lower.startswith("ver post "):
            try:
                post_id = int(mensaje_lower.replace("ver post ", "").strip())
                post = Post.objects.get(id=post_id)
                texto_respuesta = (
                    f"*{post.titulo}*\n\n"
                    f"{post.contenido[:1000]}\n\n"
                    "📷 Te envío la imagen relacionada."
                )
                enviar_imagen = True
                if post.imagen:
                    imagen_url = request.build_absolute_uri(post.imagen.url)
            except (ValueError, Post.DoesNotExist):
                texto_respuesta = "❌ No encontré un post con ese número. Probá con otro."
        else:
            # Búsqueda de posts por palabra clave en título
            posts = Post.objects.filter(titulo__icontains=mensaje)[:5]
            if posts.exists():
                titulos = "\n".join([f"- {post.titulo} (ver post {post.id})" for post in posts])
                texto_respuesta = (
                    f"🔎 Resultados para *{mensaje}*:\n{titulos}\n\n"
                    "📖 Para ver el contenido completo escribe: *ver post N* (ejemplo: ver post 3)"
                )
            else:
                texto_respuesta = f"❌ No encontré artículos con la palabra: *{mensaje}*"

        # Construcción de la URL base para la API UltraMsg
        base_url = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/"

        # Preparar payload según tipo de mensaje (texto o multimedia)
        if enviar_imagen and imagen_url:
            payload = {
                "token": TOKEN,
                "to": numero.replace('@c.us', ''),
                "image": imagen_url,
                "caption": texto_respuesta
            }
            endpoint = "sendfile"
        else:
            payload = {
                "token": TOKEN,
                "to": numero.replace('@c.us', ''),
                "body": texto_respuesta
            }
            endpoint = "chat"

        # Envío del mensaje a UltraMsg
        response = requests.post(base_url + endpoint, data=payload)
        response.raise_for_status()  # Lanzar excepción si status != 200

        # Respuesta exitosa al servicio que llamó al webhook
        return JsonResponse({
            "status": "ok",
            "mensaje_enviado": texto_respuesta,
            "ultramsg_response": response.json()
        })

    except requests.RequestException as req_err:
        # Captura errores de conexión o HTTP en UltraMsg
        return JsonResponse({"error": f"Error al enviar mensaje: {str(req_err)}"}, status=502)
    except Exception as e:
        # Captura cualquier otra excepción inesperada
        return JsonResponse({"error": f"Error interno: {str(e)}"}, status=500)

Buenas prácticas implementadas
Variables de entorno: Para credenciales y configuración sensible, evita hardcodear datos.

Validación y manejo de errores: Respuestas claras para errores de entrada, errores de red y excepciones inesperadas.

Seguridad: Uso de @csrf_exempt solo donde es estrictamente necesario (webhook externo), y limitación a métodos POST.

Claridad y mantenibilidad: Código legible, con separación lógica clara para cada tipo de mensaje.

Uso eficiente de ORM: Consultas limitadas y manejo de excepciones específicas para evitar fallos.

Respuesta consistente: Se responde siempre con JSON indicando el estado y detalles del proceso.

Logging recomendado: (No incluido aquí, pero sugerido) Para monitoreo en producción registrar errores y eventos importantes.

Requisitos previos
Django configurado con el modelo Post que contenga, al menos, los campos:

titulo (CharField)

contenido (TextField)

imagen (ImageField, opcional)

Variables de entorno definidas:

INSTANCE_ID

TOKEN

Paquete requests instalado y actualizado.

Configuración en URLs de Django apuntando a esta vista para el endpoint webhook.

Mejoras sugeridas
Implementar logging con logging para auditoría y debugging.

Añadir rate limiting para evitar abuso del webhook.

Validar formato y tamaño de mensajes recibidos.

Soporte para más comandos o flujos conversacionales.

Manejo asíncrono o encolado para escalabilidad (Celery, etc.).

