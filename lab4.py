from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
API_KEY = os.environ["GROQ_API_KEY"]

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

MODEL="llama-3.3-70b-versatile"
print("Client Ready")
print(API_KEY[:10])


#PART 1.1
def ask_llm(user_prompt,
            system_prompt="You are a helpful assistant.",
            temperature =0.7,
            max_tokens=500):

    response= client.chat.completions.create(
        model = MODEL,
        messages =[
        {"role": "system", "content": system_prompt},
      {"role": "user",   "content": user_prompt},
  ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content

#%% md
#They system are instruction given to the model that affect how it behaves for a prompt they don't affect the models weights or parameters just how the model is needed to do it tasks or like the roles they should assume to perform a task. The user gives the task to the model as to what exactly to do. Example System - You are a system designer. Prompt - Design a system for me. A token is how the model reads every character from the prompt so the API charges by token because that what is takes in and also outputs so the prompt is broken down into token and the output is given in token so it chargers per token
#%%
ask_llm("Suggest a name for a savings product for market traders in Accra.",temperature=0.5)

#%% md
#PART 1.2
#%%
question = "Suggest a name for a savings product for market traders in Accra"

print("Temperature Group 0.0\n")
for i in range (5):
    print(ask_llm(question, temperature=0.0))
    print("--"*20)

print("\nTemperature Group 1.2\n")
for i in range (5):
    print(ask_llm(question, temperature=1.2))
    print("--"*20)

#%% md
# SECTION 2
#%%
LETTERS = {
"L001": """Dear Sir/Madam,
My name is Akosua Mensah and I have been selling provisions at Makola Market for 12 years.
I am applying for a loan of GHS 8,000 to buy a deep freezer and expand into frozen foods.
My current stall makes about GHS 900 profit each month. I have saved GHS 2,500 with your
susu scheme over the past two years and I have never missed a contribution. I can repay
GHS 450 monthly over 20 months. My sister, a teacher, will stand as my guarantor.
Thank you for considering my application.""",

"L002": """Hello,
I am Kwame Boateng, a commercial driver in Kumasi. I need GHS 25,000 urgently to repair my
trotro engine and settle some personal debts. Business has been slow but it will surely
pick up after the festive season. I can pay back whenever the money comes. I do not have
collateral at the moment but God willing everything will be fine. Please help me quickly.""",

"L003": """Dear Loan Committee,
I am Efua Darko, owner of Darko Fashions, a registered dressmaking business in Takoradi
(registration no. BN-2019-4482). I employ three apprentices. I request GHS 15,000 to
purchase two industrial sewing machines and fabric stock ahead of the Christmas season.
Last year my December revenue alone was GHS 22,000; monthly profit averages GHS 2,800.
I hold a fixed deposit of GHS 5,000 with GCB which I can pledge. Proposed repayment:
GHS 1,100 monthly for 15 months. Attached are my sales records for the past 18 months.""",

"L004": """Good day,
My name is Yaw Owusu. I want a loan for my poultry farm at Nsawam. The amount is GHS 12,000
for feed and 500 new layers. I started the farm last year. Sometimes I make good money,
around GHS 1,500 in a good month, but bird flu affected us in March and I lost many birds.
I am rebuilding now. I can repay in 18 months. My uncle has agreed to guarantee the loan
with his taxi.""",

"L005": """Dear Manager,
I am writing on behalf of the Adenta Women's Weaving Cooperative (14 members). We seek
GHS 30,000 to buy a bulk order of yarn directly from the factory, cutting out middlemen and
raising our margins from 15% to about 35%. The cooperative has operated for 6 years and
holds GHS 9,000 in our group account. We propose repayment of GHS 2,000 monthly over
16 months, backed by our group savings and joint liability agreement.""",

"L006": """Hi,
This is Kofi. I saw your advert. I want GHS 50,000 to start a car washing business, a
provision shop, and also import phones from Dubai. I am 22 and full of energy. I have not
started any of these yet but my friends say I am very business minded. I will pay back in
one year when the businesses are booming. No collateral but I am trustworthy.""",
}

GOLD = {
  "L001": {"applicant_name": "Akosua Mensah", "amount_ghs": 8000,  "purpose": "buy deep freezer / expand into frozen foods",
           "monthly_profit_ghs": 900,  "has_collateral_or_guarantor": True,  "repayment_months": 20},
  "L003": {"applicant_name": "Efua Darko",    "amount_ghs": 15000, "purpose": "industrial sewing machines and fabric stock",
           "monthly_profit_ghs": 2800, "has_collateral_or_guarantor": True,  "repayment_months": 15},
  "L006": {"applicant_name": "Kofi",          "amount_ghs": 50000, "purpose": "car wash, provision shop, phone imports",
           "monthly_profit_ghs": None, "has_collateral_or_guarantor": False, "repayment_months": 12},
}

print(f"{len(LETTERS)} letters loaded.")
print (LETTERS["L001"])
print (LETTERS["L002"])



# SECTION 3
letters1= LETTERS["L002"]
letters2 =LETTERS["L006"]

summary_prompt_v1= f"""
summarise this:

{letters1}

"""
print(ask_llm(summary_prompt_v1,temperature=0))
print("--"*30)

summary_prompt_v2= f"""
summarise this:

{letters2}
"""
print(ask_llm(summary_prompt_v2,temperature=0))

print("--"*50)


print("\n -------VERSION 2-------")
SYSTEM_PROMPT = """
You are an assistant to a microfinance loan officer.

Your task is to summarize loan applications.

Rules:
- Be factual and neutral.
- Do not invent any information.
- Only use information found in the application.
- Write a concise summary of 3-4 sentences.
"""

summary_prompt_v2 = f"""
Summarize this loan application:

{letters1}
"""
print(ask_llm(summary_prompt_v2,
        SYSTEM_PROMPT,
        temperature=0))
print("--"*50)

summary_prompt_v2 = f"""
Summarize this loan application:

{letters2}
"""
print(ask_llm(summary_prompt_v2,
        SYSTEM_PROMPT,
        temperature=0))

