from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

import requests


class ContactView(TemplateView):
    template_name = 'contact.html'


BOT_TOKEN = "8165026263:AAEdbuMuWrqvMN_xvQWJ70kRi2r49h6cEJ0"
CHAT_ID = "1377513530"


def send_telegram_message(chat_id, message, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML",
    }
    requests.post(url, data=data)


@csrf_exempt
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        telegram_message = (
            f"<b>New Contact Form Submission</b>\n\n"
            f"<b>👤 Name :</b> {name}\n"
            f"<b>📧 Email :</b> {email}\n"
            f"<b>✍️ Subject :</b> {subject}\n"
            f"<b>📩 Message :</b>\n{message}"
        )

        try:
            send_telegram_message(CHAT_ID, telegram_message, BOT_TOKEN)
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, "An error occurred while sending your message. Please try again later.")

        return redirect("contact:home")

    return render(request, "contact.html")
