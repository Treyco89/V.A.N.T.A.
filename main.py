print("V.A.N.T.A. is online.")
print("Type 'exit' to shut me down.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("V.A.N.T.A. is shutting down. Goodbye!")
        break
    else:
        print(f"V.A.N.T.A.: You said '{user_input}'. How can I assist you further?")