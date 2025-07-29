# from django.shortcuts import render
# import os
# import requests
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST
# from web.models import Post
# import json


# INSTANCE_ID = os.getenv("INSTANCE_ID")
# TOKEN = os.getenv("TOKEN")

# @csrf_exempt
# @require_POST
# # def webhook(request):
# #     import json
# #     data = json.loads(request.body)
# #     message = data.get('data', {})
# #     sender = message.get('from')  # Ej: '5493512812775@c.us'
# #     text = message.get('body', '').strip().lower()

# #     reply = ""

# #     if "hola" in text:
# #         reply = "👋 ¡Hola! ¿Qué post estás buscando? Podés escribirme una palabra clave como 'Toyota'.\nTambién podés escribir:\n- ayuda\n- ver post 2"
# #     elif "ayuda" in text:
# #         reply = (
# #             "📋 *Comandos disponibles:*\n"
# #             "- hola: saludo inicial\n"
# #             "- ayuda: ver comandos\n"
# #             "- escribir una palabra clave (ej. Toyota): para buscar títulos\n"
# #             "- ver post <número>: para ver el contenido del post"
# #         )
# #     elif text.startswith("ver post"):
# #         try:
# #             # Extraer el número de post
# #             post_id = int(text.replace("ver post", "").strip())
# #             post = Post.objects.get(id=post_id)
# #             reply = f"*{post.titulo}*\n\n{post.contenido[:1000]}"  # Cortamos a 1000 chars por límite de WhatsApp
# #         except (ValueError, Post.DoesNotExist):
# #             reply = "❌ No se encontró ese post. Verificá el número ingresado."
# #     else:
# #         # Buscar coincidencias por palabra clave
# #         resultados = Post.objects.filter(titulo__icontains=text)[:3]
# #         if resultados:
# #             reply = "🔍 Encontré estos posts:\n"
# #             for post in resultados:
# #                 reply += f"- {post.titulo} (id: {post.id})\n"
# #             reply += "\nEscribí 'ver post <id>' para ver más."
# #         else:
# #             reply = "⚠️ No se encontraron resultados. Probá con otra palabra clave."

# #     # Enviar respuesta a WhatsApp
# #     url = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"
# #     params = {
# #         'token': TOKEN
# #     }
# #     payload = {
# #         "to": sender.replace('@c.us', ''),
# #         "body": reply
# #     }

# #     # response = requests.post(url, params=params, data=payload)
# #     # return JsonResponse({"status": "ok", "ultramsg_response": response.json()})
# #     return JsonResponse({"status": "ok", "respuesta_simulada": reply})
     
# # views.py
# def webhook(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         message = data.get("data", {}).get("body", "").lower()

#         if message.startswith("ver post"):
#             try:
#                 post_id = int(message.split("ver post")[1].strip())
#                 post = Post.objects.get(id=post_id)

#                 reply = f"*{post.titulo}*\n\n{post.contenido[:1000]}"
                
#                 if post.imagen:
#                     imagen_url = request.build_absolute_uri(post.imagen.url)
#                     reply += f"\n\n📷 Imagen: {imagen_url}"

#                 return JsonResponse({"status": "ok", "respuesta_simulada": reply})

#             except Exception as e:
#                 return JsonResponse({"status": "error", "message": str(e)})

#         return JsonResponse({"status": "ok", "respuesta_simulada": "Comando no reconocido"})
import os
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from web.models import Post

INSTANCE_ID = os.getenv("INSTANCE_ID")
TOKEN = os.getenv("TOKEN")

@csrf_exempt
@require_POST
def webhook(request):
    try:
        data = json.loads(request.body)
        mensaje = data.get("data", {}).get("body", "").strip()
        numero = data.get("data", {}).get("from", "")
        if not mensaje or not numero:
            return JsonResponse({"error": "No se recibió mensaje o número"}, status=400)

        mensaje_lower = mensaje.lower()

        # Mensajes fijos de ayuda, inicio y menú
        ayuda_texto = (
            "👋 *Bienvenido al Bot del Blog de Autos*\n\n"
            "🔹 Para buscar artículos: envía una palabra clave, ejemplo: *Toyota*\n"
            "🔹 Para ver un post específico: escribe *ver post N*, ejemplo: *ver post 3*\n"
            "🔹 Para volver a ver este mensaje escribe: *ayuda* o *menu*\n"
            "🔹 Saludos: puedes escribir *hola* o *inicio*\n\n"
            "¡Estoy aquí para ayudarte! 🚗💨"
        )

        if mensaje_lower in ["hola", "inicio"]:
            texto_respuesta = "👋 ¡Hola! " + ayuda_texto
            enviar_imagen = False
        elif mensaje_lower in ["ayuda", "menu"]:
            texto_respuesta = ayuda_texto
            enviar_imagen = False
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
                imagen_url = request.build_absolute_uri(post.imagen.url) if post.imagen else None

            except (ValueError, Post.DoesNotExist):
                texto_respuesta = "❌ No encontré un post con ese número. Probá con otro."
                enviar_imagen = False
        else:
            # Buscar posts que contengan la palabra clave en el título
            posts = Post.objects.filter(titulo__icontains=mensaje)[:5]
            if posts.exists():
                titulos = "\n".join([f"- {post.titulo} (ver post {post.id})" for post in posts])
                texto_respuesta = (
                    f"🔎 Resultados para *{mensaje}*:\n{titulos}\n\n"
                    "📖 Para ver el contenido completo escribe: *ver post N* (ejemplo: ver post 3)"
                )
            else:
                texto_respuesta = f"❌ No encontré artículos con la palabra: *{mensaje}*"
            enviar_imagen = False

        # URL base UltraMsg para mensajes de texto o multimedia
        url = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/"

        if enviar_imagen and imagen_url:
            # Enviar mensaje multimedia (imagen + texto)
            payload = {
                "token": TOKEN,
                "to": numero.replace('@c.us', ''),
                "image": imagen_url,
                "caption": texto_respuesta
            }
            response = requests.post(url + "sendfile", data=payload)
        else:
            # Enviar solo texto
            payload = {
                "token": TOKEN,
                "to": numero.replace('@c.us', ''),
                "body": texto_respuesta
            }
            response = requests.post(url + "chat", data=payload)

        return JsonResponse({
            "status": "ok",
            "mensaje_enviado": texto_respuesta,
            "ultramsg_response": response.json()
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
