from app.brain.memory_extractor import MemoryExtractor

extractor = MemoryExtractor()

messages = [
    "My name is Shivam",
    "I like Python programming",
    "I am building Jarvis",
    "Hello",
    "How are you?"
]

for message in messages:
    print(f"\nInput: {message}")
    print("Output:", extractor.extract(message))