from django.http import JsonResponse
from rest_framework.decorators import api_view
import openai

openai.api_key = 'sk-None-uFOIXRElhTfiMLmuhfkQT3BlbkFJzSnnwWVZ6ZHLoFbm06OK'

@api_view(['POST'])
def analyze(request):
    data = request.data
    code = data.get('code', '')
    error_message = data.get('errorMessage', '')
    response = analyze_code_with_gpt(code, error_message)
    return JsonResponse({'response': response})

def analyze_code_with_gpt(code, error_message):
    prompt = f"Explain why the following code does not work and provide suggestions to fix it:\n\nCode:\n{code}\n\nError Message:\n{error_message}"
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

