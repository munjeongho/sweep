from sweepai.utils.openai_proxy import OpenAIProxy

openai_proxy = OpenAIProxy()
resp = openai_proxy.call_openai(
    model="gpt-3.5-turbo-16k",
    messages=[{"role": "user", "content": "I am a human."}],
    max_tokens=100,
    temperature=0.0,
)
print(resp)

resp = openai_proxy.call_openai(
    model="gpt-4",
    messages=[{"role": "user", "content": "I am a human."}],
    max_tokens=100,
    temperature=0.0,
)
print(resp)

resp = openai_proxy.call_openai(
    model="gpt-4-32k",
    messages=[{"role": "user", "content": "I am a human."}],
    max_tokens=100,
    temperature=0.0,
)
print(resp)

resp = openai_proxy.call_openai(
    model="gpt-4-1106-preview",
    messages=[{"role": "user", "content": "I am a human."}],
    max_tokens=100,
    temperature=0.0,
)
print(resp)
