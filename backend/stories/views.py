# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from openai import OpenAI, OpenAIError
# import os

# # Initialize client
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# @api_view(['POST'])
# def generate_story(request):
#     prompt = request.data.get("prompt")
#     if not prompt:
#         return Response({"story": "Please tell me what the story should be about!"})
    
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": "You are a friendly storyteller for children."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         story = response.choices[0].message.content
#         return Response({"story": story})

#     except OpenAIError as e:
#         # Print the real error to your terminal so YOU know what's wrong
#         print(f"OpenAI API Error: {str(e)}")
        
#         # Check specifically for the quota error
#         if "insufficient_quota" in str(e):
#             return Response({"story": "I'm out of magic tokens right now! (The developer needs to add credits to the account)."})
        
#         # Return a friendly message to the user for other errors
#         return Response({"story": "Oops! I couldn't write the story just now. Please try again later!"})

#     except Exception as e:
#         print(f"General Error: {str(e)}")
#         return Response({"story": "Something went wrong with the magic machine!"})


#usin google free engine
from rest_framework.decorators import api_view
from rest_framework.response import Response
import google.generativeai as genai
import os

# Configure the library with your Google Key
# Ensure your .env file has GOOGLE_API_KEY=AIza...
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@api_view(['POST'])
def generate_story(request):
    prompt = request.data.get("prompt")
    if not prompt:
        return Response({"story": "Please tell me what the story should be about!"})

    demo_message = (
    #     "🔒 **PREVIEW MODE ACTIVE**\n\n"
    #     "This system is fully functional and ready to generate stories!\n\n"
    #     "However, the live AI connection is currently paused pending project completion.\n\n"
    #     "**To the Client:** Once the payment is released, the AI will be instantly switched back on, and you will receive the full source code and admin rights.\n\n"
    #     "Thank you!""
        "To access the AI story generation,please pay the project fee.\n\n"
        "Once the payment is confirmed, the AI will be activated, and you will receive the full source code and admin rights.\n\n"
        "Thank you for your understanding!"
    )
    
    return Response({"story": demo_message})    
    
    # try:
    #     # CHANGE HERE: Use 'gemini-pro' instead of 'gemini-1.5-flash'
    #     model = genai.GenerativeModel('gemini-2.5-flash')
        
    #     full_prompt = f"You are a friendly storyteller for children. Write a short story about: {prompt}"
        
    #     response = model.generate_content(full_prompt)
        
    #     # Google returns the text in .text property
    #     story = response.text
    #     return Response({"story": story})

    # except Exception as e:
    #     # This prints the specific error to your terminal for debugging
    #     print(f"Server Error: {str(e)}")
    #     return Response({"story": "The magic storyteller is sleeping right now. Please try again!"})